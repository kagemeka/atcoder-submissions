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
pub struct Fenwick<G: Monoid> {
    pub(crate) g: G,
    pub(crate) node: Vec<G::T>,
}
impl<G: Monoid> Fenwick<G>
where
    G::T: Clone,
{
    pub fn new(g: G, size: usize) -> Self {
        let node = vec![g.e(); size + 1];
        Self { g, node }
    }

    pub fn size(&self) -> usize { self.node.len() - 1 }

    pub fn operate(&mut self, mut i: usize, x: G::T) {
        let n = self.size();
        assert!(i < n);
        i += 1;
        while i <= n {
            self.node[i] = self.g.op(self.node[i].clone(), x.clone());
            i += 1 << i.trailing_zeros();
        }
    }

    pub fn fold_lt(&self, mut i: usize) -> G::T {
        assert!(i <= self.size());
        let mut v = self.g.e();
        while i > 0 {
            v = self.g.op(v, self.node[i].clone());
            i -= 1 << i.trailing_zeros();
        }
        v
    }
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: usize = read();
    let q: usize = read();
    let a: Vec<_> = (0..n).map(|_| read::<usize>()).collect();
    struct M;
    impl Monoid for M {
        type T = usize;

        fn op(&self, l: usize, r: usize) -> usize { l + r }

        fn e(&self) -> usize { 0 }
    }
    let mut fw = Fenwick::new(M {}, n);
    for i in 0..n {
        fw.operate(i, a[i]);
    }
    for _ in 0..q {
        let t: usize = read();
        let x: usize = read();
        let y: usize = read();
        if t == 0 {
            fw.operate(x, y);
        } else {
            writeln!(writer, "{}", fw.fold_lt(y) - fw.fold_lt(x)).unwrap();
        }
    }
}
