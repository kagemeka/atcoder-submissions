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
pub mod rerooting_dp_as_struct {
    pub trait Monoid {
        type T;
        fn op(&self, _: Self::T, _: Self::T) -> Self::T;
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
        dp_from_parent: Vec<M::T>,
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
            let dp_from_parent = vec![m.e(); n];
            let dp = vec![m.e(); n];
            let rev_edge = vec![None; n];
            Self { g, m, f, rev_edge, dp_from_childs, dp_from_parent, dp }
        }

        pub fn calc(g: &'a [Vec<E>], m: M, f: F) -> Vec<M::T> {
            let mut wrapper = Self::new(g, m, f);
            wrapper.tree_dp(0, 0);
            wrapper.reroot(0, 0);
            wrapper.merge_parent_and_childs();
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

        fn reroot(&mut self, u: usize, parent: usize) {
            let mut childs = vec![];
            for e in self.g[u].iter() {
                if e.to() != parent {
                    childs.push(e.clone());
                }
            }
            let n = childs.len();
            let mut dp_l = vec![self.m.e(); n + 1];
            let mut dp_r = vec![self.m.e(); n + 1];
            for (i, e) in childs.iter().enumerate() {
                dp_l[i + 1] = self.m.op(
                    dp_l[i].clone(),
                    (self.f)(&e, self.dp_from_childs[e.to()].clone()),
                );
            }
            for (i, e) in childs.iter().enumerate().rev() {
                dp_r[i] = self.m.op(
                    (self.f)(&e, self.dp_from_childs[e.to()].clone()),
                    dp_r[i + 1].clone(),
                );
            }
            for (i, e) in childs.iter().enumerate() {
                self.dp_from_parent[e.to()] = (self.f)(
                    self.rev_edge[e.to()].unwrap(),
                    self.m.op(
                        self.dp_from_parent[u].clone(),
                        self.m.op(dp_l[i].clone(), dp_r[i + 1].clone()),
                    ),
                );
                self.reroot(e.to(), u)
            }
        }

        fn merge_parent_and_childs(&mut self) {
            for i in 0..self.g.len() {
                self.dp[i] = self.m.op(
                    self.dp_from_childs[i].clone(),
                    self.dp_from_parent[i].clone(),
                );
            }
        }
    }
}
fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: usize = read();
    struct M;
    use rerooting_dp_as_struct::*;
    impl Monoid for M {
        type T = u64;

        fn op(&self, lhs: Self::T, rhs: Self::T) -> Self::T { lhs.max(rhs) }

        fn e(&self) -> Self::T { 0 }
    }
    #[derive(Clone)]
    struct E {
        to: usize,
        weight: u64,
    }
    impl E {
        pub fn new(to: usize, weight: u64) -> Self { Self { to, weight } }
    }
    impl Edge for E {
        fn to(&self) -> usize { self.to }
    }
    let mut g = vec![vec![]; n];
    for _ in 0..n - 1 {
        let u = read::<usize>() - 1;
        let v = read::<usize>() - 1;
        let w = read::<u64>();
        g[u].push(E::new(v, w));
        g[v].push(E::new(u, w));
    }
    let d: Vec<u64> = (0..n).map(|_| read()).collect();
    let map = |e: &E, x: u64| -> u64 { e.weight + x.max(d[e.to()]) };
    let res = ReRootingDP::calc(&g, M {}, &map);
    for &x in res.iter() {
        writeln!(writer, "{}", x).unwrap();
    }
}
