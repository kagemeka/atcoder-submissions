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
use std::{ops::*, str::FromStr};
#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash, Ord)]
pub struct Fraction(pub i64, pub i64);
impl Fraction {
    /// lower != 0, but accept infinity ?
    pub fn new(upper: i64, lower: i64) -> Self {
        // assert!(lower != 0);
        assert!(upper != 0 || lower != 0);
        let mut v = Self(upper, lower);
        v.normalize();
        v
    }

    fn make_denominator_positive(&mut self) {
        if self.1 < 0 {
            self.0 = -self.0;
            self.1 = -self.1;
        }
    }

    fn reduction(&mut self) {
        let g = gcd(self.0, self.1);
        debug_assert!(g != 0);
        self.0 /= g;
        self.1 /= g;
    }

    fn normalize(&mut self) {
        self.reduction();
        self.make_denominator_positive();
    }

    pub fn normalize_neg_inf_as_inf(&mut self) {
        if self.0 == -1 && self.1 == 0 {
            self.0 = 1;
        }
    }

    pub fn floor(&self) -> i64 { self.0.div_euclid(self.1) }

    pub fn ceil(&self) -> i64 {
        let mut v = self.floor();
        if v * self.1 != self.0 {
            v += 1;
        }
        v
    }
}
impl FromStr for Fraction {
    type Err = Box<dyn std::error::Error>;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let parts: Vec<_> = s.split('.').collect();
        assert!(parts.len() <= 2);
        let mut upper = parts[0].parse::<i64>()?;
        let mut p = 1;
        if parts.len() == 2 {
            p = 10i64.pow(parts[1].len() as u32);
            upper *= p;
            upper += parts[1].parse::<i64>()?;
        }
        Ok(Self::new(upper, p))
    }
}
impl PartialOrd for Fraction {
    fn ge(&self, other: &Self) -> bool { !(self < other) }

    fn gt(&self, other: &Self) -> bool { !(self <= other) }

    fn le(&self, other: &Self) -> bool { self < other || self == other }

    fn lt(&self, other: &Self) -> bool { (*self - *other).0 < 0 }

    fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {
        use std::cmp::Ordering::*;
        Some(if self < other {
            Less
        } else if self == other {
            Equal
        } else {
            Greater
        })
    }
}
impl Add for Fraction {
    type Output = Self;

    fn add(self, rhs: Self) -> Self::Output {
        let l = lcm(self.1, rhs.1);
        Self(l / self.1 * self.0 + l / rhs.1 * rhs.0, l)
    }
}
impl AddAssign for Fraction {
    fn add_assign(&mut self, rhs: Self) { *self = *self + rhs; }
}
impl Neg for Fraction {
    type Output = Self;

    fn neg(self) -> Self::Output { Self(-self.0, self.1) }
}
impl Sub for Fraction {
    type Output = Self;

    fn sub(self, rhs: Self) -> Self::Output { self + -rhs }
}
impl SubAssign for Fraction {
    fn sub_assign(&mut self, rhs: Self) { *self = *self - rhs; }
}
impl Mul for Fraction {
    type Output = Self;

    fn mul(mut self, mut rhs: Self) -> Self::Output {
        let mut g = gcd(self.0, rhs.1);
        self.0 /= g;
        rhs.1 /= g;
        g = gcd(self.1, rhs.0);
        self.1 /= g;
        rhs.0 /= g;
        let mut res = Self(self.0 * rhs.0, self.1 * rhs.1);
        res.make_denominator_positive();
        res
    }
}
impl MulAssign for Fraction {
    fn mul_assign(&mut self, rhs: Self) { *self = *self * rhs; }
}
impl MulInv for Fraction {
    type Output = Self;

    fn mul_inv(mut self) -> Self::Output {
        use std::mem::swap;
        swap(&mut self.0, &mut self.1);
        self.make_denominator_positive();
        self
    }
}
impl Div for Fraction {
    type Output = Self;

    fn div(self, rhs: Self) -> Self::Output { self * rhs.mul_inv() }
}
impl DivAssign for Fraction {
    fn div_assign(&mut self, rhs: Self) { *self = *self / rhs; }
}
pub trait MulInv {
    type Output;
    fn mul_inv(self) -> Self::Output;
}
pub fn gcd(a: i64, b: i64) -> i64 {
    if b == 0 { a.abs() } else { gcd(b, a % b) }
}
pub fn lcm(a: i64, b: i64) -> i64 {
    if a == 0 && b == 0 { 0 } else { (a / gcd(a, b) * b).abs() }
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
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: usize = read();
    let mut zz = 0;
    let mut cnt = std::collections::HashMap::new();
    let mut ab = Vec::new();
    for _ in 0..n {
        let a: i64 = read();
        let b: i64 = read();
        if a == 0 && b == 0 {
            zz += 1;
            continue;
        }
        let mut f = Fraction::new(a, b);
        f.normalize_neg_inf_as_inf();
        *cnt.entry(f).or_insert(0) += 1;
        ab.push(f);
    }
    use modular_frequent::*;
    type Mint = Mint1_000_000_007;
    let mut p = Mint::from(1);
    let k = 1 << 18;
    let mut pow2 = vec![Mint::new(2); k];
    pow2[0] = 1.into();
    for i in 0..k - 1 {
        pow2[i + 1] = pow2[i + 1] * pow2[i];
    }
    for x in ab.iter() {
        let y = &mut x.mul_inv();
        y.normalize_neg_inf_as_inf();
        y.0 *= -1;
        let mut s: Mint = 1.into();
        s += pow2[*cnt.entry(*x).or_insert(0)] - 1;
        s += pow2[*cnt.entry(*y).or_insert(0)] - 1;
        *cnt.get_mut(x).unwrap() = 0;
        *cnt.get_mut(y).unwrap() = 0;
        p *= s;
    }
    p -= 1;
    p += zz;
    writeln!(writer, "{}", p).unwrap();
}
