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
pub struct Segment(Vector2D, Vector2D);
impl From<((i64, i64), (i64, i64))> for Segment {
    fn from(points: ((i64, i64), (i64, i64))) -> Self {
        let (p0, p1) = points;
        Self(p0.into(), p1.into())
    }
}
impl Segment {
    pub fn across(&self, other: &Self) -> bool {
        let v0 = self.1 - self.0;
        let v1 = other.0 - self.0;
        let v2 = other.1 - self.0;
        v0.cross(&v1).signum() * v0.cross(&v2).signum() <= 0
    }

    pub fn intersect(&self, other: &Self) -> bool {
        self.across(other) && other.across(self)
    }
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let x0: i64 = read();
    let y0: i64 = read();
    let x1: i64 = read();
    let y1: i64 = read();
    let s0 = Segment::from(((x0, y0), (x1, y1)));
    let n: usize = read();
    let p: Vec<_> = (0..n).map(|_| (read::<i64>(), read::<i64>())).collect();
    let mut c = 0;
    for i in 0..n {
        let j = (i + 1) % n;
        let s = Segment::from((p[i], p[j]));
        if s.intersect(&s0) {
            c += 1;
        }
    }
    writeln!(writer, "{}", 1 + c / 2).unwrap();
}
