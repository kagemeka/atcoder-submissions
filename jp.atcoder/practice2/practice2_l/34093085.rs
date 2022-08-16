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

    pub fn set(&mut self, i: usize, x: O::S) {
        assert!(i < self.size());
        self._set(i, 0, self.n(), 1, x);
    }

    fn _set(&mut self, i: usize, cl: usize, cr: usize, ci: usize, x: O::S) {
        assert!(cl <= i && i < cr);
        if cr - cl == 1 {
            self.data[ci] = x;
            return;
        }
        self.propagate(ci);
        let c = (cl + cr) >> 1;
        if i < c {
            self._set(i, cl, c, ci << 1, x);
        } else {
            self._set(i, c, cr, ci << 1 | 1, x);
        }
        self.merge(ci);
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

    pub fn get(&mut self, i: usize) -> O::S { self.fold(i, i + 1) }

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
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: usize = read();
    let q: usize = read();
    struct O;
    impl Ops for O {
        type F = i64;
        type S = (i64, i64, i64);

        // 0, 1, inversion
        fn compose(&self, f: Self::F, g: Self::F) -> Self::F { f ^ g }

        fn id(&self) -> Self::F { 0 }

        fn e(&self) -> Self::S { (0, 0, 0) }

        fn map(&self, f: Self::F, x: Self::S) -> Self::S {
            if f == 0 { x } else { (x.1, x.0, x.0 * x.1 - x.2) }
        }

        fn op(&self, a: Self::S, b: Self::S) -> Self::S {
            (a.0 + b.0, a.1 + b.1, a.2 + b.2 + a.1 * b.0)
        }
    }
    let a: Vec<_> = (0..n).map(|_| read::<i64>()).collect();
    let mut seg = LazySegtree::new(O {}, n);
    for i in 0..n {
        seg.set(i, if a[i] == 0 { (1, 0, 0) } else { (0, 1, 0) });
    }
    for _ in 0..q {
        let t: usize = read();
        let l: usize = read::<usize>() - 1;
        let r: usize = read::<usize>() - 1;
        if t == 1 {
            seg.apply(l, r + 1, 1);
        } else {
            writeln!(writer, "{}", seg.fold(l, r + 1).2).unwrap();
        }
    }
}
