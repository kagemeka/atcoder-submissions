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
pub trait Monoid {
    type T;
    fn op(&self, _: Self::T, _: Self::T) -> Self::T;
    fn e(&self) -> Self::T;
}
pub struct SegmentTree<G: Monoid> {
    g: G,
    pub(crate) size: usize,
    pub(crate) data: Vec<G::T>,
}
impl<G: Monoid> SegmentTree<G> {
    fn n(&self) -> usize { self.data.len() >> 1 }
}
use std::ops::*;
impl<G: Monoid> Index<usize> for SegmentTree<G> {
    type Output = G::T;

    fn index(&self, i: usize) -> &Self::Output { &self.data[i + self.n()] }
}
impl<G: Monoid> SegmentTree<G>
where
    G::T: Clone,
{
    fn update(&mut self, i: usize) {
        self.data[i] = self
            .g
            .op(self.data[i << 1].clone(), self.data[i << 1 | 1].clone());
    }

    pub fn new(g: G, size: usize) -> Self {
        assert!(size > 0);
        let data = vec![g.e(); size.next_power_of_two() << 1];
        Self { g, size, data }
    }

    pub fn set(&mut self, mut i: usize, x: G::T) {
        assert!(i < self.size);
        i += self.n();
        self.data[i] = x;
        while i > 1 {
            i >>= 1;
            self.update(i);
        }
    }

    pub fn get(&self, mut l: usize, mut r: usize) -> G::T {
        assert!(l <= r && r <= self.size);
        let mut vl = self.g.e();
        let mut vr = self.g.e();
        let n = self.n();
        l += n;
        r += n;
        while l < r {
            if l & 1 == 1 {
                vl = self.g.op(vl.clone(), self.data[l].clone());
                l += 1;
            }
            if r & 1 == 1 {
                r -= 1;
                vr = self.g.op(self.data[r].clone(), vr.clone());
            }
            l >>= 1;
            r >>= 1;
        }
        self.g.op(vl, vr)
    }
}
pub fn gcd(a: i64, b: i64) -> i64 { if b == 0 { a } else { gcd(b, a % b) } }
fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: usize = read();
    let q: usize = read();
    let a: Vec<_> = (0..n).map(|_| read::<i64>()).collect();
    let b: Vec<_> = (0..n).map(|_| read::<i64>()).collect();
    let mut da = a.clone();
    let mut db = b.clone();
    for i in 0..n - 1 {
        da[i] = da[i + 1] - da[i];
        db[i] = db[i + 1] - db[i];
    }
    struct G;
    impl Monoid for G {
        type T = i64;

        fn op(&self, x: i64, y: i64) -> i64 { gcd(x, y) }

        fn e(&self) -> i64 { 0 }
    }
    let mut seg_a = SegmentTree::<G>::new(G {}, n);
    let mut seg_b = SegmentTree::<G>::new(G {}, n);
    for i in 0..n - 1 {
        seg_a.set(i, da[i]);
        seg_b.set(i, db[i]);
    }
    for _ in 0..q {
        let h0 = read::<usize>() - 1;
        let h1 = read::<usize>() - 1;
        let w0 = read::<usize>() - 1;
        let w1 = read::<usize>() - 1;
        let mut g = a[h0] + b[w0];
        if h0 < h1 {
            g = gcd(g, seg_a.get(h0, h1));
        }
        if w0 < w1 {
            g = gcd(g, seg_b.get(w0, w1));
        }
        writeln!(writer, "{}", g.abs()).unwrap();
    }
}
