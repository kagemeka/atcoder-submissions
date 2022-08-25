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
#[derive(Debug, Clone, Copy, Eq, PartialEq, Hash, Ord)]
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
impl Vector2D {
    /// [0, \pi)
    fn positive_angle(&self) -> bool {
        self.1 > 0 || self.1 == 0 && self.0 == 0
    }

    /// self < rhs ?
    /// [-\pi, \pi)
    pub fn angle_lt(&self, rhs: &Self) -> bool {
        let a = self.positive_angle();
        let b = rhs.positive_angle();
        if a != b { b } else { self.cross(rhs) > 0 }
    }

    pub fn radian(&self) -> f64 { (self.1 as f64).atan2(self.0 as f64) }
}
impl Vector2D {
    pub fn is_acute(&self) -> bool { self.1 > 0 && self.0 > 0 }

    pub fn is_othogonal(&self) -> bool { self.1 > 0 && self.0 == 0 }

    pub fn is_obtuse(&self) -> bool { self.1 > 0 && self.0 < 0 }

    pub fn acute(&self, other: &Self) -> bool {
        self.cross(other) > 0 && self.dot(other) > 0
    }

    pub fn othogonal(&self, other: &Self) -> bool {
        self.cross(other) > 0 && self.dot(other) == 0
    }

    pub fn obtuse(&self, other: &Self) -> bool {
        self.cross(other) > 0 && self.dot(other) < 0
    }
}
impl PartialOrd for Vector2D {
    fn lt(&self, other: &Self) -> bool { self.angle_lt(other) }

    fn le(&self, other: &Self) -> bool { self == other && self <= other }

    fn ge(&self, other: &Self) -> bool { !(self < other) }

    fn gt(&self, other: &Self) -> bool { !(self <= other) }

    fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {
        use std::cmp::Ordering::*;
        let res = if self == other {
            Equal
        } else if self < other {
            Less
        } else {
            Greater
        };
        Some(res)
    }
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: usize = read();
    let p: Vec<_> = (0..n)
        .map(|_| Vector2D::from((read::<i64>(), read::<i64>())))
        .collect();
    let mut s = 0; // s := 2s = 8a
    for i in 1..n - 1 {
        s += (p[i] - p[0]).cross(&(p[i + 1] - p[0]));
    }
    // sum(4 * cross) > s
    let mut j = 0;
    let mut mn = std::i64::MAX;
    let mut x = 0;
    for i in 0..n {
        let p0 = p[i];
        while j < i + n - 1 && x < s {
            mn = mn.min(s - x);
            x += (p[j % n] - p0).cross(&(p[(j + 1) % n] - p0)) * 4;
            j += 1;
        }
        mn = mn.min(x - s);
        let pj = p[j % n];
        x -= (p0 - pj).cross(&(p[(i + 1) % n] - pj)) * 4;
        assert!(x >= 0);
    }
    writeln!(writer, "{}", mn).unwrap();
}
