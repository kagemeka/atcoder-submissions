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
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    struct M;
    impl Monoid for M {
        type T = (i64, i64);

        fn e(&self) -> Self::T { (std::i64::MAX, 0) }

        fn op(&self, l: Self::T, r: Self::T) -> Self::T {
            (l.0.min(l.1 + r.0), l.1 + r.1)
        }
    }
    let m = M {};
    let n: usize = read();
    let q: usize = read();
    let s: String = read();
    let s: Vec<_> = s.chars().collect();
    let mut a = vec![0; n];
    for i in 0..n {
        a[i] = if s[i] == '(' { 1 } else { -1 };
    }
    let mut seg = SegmentTree::new(m, n);
    for i in 0..n {
        seg.set(i, (a[i], a[i]));
    }
    for _ in 0..q {
        let t: usize = read();
        let l = read::<usize>() - 1;
        let r = read::<usize>() - 1;
        if t == 1 {
            a.swap(l, r);
            seg.set(l, (a[l], a[l]));
            seg.set(r, (a[r], a[r]));
        } else {
            let s = seg.get(l, r + 1);
            writeln!(
                writer,
                "{}",
                if s.0 >= 0 && s.1 == 0 { "Yes" } else { "No" }
            )
            .unwrap();
        }
    }
}
