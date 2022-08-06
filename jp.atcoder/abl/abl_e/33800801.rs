pub fn read<T: std::str::FromStr>() -> T {
    use std::io::Read;
    std::io::stdin()
        .lock()
        .by_ref()
        .bytes()
        .map(|c| c.unwrap() as char)
        .skip_while(|c| c.is_whitespace())
        .take_while(|c| !c.is_whitespace())
        .collect::<String>()
        .parse::<T>()
        .ok()
        .unwrap()
}
pub fn bit_length(n: usize) -> usize {
    (0usize.leading_zeros() - n.leading_zeros()) as usize
}
pub trait Identity {
    fn e() -> Self;
}
#[derive(Debug)]
pub struct LazySegtree<S, F> {
    data: Vec<S>,
    lazy: Vec<F>,
    size: usize,
}
// be careful of composition order
impl<S, F> LazySegtree<S, F>
where
    S: Clone + Add<Output = S> + Add<F, Output = S> + Identity,
    F: Clone + Add<Output = F> + Identity,
{
    pub fn new(size: usize) -> Self {
        assert!(size > 0);
        let n = size.next_power_of_two();
        let data = vec![S::e(); n << 1];
        let lazy = vec![F::e(); n];
        Self { data, lazy, size }
    }

    pub fn size(&self) -> usize { self.size }

    fn n(&self) -> usize { self.lazy.len() }

    fn height(&self) -> usize { bit_length(self.n()) }

    fn merge(&mut self, i: usize) {
        self.data[i] =
            self.data[i << 1].clone() + self.data[i << 1 | 1].clone();
    }

    fn apply_node(&mut self, i: usize, f: F) {
        self.data[i] = self.data[i].clone() + f.clone();
        if i < self.n() {
            self.lazy[i] = self.lazy[i].clone() + f;
        }
    }

    fn propagate(&mut self, i: usize) {
        let f = self.lazy[i].clone();
        self.apply_node(i << 1, f.clone());
        self.apply_node(i << 1 | 1, f);
        self.lazy[i] = F::e();
    }

    fn pull(&mut self, i: usize) {
        for j in (1..self.height()).rev() {
            self.propagate(i >> j);
        }
    }

    fn merge_above(&mut self, mut i: usize) {
        while i > 1 {
            i >>= 1;
            self.merge(i);
        }
    }

    pub fn apply(&mut self, mut l: usize, mut r: usize, f: F) {
        assert!(l <= r && r <= self.size);
        let n = self.n();
        l += n;
        r += n;
        let l0 = l >> l.trailing_zeros();
        let r0 = (r >> r.trailing_zeros()) - 1;
        self.pull(l0);
        self.pull(r0);
        while l < r {
            if l & 1 == 1 {
                self.apply_node(l, f.clone());
                l += 1;
            }
            if r & 1 == 1 {
                r -= 1;
                self.apply_node(r, f.clone());
            }
            l >>= 1;
            r >>= 1;
        }
        self.merge_above(l0);
        self.merge_above(r0);
    }

    pub fn set(&mut self, mut i: usize, x: S) {
        assert!(i < self.size);
        i += self.n();
        self.pull(i);
        self.data[i] = x;
        self.merge_above(i);
    }

    pub fn fold(&mut self, mut l: usize, mut r: usize) -> S {
        assert!(l <= r && r <= self.size);
        let n = self.n();
        l += n;
        r += n;
        self.pull(l);
        self.pull(r - 1);
        let mut vl = S::e();
        let mut vr = S::e();
        while l < r {
            if l & 1 == 1 {
                vl = vl + self.data[l].clone();
                l += 1;
            }
            if r & 1 == 1 {
                r -= 1;
                vr = self.data[r].clone() + vr;
            }
            l >>= 1;
            r >>= 1;
        }
        vl + vr
    }

    pub fn max_right<G>(&mut self, is_ok: &G, l: usize) -> usize
    where
        G: Fn(&S) -> bool,
    {
        assert!(l <= self.size);
        if l == self.size {
            return self.size;
        }
        let n = self.n();
        let mut v = S::e();
        let mut i = n + l;
        self.pull(i);
        loop {
            i >>= i.trailing_zeros();
            let nv = v.clone() + self.data[i].clone();
            if !is_ok(&nv) {
                break;
            }
            v = nv;
            i += 1;
            if i.count_ones() == 1 {
                return self.size;
            }
        }
        while i < n {
            self.propagate(i);
            i <<= 1;
            let nv = v.clone() + self.data[i].clone();
            if !is_ok(&nv) {
                continue;
            }
            v = nv;
            i += 1;
        }
        i - n
    }

    pub fn min_left<G>(&mut self, is_ok: &G, r: usize) -> usize
    where
        G: Fn(&S) -> bool,
    {
        assert!(r <= self.size);
        if r == 0 {
            return 0;
        }
        let n = self.n();
        let mut v = S::e();
        let mut i = n + r;
        self.pull(i - 1);
        loop {
            debug_assert!(i >= 1);
            i >>= i.trailing_zeros();
            let nv = self.data[i - 1].clone() + v.clone();
            if !is_ok(&nv) {
                break;
            }
            i -= 1;
            v = nv;
            if i == 0 || i.count_ones() == 1 {
                return 0;
            }
        }
        while i < n {
            debug_assert!(i >= 1);
            self.propagate(i - 1);
            i <<= 1;
            let nv = self.data[i - 1].clone() + v.clone();
            if !is_ok(&nv) {
                continue;
            }
            i -= 1;
            v = nv;
        }
        i - n
    }
}
pub mod modular_frequent {
    use std::{
        marker::PhantomData,
        ops::*,
        sync::atomic::{AtomicI64, Ordering::SeqCst},
    };
    #[derive(Debug, Copy, Clone, Hash, PartialEq, Eq)]
    pub struct DefaultId;
    pub type Mint = Modint<DefaultId>;
    #[derive(Debug, Copy, Clone, Hash, PartialEq, Eq)]
    pub struct Modint<Id>(pub i64, PhantomData<Id>);
    impl<Id> std::fmt::Display for Modint<Id> {
        fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
            write!(f, "{}", self.0)
        }
    }
    impl<Id: Copy> Modint<Id> {
        fn cell() -> &'static AtomicI64 {
            static CELL: AtomicI64 = AtomicI64::new(0);
            &CELL
        }

        pub fn get_mod() -> i64 { Self::cell().load(SeqCst) }

        fn m() -> i64 { Self::get_mod() }

        pub fn set_mod(value: i64) { Self::cell().store(value, SeqCst); }

        pub fn normalize(mut v: i64) -> i64 {
            let m = Self::m();
            if v < -Self::m() || v >= m {
                v %= m;
            }
            if v < 0 {
                v += m;
            }
            v
        }

        pub fn new(v: i64) -> Self { Self(Self::normalize(v), PhantomData) }
    }
    impl<Id: Copy> Add for Modint<Id> {
        type Output = Self;

        fn add(mut self, rhs: Self) -> Self::Output {
            self.0 += rhs.0;
            if self.0 >= Self::m() {
                self.0 -= Self::m();
            }
            self
        }
    }
    impl<Id: Copy> Neg for Modint<Id> {
        type Output = Self;

        fn neg(mut self) -> Self::Output {
            if self.0 != 0 {
                self.0 = Self::m() - self.0;
            }
            self
        }
    }
    impl<Id: Copy> Mul for Modint<Id> {
        type Output = Self;

        fn mul(mut self, rhs: Self) -> Self::Output {
            self.0 *= rhs.0;
            if self.0 >= Self::m() {
                self.0 %= Self::m();
            }
            self
        }
    }
    impl<Id: Copy> MulInv for Modint<Id> {
        type Output = Self;

        fn mul_inv(mut self) -> Self::Output {
            self.0 = modinv(Self::m(), self.0);
            self
        }
    }
    impl<Id: Copy> Sub for Modint<Id> {
        type Output = Self;

        fn sub(self, rhs: Self) -> Self::Output { self + -rhs }
    }
    impl<Id: Copy> Div for Modint<Id> {
        type Output = Self;

        fn div(self, rhs: Self) -> Self::Output { self * rhs.mul_inv() }
    }
    impl<Id: Copy> Add<i64> for Modint<Id> {
        type Output = Self;

        fn add(self, rhs: i64) -> Self::Output { self + Self::new(rhs) }
    }
    impl<Id: Copy> Sub<i64> for Modint<Id> {
        type Output = Self;

        fn sub(self, rhs: i64) -> Self::Output { self - Self::new(rhs) }
    }
    impl<Id: Copy> Mul<i64> for Modint<Id> {
        type Output = Self;

        fn mul(self, rhs: i64) -> Self::Output { self * Self::new(rhs) }
    }
    impl<Id: Copy> Div<i64> for Modint<Id> {
        type Output = Self;

        fn div(self, rhs: i64) -> Self::Output { self / Self::new(rhs) }
    }
    impl<Id: Copy> Add<Modint<Id>> for i64 {
        type Output = Modint<Id>;

        fn add(self, rhs: Modint<Id>) -> Self::Output {
            Modint::<Id>::new(self) + rhs
        }
    }
    impl<Id: Copy> Sub<Modint<Id>> for i64 {
        type Output = Modint<Id>;

        fn sub(self, rhs: Modint<Id>) -> Self::Output {
            Modint::<Id>::new(self) - rhs
        }
    }
    impl<Id: Copy> Mul<Modint<Id>> for i64 {
        type Output = Modint<Id>;

        fn mul(self, rhs: Modint<Id>) -> Self::Output {
            Modint::<Id>::new(self) * rhs
        }
    }
    impl<Id: Copy> Div<Modint<Id>> for i64 {
        type Output = Modint<Id>;

        fn div(self, rhs: Modint<Id>) -> Self::Output {
            Modint::<Id>::new(self) / rhs
        }
    }
    impl<Id: Copy, T> AddAssign<T> for Modint<Id>
    where
        Self: Add<T, Output = Self>,
    {
        fn add_assign(&mut self, rhs: T) { *self = *self + rhs; }
    }
    impl<Id: Copy, T> SubAssign<T> for Modint<Id>
    where
        Self: Sub<T, Output = Self>,
    {
        fn sub_assign(&mut self, rhs: T) { *self = *self - rhs; }
    }
    impl<Id: Copy, T> MulAssign<T> for Modint<Id>
    where
        Self: Mul<T, Output = Self>,
    {
        fn mul_assign(&mut self, rhs: T) { *self = *self * rhs; }
    }
    impl<Id: Copy, T> DivAssign<T> for Modint<Id>
    where
        Self: Div<T, Output = Self>,
    {
        fn div_assign(&mut self, rhs: T) { *self = *self / rhs; }
    }
    impl<Id: Copy> Modint<Id> {
        pub fn pow(self, n: i64) -> Self {
            if n < 0 {
                return self.mul_inv().pow(-n);
            }
            if n == 0 {
                return Self::new(1);
            }
            let mut y = self.pow(n >> 1);
            y *= y;
            if n & 1 == 1 {
                y *= self;
            }
            y
        }
    }
    impl<Id: Copy> From<i32> for Modint<Id> {
        fn from(x: i32) -> Self { Self::new(x as i64) }
    }
    pub fn extgcd(mut a: i64, mut b: i64) -> (i64, i64, i64) {
        use std::mem::swap;
        let (mut x00, mut x01, mut x10, mut x11) = (1, 0, 0, 1);
        while b != 0 {
            let q = a / b;
            a %= b;
            swap(&mut a, &mut b);
            x00 -= q * x01;
            swap(&mut x00, &mut x01);
            x10 -= q * x11;
            swap(&mut x10, &mut x11);
        }
        if a >= 0 { (a, x00, x10) } else { (-a, -x00, -x10) }
    }
    pub fn mod_gcd_inv(modulus: i64, n: i64) -> (i64, i64) {
        let (g, mut x, _) = extgcd(n, modulus);
        let u = modulus / g;
        if x < 0 {
            x += u;
        }
        debug_assert!(0 <= x && x <= u);
        (g, x)
    }
    pub fn modinv(modulus: i64, x: i64) -> i64 {
        let (g, inv) = mod_gcd_inv(modulus, x);
        assert!(g == 1);
        return inv;
    }
    pub trait MulInv {
        type Output;
        fn mul_inv(self) -> Self::Output;
    }
    pub fn cumprod<T>(mut a: Vec<T>) -> Vec<T>
    where
        T: Mul<Output = T> + Clone,
    {
        for i in 0..a.len() - 1 {
            a[i + 1] = a[i + 1].clone() * a[i].clone()
        }
        a
    }
    pub fn factorial<T>(size: usize) -> Vec<T>
    where
        T: Mul<Output = T> + From<i32> + Clone,
    {
        if size == 0 {
            return vec![];
        }
        let mut fact = (0..size as i32).map(|i| i.into()).collect::<Vec<T>>();
        fact[0] = 1.into();
        cumprod(fact)
    }
    pub fn inverse_factorial<T>(size: usize) -> Vec<T>
    where
        T: Mul<Output = T> + MulInv<Output = T> + From<i32> + Clone,
    {
        if size == 0 {
            return vec![];
        }
        let mut inv_fact = (0..size as i32)
            .rev()
            .map(|i| (i + 1).into())
            .collect::<Vec<T>>();
        inv_fact[0] = factorial::<T>(size)[size - 1].clone().mul_inv();
        inv_fact = cumprod(inv_fact);
        inv_fact.reverse();
        inv_fact
    }
    pub struct FactorialTablesFrequentOps<T> {
        pub fact: Vec<T>,
        pub inv_fact: Vec<T>,
    }
    impl<T> FactorialTablesFrequentOps<T>
    where
        T: Clone + Mul<Output = T> + MulInv<Output = T> + From<i32>,
    {
        pub fn new(size: usize) -> Self {
            let fact = factorial(size);
            let inv_fact = inverse_factorial(size);
            Self { fact, inv_fact }
        }

        pub fn p(&self, n: usize, k: usize) -> T {
            if n < k {
                0.into()
            } else {
                self.fact[n].clone() * self.inv_fact[n - k].clone()
            }
        }

        pub fn c(&self, n: usize, k: usize) -> T {
            self.p(n, k) * self.inv_fact[k].clone()
        }

        pub fn h(&self, n: usize, k: usize) -> T {
            if n == 0 { 0.into() } else { self.c(n - 1 + k, k) }
        }

        pub fn inv(&self, n: usize) -> T {
            self.fact[n - 1].clone() * self.inv_fact[n].clone()
        }

        pub fn inv_p(&self, n: usize, k: usize) -> T {
            assert!(k <= n);
            self.inv_fact[n].clone() * self.fact[n - k].clone()
        }

        pub fn inv_c(&self, n: usize, k: usize) -> T {
            self.inv_p(n, k) * self.fact[k].clone()
        }
    }
}
use std::ops::*;

