// it's gonna be TLE
// this submission is just for checking DFT
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
pub fn dft_convolve(mut a: Vec<Complex>, mut b: Vec<Complex>) -> Vec<Complex> {
    let k = a.len() + b.len() - 1;
    a.resize(k, Complex::zero());
    b.resize(k, Complex::zero());
    let c: Vec<_> = dft(&a)
        .into_iter()
        .zip(dft(&b).into_iter())
        .map(|(a, b)| a * b)
        .collect();
    idft(&c)
}
pub fn from_i64(a: &[i64], b: &[i64]) -> Vec<i64> {
    let a: Vec<_> = a.iter().map(|x| Complex(*x as f64, 0.0)).collect();
    let b: Vec<_> = b.iter().map(|x| Complex(*x as f64, 0.0)).collect();
    dft_convolve(a, b)
        .into_iter()
        .map(|x| x.rint() as i64)
        .collect()
}
pub fn dft(a: &[Complex]) -> Vec<Complex> {
    let n = a.len();
    (0..n)
        .map(|i| {
            let mut b = Complex(0., 0.);
            for (j, &a) in a.iter().enumerate() {
                b += a * Complex::from_polar(
                    1.0,
                    -2. * PI * i as f64 * j as f64 / n as f64,
                );
            }
            b
        })
        .collect()
}
pub fn idft(b: &[Complex]) -> Vec<Complex> {
    let n = b.len();
    (0..n)
        .map(|i| {
            let mut a = Complex(0., 0.);
            for (j, &b) in b.iter().enumerate() {
                a += b * Complex::from_polar(
                    1.0,
                    2. * PI * i as f64 * j as f64 / n as f64,
                );
            }
            a / n as f64
        })
        .collect()
}
use std::f64::consts::*;
#[derive(Debug, Clone, Copy, PartialEq)]
pub struct Complex(pub f64, pub f64);
impl From<f64> for Complex {
    fn from(real: f64) -> Self { Self(real, 0.0) }
}
impl From<(f64, f64)> for Complex {
    fn from(rect: (f64, f64)) -> Self { Self(rect.0, rect.1) }
}
impl Complex {
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
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: usize = read();
    let mut f = vec![0; n + 1];
    let mut g = vec![0; n + 1];
    for i in 0..n {
        f[i + 1] = read();
        g[i + 1] = read();
    }
    let h = from_i64(&f, &g);
    for x in h[1..].iter() {
        writeln!(writer, "{}", x).unwrap();
    }
}
