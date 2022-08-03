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
pub fn add_middle_nodes(edges: &[(usize, usize)]) -> Vec<(usize, usize)> {
    let n = edges.len() + 1;
    let mut new_edges = Vec::with_capacity((n - 1) << 1);
    for i in 0..n - 1 {
        let (u, v) = edges[i];
        new_edges.push((u, n + i));
        new_edges.push((v, n + i));
    }
    new_edges
}
pub fn diameter_path(g: &[Vec<usize>]) -> Vec<usize> {
    let n = g.len();
    let argmax = |dep: &[usize], root| {
        let mut v = root;
        let mut mx = 0;
        for i in 0..n {
            if dep[i] <= mx {
                continue;
            }
            mx = dep[i];
            v = i;
        }
        v
    };
    let (_, dep) = bfs(&g, 0);
    let u = argmax(&dep, 0);
    let (parent, dep) = bfs(&g, u);
    let mut v = argmax(&dep, u);
    let mut path = vec![v];
    for _ in 0..dep[v] {
        v = parent[v];
        path.push(v);
    }
    path
}
pub fn euler_tour_nodes(g: &[Vec<usize>], root: usize) -> Vec<usize> {
    let n = g.len();
    let mut tour = Vec::with_capacity(2 * n - 1);
    fn dfs(g: &[Vec<usize>], tour: &mut Vec<usize>, u: usize, p: usize) {
        tour.push(u);
        for &v in g[u].iter() {
            if v == p {
                continue;
            }
            dfs(g, tour, v, u);
            tour.push(u);
        }
    }
    dfs(g, &mut tour, root, n);
    tour
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: usize = read();
    let edges: Vec<_> = (0..n - 1)
        .map(|_| (read::<usize>() - 1, read::<usize>() - 1))
        .collect();
    let edges = add_middle_nodes(&edges);
    let n = edges.len() + 1;
    let mut g = vec![vec![]; n];
    for &(u, v) in edges.iter() {
        g[u].push(v);
        g[v].push(u);
    }
    let path = diameter_path(&g);
    let d = path.len() - 1;
    assert!(d & 1 == 0);
    let r = d >> 1;
    let c = path[r];
    let (_, dep) = bfs(&g, c);
    const MOD: i64 = 998_244_353;
    let tour = euler_tour_nodes(&g, c);
    let mut cnt = 0;
    let mut s = 1;
    let mut neg = 0;
    for &u in tour.iter() {
        if u != c {
            if dep[u] == r {
                cnt += 1;
            }
            continue;
        }
        s *= cnt + 1;
        s %= MOD;
        neg += cnt;
        cnt = 0;
    }
    s -= neg + 1;
    s %= MOD;
    s += MOD;
    s %= MOD;
    writeln!(writer, "{}", s).unwrap();
}
