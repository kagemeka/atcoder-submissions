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
pub fn rerooting_dp<M, E, F>(g: &[Vec<E>], m: M, f: F) -> Vec<M::T>
where
    M: Monoid,
    M::T: Clone,
    E: Clone + Edge,
    F: Fn(&E, M::T) -> M::T,
{
    let n = g.len();
    let mut dp_from_childs = vec![m.e(); n];
    let mut dp = vec![m.e(); n];
    let mut parent = vec![n; n];
    let mut st = vec![0isize];
    let mut rev_edge = vec![None; n];
    while let Some(u) = st.pop() {
        if u < 0 {
            let u = !u as usize;
            for e in g[u].iter() {
                let v = e.to();
                if v == parent[u] {
                    continue;
                }
                dp_from_childs[u] = m.op(
                    dp_from_childs[u].clone(),
                    f(e, dp_from_childs[v].clone()),
                );
            }
            continue;
        }
        st.push(!u);
        let u = u as usize;
        for e in g[u].iter() {
            let v = e.to();
            if v == parent[u] {
                rev_edge[u] = Some(e);
                continue;
            }
            parent[v] = u;
            st.push(v as isize)
        }
    }
    let mut st = vec![(0, m.e())];
    while let Some((u, x)) = st.pop() {
        dp[u] = m.op(x.clone(), dp_from_childs[u].clone());
        let n = g[u].len();
        let mut dp_r = vec![m.e(); n + 1];
        for (i, e) in g[u].iter().enumerate().rev() {
            let v = e.to();
            dp_r[i] = if v == parent[u] {
                dp_r[i + 1].clone()
            } else {
                m.op(f(e, dp_from_childs[v].clone()), dp_r[i + 1].clone())
            };
        }
        let mut dp_l = m.e();
        for (i, e) in g[u].iter().enumerate() {
            let v = e.to();
            if v == parent[u] {
                continue;
            }
            let y = f(
                rev_edge[v].unwrap(),
                m.op(x.clone(), m.op(dp_l.clone(), dp_r[i + 1].clone())),
            );
            st.push((v, y));
            dp_l = m.op(dp_l, f(e, dp_from_childs[v].clone()));
        }
    }
    dp
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
    let res =
        rerooting_dp(&g, M {}, |_, x: (usize, usize)| (x.0 + x.1 + 1, x.1 + 1));
    for &x in res.iter() {
        writeln!(writer, "{}", x.0).unwrap();
    }
}
