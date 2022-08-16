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
    use std::{marker::PhantomData, ops::*};
    pub trait Get {
        type T;
        fn get() -> Self::T;
    }
    #[derive(Debug, Copy, Clone, Hash, PartialEq, Eq)]
    pub struct Mod1_000_000_007;
    impl Get for Mod1_000_000_007 {
        type T = i64;

        fn get() -> Self::T { 1_000_000_007 }
    }
    #[derive(Debug, Copy, Clone, Hash, PartialEq, Eq)]
    pub struct Mod998_244_353;
    impl Get for Mod998_244_353 {
        type T = i64;

        fn get() -> Self::T { 998_244_353 }
    }
    #[derive(Debug, Copy, Clone, Hash, PartialEq, Eq)]
    pub struct Modint<M>(pub i64, PhantomData<M>);
    impl<M> std::fmt::Display for Modint<M> {
        fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
            write!(f, "{}", self.0)
        }
    }
    impl<M: Get<T = i64>> Modint<M> {
        pub fn modulus() -> i64 { M::get() }

        fn m() -> i64 { M::get() }

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
    impl<M: Get<T = i64>> Add for Modint<M> {
        type Output = Self;

        fn add(mut self, rhs: Self) -> Self::Output {
            self.0 += rhs.0;
            if self.0 >= Self::m() {
                self.0 -= Self::m();
            }
            self
        }
    }
    impl<M: Get<T = i64>> Neg for Modint<M> {
        type Output = Self;

        fn neg(mut self) -> Self::Output {
            if self.0 != 0 {
                self.0 = Self::m() - self.0;
            }
            self
        }
    }
    impl<M: Get<T = i64>> Mul for Modint<M> {
        type Output = Self;

        fn mul(mut self, rhs: Self) -> Self::Output {
            self.0 *= rhs.0;
            if self.0 >= Self::m() {
                self.0 %= Self::m();
            }
            self
        }
    }
    impl<M: Get<T = i64>> MulInv for Modint<M> {
        type Output = Self;

        fn mul_inv(mut self) -> Self::Output {
            self.0 = modinv(Self::m(), self.0);
            self
        }
    }
    impl<M: Get<T = i64>> Sub for Modint<M> {
        type Output = Self;

        fn sub(self, rhs: Self) -> Self::Output { self + -rhs }
    }
    impl<M: Get<T = i64>> Div for Modint<M> {
        type Output = Self;

        fn div(self, rhs: Self) -> Self::Output { self * rhs.mul_inv() }
    }
    impl<M: Get<T = i64>> Add<i64> for Modint<M> {
        type Output = Self;

        fn add(self, rhs: i64) -> Self::Output { self + Self::new(rhs) }
    }
    impl<M: Get<T = i64>> Sub<i64> for Modint<M> {
        type Output = Self;

        fn sub(self, rhs: i64) -> Self::Output { self - Self::new(rhs) }
    }
    impl<M: Get<T = i64>> Mul<i64> for Modint<M> {
        type Output = Self;

        fn mul(self, rhs: i64) -> Self::Output { self * Self::new(rhs) }
    }
    impl<M: Get<T = i64>> Div<i64> for Modint<M> {
        type Output = Self;

        fn div(self, rhs: i64) -> Self::Output { self / Self::new(rhs) }
    }
    impl<M: Get<T = i64>> Add<Modint<M>> for i64 {
        type Output = Modint<M>;

        fn add(self, rhs: Modint<M>) -> Self::Output {
            Modint::<M>::new(self) + rhs
        }
    }
    impl<M: Get<T = i64>> Sub<Modint<M>> for i64 {
        type Output = Modint<M>;

        fn sub(self, rhs: Modint<M>) -> Self::Output {
            Modint::<M>::new(self) - rhs
        }
    }
    impl<M: Get<T = i64>> Mul<Modint<M>> for i64 {
        type Output = Modint<M>;

        fn mul(self, rhs: Modint<M>) -> Self::Output {
            Modint::<M>::new(self) * rhs
        }
    }
    impl<M: Get<T = i64>> Div<Modint<M>> for i64 {
        type Output = Modint<M>;

        fn div(self, rhs: Modint<M>) -> Self::Output {
            Modint::<M>::new(self) / rhs
        }
    }
    impl<M: Get<T = i64> + Copy, T> AddAssign<T> for Modint<M>
    where
        Self: Add<T, Output = Self>,
    {
        fn add_assign(&mut self, rhs: T) { *self = *self + rhs; }
    }
    impl<M: Get<T = i64> + Copy, T> SubAssign<T> for Modint<M>
    where
        Self: Sub<T, Output = Self>,
    {
        fn sub_assign(&mut self, rhs: T) { *self = *self - rhs; }
    }
    impl<M: Get<T = i64> + Copy, T> MulAssign<T> for Modint<M>
    where
        Self: Mul<T, Output = Self>,
    {
        fn mul_assign(&mut self, rhs: T) { *self = *self * rhs; }
    }
    impl<M: Get<T = i64> + Copy, T> DivAssign<T> for Modint<M>
    where
        Self: Div<T, Output = Self>,
    {
        fn div_assign(&mut self, rhs: T) { *self = *self / rhs; }
    }
    impl<M: Get<T = i64> + Copy> Modint<M> {
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
    impl<M: Get<T = i64>> From<i32> for Modint<M> {
        fn from(x: i32) -> Self { Self::new(x as i64) }
    }
    impl<M: Get<T = i64>> From<usize> for Modint<M> {
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
pub fn bit_length(n: usize) -> usize {
    (0usize.leading_zeros() - n.leading_zeros()) as usize
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

    fn height(&self) -> usize { bit_length(self.n()) }

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

    pub fn set(&mut self, mut i: usize, x: O::S) {
        assert!(i < self.size);
        i += self.n();
        self.pull(i);
        self.data[i] = x;
        self.merge_above(i);
    }

    pub fn apply(&mut self, mut l: usize, mut r: usize, f: O::F) {
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

    pub fn get(&mut self, mut i: usize) -> O::S {
        assert!(i < self.size);
        i += self.n();
        self.pull(i);
        self.data[i].clone()
    }

    pub fn fold(&mut self, mut l: usize, mut r: usize) -> O::S {
        assert!(l <= r && r <= self.size);
        let n = self.n();
        l += n;
        r += n;
        self.pull(l);
        self.pull(r - 1);
        let mut vl = self.ops.e();
        let mut vr = self.ops.e();
        while l < r {
            if l & 1 == 1 {
                vl = self.ops.op(vl, self.data[l].clone());
                l += 1;
            }
            if r & 1 == 1 {
                r -= 1;
                vr = self.ops.op(self.data[r].clone(), vr);
            }
            l >>= 1;
            r >>= 1;
        }
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
    type Mint = Modint<Mod998_244_353>;
    // Mint::set_mod(998_244_353);
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
