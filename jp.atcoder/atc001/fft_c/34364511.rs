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
use std::f64::consts::*;
/// rectangular form (real, imaginary)
#[derive(Debug, Clone, Copy, PartialEq)]
pub struct Complex(pub f64, pub f64);
impl From<f64> for Complex {
    fn from(real: f64) -> Self { Self(real, 0.0) }
}
impl From<(f64, f64)> for Complex {
    fn from(rect: (f64, f64)) -> Self { Self(rect.0, rect.1) }
}
impl Complex {
    /// as f64 real integer
    pub fn rint(&self) -> f64 { self.0.round() }

    pub fn zero() -> Self { Self(0.0, 0.0) }

    pub fn one() -> Self { Self(1.0, 0.0) }

    pub fn i() -> Self { Self(0.0, 1.0) }

    pub fn norm_square(&self) -> f64 { self.0 * self.0 + self.1 * self.1 }

    pub fn conjugate(&self) -> Self { Self(self.0, -self.1) }

    pub fn mul_inv(&self) -> Self {
        let ns = self.norm_square();
        Self(self.0 / ns, -self.1 / ns)
    }

    pub fn argument(&self) -> f64 { self.1.atan2(self.0) }

    pub fn norm(&self) -> f64 { self.0.hypot(self.1) }

    pub fn polar(&self) -> (f64, f64) { (self.norm(), self.argument()) }

    pub fn from_polar(r: f64, theta: f64) -> Self {
        Self::rectangular(r, theta)
    }

    pub fn rectangular(r: f64, theta: f64) -> Self {
        Self(r * theta.cos(), r * theta.sin())
    }

    /// e^{a + bi} = e^a * e^{bi} = e^a * (cos(b) + i*sin(b))
    pub fn exp(&self) -> Self {
        Self(self.1.cos(), self.1.sin()) * self.0.exp()
    }

    /// t := arg(z)
    /// z = |z|*exp(i*t) = exp(ln(|z|) + i*t)
    /// ln(z) = ln(|z|) + i*t
    pub fn ln(&self) -> Self { Self(self.norm().ln(), self.argument()) }

    pub fn sqrt(&self) -> Complex {
        let (r, theta) = self.polar();
        Self::rectangular(r, theta / 2.0)
    }

    /// sin(a + bi) = sin(a)cosh(b) + i*cos(a)sinh(b)
    pub fn sin(&self) -> Complex {
        Self(self.0.sin() * self.1.cosh(), self.0.cos() * self.1.sinh())
    }

    /// cos(a + bi) = cos(a)cosh(b) - i*sin(a)sinh(b)
    pub fn cos(&self) -> Complex {
        Self(self.0.cos() * self.1.cosh(), -self.0.sin() * self.1.sinh())
    }

    /// tan(a + bi) = (sin(2a) + i*sinh(2b)) / (cos(2a) + cosh(2b))
    pub fn tan(&self) -> Complex {
        let Self(a, b) = *self * 2.0;
        Self(a.sin(), b.sinh()) / (a.cos() + b.cosh())
    }
}
use std::ops::*;
impl MulAssign<f64> for Complex {
    fn mul_assign(&mut self, x: f64) {
        self.0 *= x;
        self.1 *= x;
    }
}
impl Mul<f64> for Complex {
    type Output = Self;

    fn mul(mut self, x: f64) -> Self::Output {
        self *= x;
        self
    }
}
impl DivAssign<f64> for Complex {
    fn div_assign(&mut self, x: f64) {
        self.0 /= x;
        self.1 /= x;
    }
}
impl Div<f64> for Complex {
    type Output = Self;

    fn div(mut self, x: f64) -> Self::Output {
        self /= x;
        self
    }
}
impl AddAssign for Complex {
    fn add_assign(&mut self, rhs: Self) {
        self.0 += rhs.0;
        self.1 += rhs.1;
    }
}
impl Add for Complex {
    type Output = Self;

