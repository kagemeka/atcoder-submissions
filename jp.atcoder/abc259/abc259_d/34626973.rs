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
pub fn dist2<T>(x0: T, y0: T, x1: T, y1: T) -> T
where
    T: Sub<Output = T> + Clone + Mul<Output = T> + Add<Output = T>,
{
    let dx = x1 - x0;
    let dy = y1 - y0;
    dx.clone() * dx + dy.clone() * dy
}
pub struct Circle(i64, i64, i64);
impl Circle {
    pub fn dist2(&self, rhs: &Self) -> i64 {
        (self.0 - rhs.0).pow(2) + (self.1 - rhs.1).pow(2)
    }

    pub fn intersect(&self, rhs: &Self) -> bool {
        let d = self.dist2(rhs);
        (self.2 - rhs.2).pow(2) <= d && d <= (self.2 + rhs.2).pow(2)
    }

    /// radius power to the 2.
    pub fn r2(&self) -> i64 { self.2.pow(2) }

    pub fn dist2_from_center(&self, x: i64, y: i64) -> i64 {
        dist2(self.0, self.1, x, y)
    }

    pub fn on_circumference(&self, x: i64, y: i64) -> bool {
        self.dist2_from_center(x, y) == self.r2()
    }
}
impl From<(i64, i64, i64)> for Circle {
    fn from(c: (i64, i64, i64)) -> Self { Self(c.0, c.1, c.2) }
}
pub struct UnionFind(Vec<isize>);
impl UnionFind {
    pub fn new(size: usize) -> Self { Self(vec![-1; size]) }

    pub fn root(&mut self, u: usize) -> usize {
        if self.0[u] < 0 {
            return u;
        }
        let r = self.root(self.0[u] as usize);
        self.0[u] = r as isize;
        return r;
    }

    pub fn unite(&mut self, mut u: usize, mut v: usize) {
        u = self.root(u);
        v = self.root(v);
        if u == v {
            return;
        }
        use std::mem::swap;
        if self.0[u] > self.0[v] {
            swap(&mut u, &mut v);
        }
        self.0[u] += self.0[v];
        self.0[v] = u as isize;
    }

    pub fn same(&mut self, u: usize, v: usize) -> bool {
        self.root(u) == self.root(v)
    }
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: usize = read();
    let sx: i64 = read();
    let sy: i64 = read();
    let tx: i64 = read();
    let ty: i64 = read();
    let c: Vec<_> = (0..n)
        .map(|_| Circle::from((read(), read(), read())))
        .collect();
    let mut si = 0;
    let mut ti = 0;
    for i in 0..n {
        if c[i].on_circumference(sx, sy) {
            si = i;
        }
        if c[i].on_circumference(tx, ty) {
            ti = i;
        }
    }
    let mut uf = UnionFind::new(n);
    for i in 0..n {
        for j in 0..i {
            if c[i].intersect(&c[j]) {
                uf.unite(i, j);
            }
        }
    }
    writeln!(writer, "{}", if uf.same(si, ti) { "Yes" } else { "No" }).unwrap();
}
