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
use std::ops::*;
#[derive(Debug, Clone, Copy, Eq, PartialEq, Hash)]
pub struct Vector2D(i64, i64);
impl From<(i64, i64)> for Vector2D {
    fn from(p: (i64, i64)) -> Self { Self(p.0, p.1) }
}
impl AddAssign for Vector2D {
    fn add_assign(&mut self, rhs: Self) {
        self.0 += rhs.0;
        self.1 += rhs.1;
    }
}
impl Add for Vector2D {
    type Output = Self;

    fn add(mut self, rhs: Self) -> Self::Output {
        self += rhs;
        self
    }
}
impl Neg for Vector2D {
    type Output = Self;

    fn neg(mut self) -> Self::Output {
        self.0 *= -1;
        self.1 *= -1;
        self
    }
}
impl SubAssign for Vector2D {
    fn sub_assign(&mut self, rhs: Self) { *self += -rhs; }
}
impl Sub for Vector2D {
    type Output = Self;

    fn sub(mut self, rhs: Self) -> Self::Output {
        self -= rhs;
        self
    }
}
impl Mul for Vector2D {
    type Output = i64;

    fn mul(self, rhs: Self) -> Self::Output { self.0 * rhs.0 + self.1 * rhs.1 }
}
impl MulAssign<i64> for Vector2D {
    fn mul_assign(&mut self, x: i64) {
        self.0 *= x;
        self.1 *= x;
    }
}
impl Mul<i64> for Vector2D {
    type Output = Self;

    fn mul(mut self, x: i64) -> Self::Output {
        self *= x;
        self
    }
}
impl DivAssign<i64> for Vector2D {
    fn div_assign(&mut self, x: i64) {
        assert!(self.0 % x == 0 && self.1 % x == 0);
        self.0 /= x;
        self.1 /= x;
    }
}
impl Div<i64> for Vector2D {
    type Output = Self;

    fn div(mut self, rhs: i64) -> Self::Output {
        self /= rhs;
        self
    }
}
impl Vector2D {
    pub fn cross(&self, rhs: &Self) -> i64 { self.0 * rhs.1 - self.1 * rhs.0 }

    pub fn dot(&self, rhs: &Self) -> i64 { *self * *rhs }

    pub fn norm2(&self) -> i64 { self.dot(self) }

    pub fn norm(&self) -> f64 { (self.norm2() as f64).sqrt() }
}
pub struct Triangle(Vector2D, Vector2D, Vector2D);
impl From<((i64, i64), (i64, i64), (i64, i64))> for Triangle {
    fn from(points: ((i64, i64), (i64, i64), (i64, i64))) -> Self {
        let (p0, p1, p2) = points;
        Self(p0.into(), p1.into(), p2.into())
    }
}
impl Triangle {
    pub fn singed_area(&self) -> f64 {
        (self.1 - self.0).cross(&(self.2 - self.0)) as f64 / 2.
    }

    pub fn area(&self) -> f64 { self.singed_area().abs() }
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let x0: i64 = read();
    let y0: i64 = read();
    let x1: i64 = read();
    let y1: i64 = read();
    let x2: i64 = read();
    let y2: i64 = read();
    let t: Triangle = ((x0, y0), (x1, y1), (x2, y2)).into();
    writeln!(writer, "{}", t.area()).unwrap();
}