use modular_frequent::*;
#[derive(Clone)]
pub struct S(Mint, Mint);
impl Add for S {
    type Output = Self;

    fn add(self, rhs: Self) -> Self::Output {
        S(self.0 + rhs.0, self.1 + rhs.1)
    }
}
impl Identity for S {
    fn e() -> S { S(0.into(), 0.into()) }
}
#[derive(Clone)]
pub struct F(Option<Mint>);
impl Add for F {
    type Output = Self;

    fn add(self, g: Self) -> Self::Output {
        if g.0.is_some() { g } else { self }
    }
}
impl Identity for F {
    fn e() -> Self { F(None) }
}
impl Add<F> for S {
    type Output = Self;

    fn add(self, f: F) -> Self::Output {
        if let Some(f) = f.0 {
            S(f * self.1.clone(), self.1)
        } else {
            self
        }
    }
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    Mint::set_mod(998_244_353);
    let n: usize = read();
    let q: usize = read();
    let mut seg = LazySegtree::<S, F>::new(n);
    let mut p = Mint::new(1);
    for i in 0..n {
        seg.set(n - 1 - i, S(p.clone(), p.clone()));
        p *= 10;
    }
    for _ in 0..q {
        let l = read::<usize>() - 1;
        let r = read::<usize>() - 1;
        let d: Mint = read::<i32>().into();
        seg.apply(l, r + 1, F(Some(d)));
        writeln!(writer, "{}", seg.fold(0, n).0).unwrap();
    }
}
