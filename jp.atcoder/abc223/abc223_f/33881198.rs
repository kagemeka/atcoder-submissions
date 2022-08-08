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
pub fn bit_length(n: usize) -> usize {
    (0usize.leading_zeros() - n.leading_zeros()) as usize
}
pub trait Ops {
    type S;
    type F;
    fn op(&self, a: Self::S, b: Self::S) -> Self::S;
    fn e(&self) -> Self::S;
    fn compose(&self, f: Self::F, g: Self::F) -> Self::F;
    fn id(&self) -> Self::F;
    fn map(&self, f: Self::F, x: Self::S) -> Self::S;
}
#[derive(Debug)]
pub struct LazySegtree<O: Ops> {
    ops: O,
    data: Vec<O::S>,
    lazy: Vec<O::F>,
    size: usize,
}
impl<O: Ops> LazySegtree<O>
where
    O::S: Clone,
    O::F: Clone,
{
    pub fn new(ops: O, size: usize) -> Self {
        assert!(size > 0);
        let n = size.next_power_of_two();
        let data = vec![ops.e(); n << 1];
        let lazy = vec![ops.id(); n];
        Self { ops, data, lazy, size }
    }

    pub fn size(&self) -> usize { self.size }

    fn n(&self) -> usize { self.lazy.len() }

    fn height(&self) -> usize { bit_length(self.n()) }

    fn merge(&mut self, i: usize) {
        self.data[i] = self
            .ops
            .op(self.data[i << 1].clone(), self.data[i << 1 | 1].clone());
    }

    fn apply_node(&mut self, i: usize, f: O::F) {
        self.data[i] = self.ops.map(f.clone(), self.data[i].clone());
        if i < self.n() {
            self.lazy[i] = self.ops.compose(f, self.lazy[i].clone());
        }
    }

    fn propagate(&mut self, i: usize) {
        let f = self.lazy[i].clone();
        self.apply_node(i << 1, f.clone());
        self.apply_node(i << 1 | 1, f);
        self.lazy[i] = self.ops.id();
    }

    fn pull(&mut self, i: usize) {
        for j in (1..self.height()).rev() {
            self.propagate(i >> j);
        }
    }

    fn merge_above(&mut self, mut i: usize) {
        while i > 1 {
            i >>= 1;
            self.merge(i);
        }
    }

    pub fn apply(&mut self, l: usize, r: usize, f: O::F) {
        assert!(l <= r && r <= self.size);
        self._apply(l, r, 0, self.n(), 1, f);
    }

    fn _apply(
        &mut self, l: usize, r: usize, cl: usize, cr: usize, i: usize, f: O::F,
    ) {
        if cr <= l || r <= cl {
            return;
        }
        if l <= cl && cr <= r {
            self.apply_node(i, f);
            return;
        }
        self.propagate(i);
        let c = (cl + cr) >> 1;
        self._apply(l, r, cl, c, i << 1, f.clone());
        self._apply(l, r, c, cr, i << 1 | 1, f);
        self.merge(i);
    }

    pub fn set(&mut self, mut i: usize, x: O::S) {
        assert!(i < self.size);
        i += self.n();
        self.pull(i);
        self.data[i] = x;
        self.merge_above(i);
    }

    pub fn get(&mut self, mut i: usize) -> O::S {
        assert!(i < self.size);
        i += self.n();
        self.pull(i);
        self.data[i].clone()
    }

    pub fn fold(&mut self, l: usize, r: usize) -> O::S {
        assert!(l <= r && r <= self.size);
        self._fold(l, r, 0, self.n(), 1)
    }

    fn _fold(
        &mut self, l: usize, r: usize, cl: usize, cr: usize, i: usize,
    ) -> O::S {
        if cr <= l || r <= cl {
            return self.ops.e();
        }
        if l <= cl && cr <= r {
            return self.data[i].clone();
        }
        self.propagate(i);
        let c = (cl + cr) >> 1;
        let vl = self._fold(l, r, cl, c, i << 1);
        let vr = self._fold(l, r, c, cr, i << 1 | 1);
        self.ops.op(vl, vr)
    }
}
use std::ops::*;
pub struct RangeAddRangeMinimum<T>(T, T);
impl<T> RangeAddRangeMinimum<T> {
    pub fn new(inf: T, zero: T) -> Self { Self(inf, zero) }
}
impl<T> Ops for RangeAddRangeMinimum<T>
where
    T: Ord + Clone + Add<Output = T>,
{
    type F = T;
    type S = T;

    fn op(&self, a: Self::S, b: Self::S) -> Self::S { a.min(b) }

    fn e(&self) -> Self::S { self.0.clone() }

    fn compose(&self, f: Self::F, g: Self::F) -> Self::F { f + g }

    fn id(&self) -> Self::F { self.1.clone() }

    fn map(&self, f: Self::F, x: Self::S) -> Self::S {
        if x == self.e() { x } else { f + x }
    }
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: usize = read();
    let q: usize = read();
    let s: String = read();
    let s: Vec<_> = s.chars().collect();
    let mut a = vec![0; n];
    for i in 0..n {
        a[i] = if s[i] == '(' { 1 } else { -1 };
    }
    let ops = RangeAddRangeMinimum::<i64>::new(std::i64::MAX, 0);
    let mut seg = LazySegtree::new(ops, n);
    for i in 0..n {
        seg.set(i, 0);
    }
    for i in 0..n {
        seg.apply(i, n, a[i]);
    }
    for _ in 0..q {
        let t: usize = read();
        let l = read::<usize>() - 1;
        let r = read::<usize>() - 1;
        if t == 1 {
            seg.apply(l, n, -a[l]);
            seg.apply(r, n, -a[r]);
            a.swap(l, r);
            seg.apply(l, n, a[l]);
            seg.apply(r, n, a[r]);
        } else {
            let s = seg.fold(l, r + 1);
            let b = if l == 0 { 0 } else { seg.get(l - 1) };
            let ok = s >= b && seg.get(r) == b;
            writeln!(writer, "{}", if ok { "Yes" } else { "No" }).unwrap();
        }
    }
}
