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
    pub type Mint1_000_000_007 = Modint<Mod1_000_000_007>;
    pub type Mint998_244_353 = Modint<Mod998_244_353>;
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
pub fn edge_count(adj_bits: &[usize]) -> Vec<usize> {
    let g = adj_bits;
    let n = g.len();
    let n2 = 1 << n;
    let mut f = vec![0; n2];
    for s in 1..n2 {
        let i = s.trailing_zeros() as usize;
        f[s] = f[s & (s - 1)] + (s & g[i]).count_ones() as usize;
    }
    f
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    use modular_frequent::*;
    type Mint = Mint998_244_353;
    let n: usize = read();
    let m: usize = read();
    let mut g = vec![0; n];
    for _ in 0..m {
        let u = read::<usize>() - 1;
        let v = read::<usize>() - 1;
        g[u] |= 1 << v;
        g[v] |= 1 << u;
    }
    let n2 = 1 << n;
    let ec = edge_count(&g);
    let mut pow2 = vec![Mint::new(2); m + 1];
    pow2[0] = 1.into();
    for i in 0..m {
        pow2[i + 1] = pow2[i + 1] * pow2[i];
    }
    let mut dp = vec![Mint::new(0); n2];
    for s in 0..n2 {
        if s & 1 == 0 {
            continue;
        }
        let mut t = s;
        dp[s] = pow2[ec[s]];
        while t > 0 {
            t = (t - 1) & s;
            if t & 1 == 0 {
                continue;
            }
            dp[s] = dp[s] - dp[t] * pow2[ec[s ^ t]];
        }
    }
    let mut res = vec![Mint::new(0); n];
    for s in 0..n2 {
        for i in 0..n {
            if s >> i & 1 == 0 {
                continue;
            }
            res[i] += dp[s] * pow2[ec[(n2 - 1) ^ s]];
        }
    }
    for x in res[1..].iter() {
        writeln!(writer, "{}", x).unwrap();
    }
}
