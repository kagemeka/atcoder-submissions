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
pub fn bfs(g: &[Vec<usize>], root: usize) -> (Vec<usize>, Vec<usize>) {
    let n = g.len();
    let mut p = vec![n; n];
    p[root] = root;
    let mut d = vec![0; n];
    let mut que = std::collections::VecDeque::new();
    que.push_back(root);
    while let Some(u) = que.pop_front() {
        for &v in g[u].iter() {
            if v == p[u] {
                continue;
            }
            p[v] = u;
            d[v] = d[u] + 1;
            que.push_back(v);
        }
    }
    (p, d)
}
pub fn argmax<T: PartialOrd + Clone>(a: &[T]) -> usize {
    let (mut idx, mut mx) = (0, &a[0]);
    for (i, x) in a.iter().enumerate() {
        if x > mx {
            idx = i;
            mx = x;
        }
    }
    idx
}
pub fn diameter_path(g: &[Vec<usize>]) -> Vec<usize> {
    let (_, dep) = bfs(&g, 0);
    let (parent, dep) = bfs(&g, argmax(&dep));
    let mut v = argmax(&dep);
    let mut path = vec![v];
    for _ in 0..dep[v] {
        v = parent[v];
        path.push(v);
    }
    path
}
pub fn level_ancestor(
    g: &[Vec<usize>], root: usize, queries: &[(usize, usize)],
) -> Vec<Option<usize>> {
    let n = g.len();
    let mut st = Vec::new();
    let mut res = vec![None; queries.len()];
    let mut q = vec![vec![]; n];
    for (i, &(u, k)) in queries.iter().enumerate() {
        q[u].push((i, k));
    }
    fn dfs(
        g: &[Vec<usize>], q: &[Vec<(usize, usize)>], res: &mut [Option<usize>],
        st: &mut Vec<usize>, u: usize, p: usize,
    ) {
        st.push(u);
        for &(i, k) in q[u].iter() {
            if st.len() <= k {
                continue;
            }
            res[i] = Some(st[st.len() - 1 - k]);
        }
        for &v in g[u].iter() {
            if v == p {
                continue;
            }
            dfs(g, q, res, st, v, u);
        }
        st.pop();
    }
    dfs(g, &q, &mut res, &mut st, root, n);
    res
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
    let q: usize = read();
    let queries: Vec<_> = (0..q)
        .map(|_| (read::<usize>() - 1, read::<usize>()))
        .collect();
    let path = diameter_path(&g);
    let u = path[0];
    let v = *path.last().unwrap();
    let res0 = level_ancestor(&g, u, &queries);
    let res1 = level_ancestor(&g, v, &queries);
    for (u, v) in res0.into_iter().zip(res1.into_iter()) {
        let res = if let Some(u) = u {
            u as isize + 1
        } else if let Some(v) = v {
            v as isize + 1
        } else {
            -1
        };
        writeln!(writer, "{}", res).unwrap();
    }
}