    fn add(mut self, rhs: Self) -> Self::Output {
        self += rhs;
        self
    }
}
impl MulAssign for Complex {
    fn mul_assign(&mut self, rhs: Self) { *self = *self * rhs; }
}
impl Mul for Complex {
    type Output = Self;

    fn mul(self, rhs: Self) -> Self::Output {
        Self(
            self.0 * rhs.0 - self.1 * rhs.1,
            self.0 * rhs.1 + self.1 * rhs.0,
        )
    }
}
impl Neg for Complex {
    type Output = Self;

    fn neg(self) -> Self::Output { Self(-self.0, -self.1) }
}
impl SubAssign for Complex {
    fn sub_assign(&mut self, rhs: Self) { *self += -rhs; }
}
impl Sub for Complex {
    type Output = Self;

    fn sub(mut self, rhs: Self) -> Self::Output {
        self -= rhs;
        self
    }
}
impl DivAssign for Complex {
    fn div_assign(&mut self, rhs: Self) { *self *= rhs.mul_inv(); }
}
impl Div for Complex {
    type Output = Self;

    fn div(mut self, rhs: Self) -> Self::Output {
        self /= rhs;
        self
    }
}
pub fn fft(mut a: Vec<Complex>, bit_len: usize) -> Vec<Complex> {
    use std::mem::size_of;
    let n = 1 << bit_len;
    a.resize(n, Complex::zero());
    // bit reversal permutate (buttefly)
    for i in 0..n {
        let j = i.reverse_bits() >> (size_of::<usize>() << 3) - bit_len;
        if i < j {
            a.swap(i, j);
        }
    }
    // divide and conquer along with inverse butterfly
    let mut d = 1;
    while d < n {
        for j in 0..d {
            let w = Complex::from_polar(1.0, -PI / d as f64 * j as f64);
            for i in (j..n).step_by(d << 1) {
                let s = a[i];
                let t = a[i + d] * w;
                a[i] = s + t;
                a[i + d] = s - t;
            }
        }
        d <<= 1;
    }
    a
}
pub fn ifft(mut a: Vec<Complex>, bit_len: usize) -> Vec<Complex> {
    use std::mem::size_of;
    let n = 1 << bit_len;
    a.resize(n, Complex::zero());
    for i in 0..n {
        let j = i.reverse_bits() >> (size_of::<usize>() << 3) - bit_len;
        if i < j {
            a.swap(i, j);
        }
    }
    let mut d = 1;
    while d < n {
        for j in 0..d {
            let w = Complex::from_polar(1.0, PI / d as f64 * j as f64);
            for i in (j..n).step_by(d << 1) {
                let s = a[i];
                let t = a[i + d] * w;
                a[i] = s + t;
                a[i + d] = s - t;
            }
        }
        d <<= 1;
    }
    for x in a.iter_mut() {
        *x /= n as f64;
    }
    a
}
pub fn fft_convolve(a: Vec<Complex>, b: Vec<Complex>) -> Vec<Complex> {
    let k = a.len() + b.len() - 1;
    let bit_len = k.next_power_of_two().trailing_zeros() as usize;
    let c: Vec<_> = fft(a, bit_len)
        .into_iter()
        .zip(fft(b, bit_len).into_iter())
        .map(|(a, b)| a * b)
        .collect();
    ifft(c, bit_len).into_iter().take(k).collect()
}
pub fn from_i64(a: &[i64], b: &[i64]) -> Vec<i64> {
    let a: Vec<_> = a.iter().map(|x| Complex(*x as f64, 0.0)).collect();
    let b: Vec<_> = b.iter().map(|x| Complex(*x as f64, 0.0)).collect();
    fft_convolve(a, b)
        .into_iter()
        .map(|x| x.rint() as i64)
        .collect()
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: usize = read();
    let mut a = vec![0; n + 1];
    let mut b = vec![0; n + 1];
    for i in 0..n {
        a[i + 1] = read();
        b[i + 1] = read();
    }
    let c = from_i64(&a, &b);
    for x in c[1..].iter() {
        writeln!(writer, "{}", x).unwrap();
    }
}
