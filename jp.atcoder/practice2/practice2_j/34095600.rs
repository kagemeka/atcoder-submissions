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
    fn op(&self, l: Self::T, r: Self::T) -> Self::T;
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
    fn merge(&mut self, i: usize) {
        self.data[i] = self
            .g
            .op(self.data[i << 1].clone(), self.data[i << 1 | 1].clone());
    }

    pub fn new(g: G, size: usize) -> Self {
        assert!(size > 0);
        let n = size.next_power_of_two();
        let data = vec![g.e(); n << 1];
        Self { g, size, data }
    }

    pub fn set(&mut self, mut i: usize, x: G::T) {
        assert!(i < self.size);
        i += self.n();
        self.data[i] = x;
        while i > 1 {
            i >>= 1;
            self.merge(i);
        }
    }

    pub fn fold(&self, mut l: usize, mut r: usize) -> G::T {
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

    pub fn max_right<F: Fn(&G::T) -> bool>(&self, f: F, l: usize) -> usize {
        assert!(l <= self.size);
        if l == self.size {
            return self.size;
        }
        let mut v = self.g.e();
        let n = self.n();
        let mut i = l + n;
        loop {
            i >>= i.trailing_zeros();
            let nv = self.g.op(v.clone(), self.data[i].clone());
            if !f(&nv) {
                break;
            }
            v = nv;
            i += 1;
            if i.count_ones() == 1 {
                return self.size;
            }
        }
        while i < n {
            i <<= 1;
            let nv = self.g.op(v.clone(), self.data[i].clone());
            if !f(&nv) {
                continue;
            }
            v = nv;
            i += 1;
        }
        i - n
    }

    pub fn min_left<F: Fn(&G::T) -> bool>(&self, f: F, r: usize) -> usize {
        assert!(r <= self.size);
        if r == 0 {
            return 0;
        }
        let mut v = self.g.e();
        let n = self.n();
        let mut i = r + n;
        loop {
            i >>= i.trailing_zeros();
            let nv = self.g.op(self.data[i - 1].clone(), v.clone());
            if !f(&nv) {
                break;
            }
            i -= 1;
            v = nv;
            if i.count_ones() == 1 {
                return 0;
            }
        }
        while i < n {
            i <<= 1;
            let nv = self.g.op(self.data[i - 1].clone(), v.clone());
            if !f(&nv) {
                continue;
            }
            i -= 1;
            v = nv;
        }
        i - n
    }
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: usize = read();
    let q: usize = read();
    let a: Vec<_> = (0..n).map(|_| read::<i32>()).collect();
    pub struct RangeMinimum<T>(T);
    impl<T> RangeMinimum<T> {
        pub fn new(inf: T) -> Self { Self(inf) }
    }
    impl<T: Ord + Clone> Monoid for RangeMinimum<T> {
        type T = T;

        fn e(&self) -> Self::T { self.0.clone() }

        fn op(&self, l: Self::T, r: Self::T) -> Self::T { l.min(r) }
    }
    let mut seg = SegmentTree::new(RangeMinimum::new(1 << 30), n);
    for i in 0..n {
        seg.set(i, -a[i]);
    }
    for _ in 0..q {
        let t: usize = read();
        let x: i32 = read();
        let y: i32 = read();
        if t == 1 {
            seg.set(x as usize - 1, -y);
        } else if t == 2 {
            writeln!(writer, "{}", -seg.fold(x as usize - 1, y as usize))
                .unwrap();
        } else {
            writeln!(
                writer,
                "{}",
                seg.max_right(|v| v > &-y, x as usize - 1) + 1
            )
            .unwrap();
        }
    }
}
