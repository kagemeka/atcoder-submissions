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
pub trait Edge {
    fn to(&self) -> usize;
}
pub struct ReRootingDP<'a, M: Monoid, E, F> {
    g: &'a [Vec<E>],
    m: M,
    f: F,
    rev_edge: Vec<Option<&'a E>>,
    dp_from_childs: Vec<M::T>,
    dp: Vec<M::T>,
}
impl<'a, M: Monoid, E, F: Fn(&E, M::T) -> M::T> ReRootingDP<'a, M, E, F>
where
    M::T: Clone + std::fmt::Debug,
    E: Clone + Edge,
{
    fn new(g: &'a [Vec<E>], m: M, f: F) -> Self {
        let n = g.len();
        let dp_from_childs = vec![m.e(); n];
        let dp = vec![m.e(); n];
        let rev_edge = vec![None; n];
        Self { g, m, f, rev_edge, dp_from_childs, dp }
    }

    pub fn calc(g: &'a [Vec<E>], m: M, f: F) -> Vec<M::T> {
        let mut wrapper = Self::new(g, m, f);
        wrapper.tree_dp(0, 0);
        wrapper.reroot(0, 0, wrapper.m.e());
        wrapper.dp
    }

    fn tree_dp(&mut self, u: usize, parent: usize) {
        for e in self.g[u].iter() {
            let v = e.to();
            if v == parent {
                self.rev_edge[u] = Some(e);
                continue;
            }
            self.tree_dp(v, u);
            self.dp_from_childs[u] = self.m.op(
                self.dp_from_childs[u].clone(),
                (self.f)(&e, self.dp_from_childs[v].clone()),
            );
        }
    }

    fn reroot(&mut self, u: usize, parent: usize, x: M::T) {
        self.dp[u] = self.m.op(x.clone(), self.dp_from_childs[u].clone());
        let n = self.g[u].len();
        let mut dp_r = vec![self.m.e(); n + 1];
        for (i, e) in self.g[u].iter().enumerate().rev() {
            let v = e.to();
            dp_r[i] = if v == parent {
                dp_r[i + 1].clone()
            } else {
                self.m.op(
                    (self.f)(e, self.dp_from_childs[v].clone()),
                    dp_r[i + 1].clone(),
                )
            };
        }
        let mut dp_l = self.m.e();
        for (i, e) in self.g[u].iter().enumerate() {
            let v = e.to();
            if v == parent {
                continue;
            }
            let y = (self.f)(
                self.rev_edge[v].unwrap(),
                self.m.op(
                    x.clone(),
                    self.m.op(dp_l.clone(), dp_r[i + 1].clone()),
                ),
            );
            dp_l = self.m.op(dp_l, (self.f)(e, self.dp_from_childs[v].clone()));
            self.reroot(v, u, y);
        }
    }
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: usize = read();
    let mut g = vec![vec![]; n];
    for _ in 0..n - 1 {
        let u = read::<usize>() - 1;
        let v = read::<usize>() - 1;
        g[u].push(v);
        g[v].push(u);
    }
    struct M;
    impl Monoid for M {
        type T = (usize, usize);

        fn e(&self) -> Self::T { (0, 0) }

        fn op(&self, l: Self::T, r: Self::T) -> Self::T {
            (l.0 + r.0, l.1 + r.1)
        }
    }
    impl Edge for usize {
        fn to(&self) -> usize { *self }
    }
    let res = ReRootingDP::calc(&g, M {}, |_, x: (usize, usize)| {
        (x.0 + x.1 + 1, x.1 + 1)
    });
    for &x in res.iter() {
        writeln!(writer, "{}", x.0).unwrap();
    }
}
