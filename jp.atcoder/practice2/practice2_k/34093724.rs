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
    impl<Id: Copy> From<usize> for Modint<Id> {
        fn from(x: usize) -> Self { Self::new(x as i64) }
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
        T: Mul<Output = T> + Div<Output = T> + From<i32> + Clone,
    {
        if size == 0 {
            return vec![];
        }
        let mut inv_fact = (0..size as i32)
            .rev()
            .map(|i| (i + 1).into())
            .collect::<Vec<T>>();
        inv_fact[0] = T::from(1) / factorial::<T>(size)[size - 1].clone();
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
        T: Clone + Mul<Output = T> + Div<Output = T> + From<i32>,
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
pub trait Ops {
    type S;
    type F;
    fn op(&self, a: Self::S, b: Self::S) -> Self::S;
    fn e(&self) -> Self::S;
    fn compose(&self, f: Self::F, g: Self::F) -> Self::F;
    fn id(&self) -> Self::F;
    fn map(&self, f: Self::F, x: Self::S) -> Self::S;
}
#[derive(Debug)]
pub struct LazySegtree<O: Ops> {
    ops: O,
    data: Vec<O::S>,
    lazy: Vec<O::F>,
    size: usize,
}
impl<O: Ops> LazySegtree<O>
where
    O::S: Clone,
    O::F: Clone,
{
    pub fn new(ops: O, size: usize) -> Self {
        assert!(size > 0);
        let n = size.next_power_of_two();
        let data = vec![ops.e(); n << 1];
        let lazy = vec![ops.id(); n];
        Self { ops, data, lazy, size }
    }

    pub fn size(&self) -> usize { self.size }

    fn n(&self) -> usize { self.lazy.len() }

    fn merge(&mut self, i: usize) {
        self.data[i] = self
            .ops
            .op(self.data[i << 1].clone(), self.data[i << 1 | 1].clone());
    }

    fn apply_node(&mut self, i: usize, f: O::F) {
        self.data[i] = self.ops.map(f.clone(), self.data[i].clone());
        if i < self.n() {
            self.lazy[i] = self.ops.compose(f, self.lazy[i].clone());
        }
    }

    fn propagate(&mut self, i: usize) {
        let f = self.lazy[i].clone();
        self.apply_node(i << 1, f.clone());
        self.apply_node(i << 1 | 1, f);
        self.lazy[i] = self.ops.id();
    }

    pub fn set(&mut self, i: usize, x: O::S) {
        assert!(i < self.size());
        self._set(i, 0, self.n(), 1, x);
    }

    fn _set(&mut self, i: usize, cl: usize, cr: usize, ci: usize, x: O::S) {
        assert!(cl <= i && i < cr);
        if cr - cl == 1 {
            self.data[ci] = x;
            return;
        }
        self.propagate(ci);
        let c = (cl + cr) >> 1;
        if i < c {
            self._set(i, cl, c, ci << 1, x);
        } else {
            self._set(i, c, cr, ci << 1 | 1, x);
        }
        self.merge(ci);
    }

    pub fn apply(&mut self, l: usize, r: usize, f: O::F) {
        assert!(l <= r && r <= self.size);
        self._apply(l, r, 0, self.n(), 1, f);
    }

    fn _apply(
        &mut self, l: usize, r: usize, cl: usize, cr: usize, i: usize, f: O::F,
    ) {
        if cr <= l || r <= cl {
            return;
        }
        if l <= cl && cr <= r {
            self.apply_node(i, f);
            return;
        }
        self.propagate(i);
        let c = (cl + cr) >> 1;
        self._apply(l, r, cl, c, i << 1, f.clone());
        self._apply(l, r, c, cr, i << 1 | 1, f);
        self.merge(i);
    }

    pub fn get(&mut self, i: usize) -> O::S { self.fold(i, i + 1) }

    pub fn fold(&mut self, l: usize, r: usize) -> O::S {
        assert!(l <= r && r <= self.size);
        self._fold(l, r, 0, self.n(), 1)
    }

    fn _fold(
        &mut self, l: usize, r: usize, cl: usize, cr: usize, i: usize,
    ) -> O::S {
        if cr <= l || r <= cl {
            return self.ops.e();
        }
        if l <= cl && cr <= r {
            return self.data[i].clone();
        }
        self.propagate(i);
        let c = (cl + cr) >> 1;
        let vl = self._fold(l, r, cl, c, i << 1);
        let vr = self._fold(l, r, c, cr, i << 1 | 1);
        self.ops.op(vl, vr)
    }
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: usize = read();
    let q: usize = read();
    let a: Vec<_> = (0..n).map(|_| read::<i32>()).collect();
    use modular_frequent::*;
    Mint::set_mod(998_244_353);
    use std::{marker::PhantomData, ops::*};
    struct RangeAffineRangeSum<T>(PhantomData<T>);
    impl<T> RangeAffineRangeSum<T> {
        pub fn new() -> Self { Self(PhantomData) }
    }
    impl<T> Ops for RangeAffineRangeSum<T>
    where
        T: From<i32> + Clone + Mul<Output = T> + Add<Output = T>,
    {
        type F = (T, T);
        // (a, b)
        type S = (T, T);

        // (sum, len)
        fn compose(&self, f: Self::F, g: Self::F) -> Self::F {
            (f.0.clone() * g.0, f.0 * g.1 + f.1)
        }

        fn e(&self) -> Self::S { (0.into(), 0.into()) }

        fn op(&self, a: Self::S, b: Self::S) -> Self::S {
            (a.0 + b.0, a.1 + b.1)
        }

        fn id(&self) -> Self::F { (1.into(), 0.into()) }

        fn map(&self, f: Self::F, x: Self::S) -> Self::S {
            (f.0 * x.0 + f.1 * x.1.clone(), x.1)
        }
    }
    let mut seg = LazySegtree::new(RangeAffineRangeSum::<Mint>::new(), n);
    for i in 0..n {
        seg.set(i, (a[i].into(), 1.into()));
    }
    for _ in 0..q {
        let t: usize = read();
        let l: usize = read();
        let r: usize = read();
        if t == 0 {
            let b: i32 = read();
            let c: i32 = read();
            seg.apply(l, r, (b.into(), c.into()));
        } else {
            writeln!(writer, "{}", seg.fold(l, r).0).unwrap();
        }
    }
}
