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
pub fn doubling_table(f: &[usize], n_bits: usize) -> Vec<Vec<usize>> {
    assert!(n_bits > 0);
    let n = f.len();
    let mut a = Vec::with_capacity(n_bits);
    a.push(f.to_owned());
    for i in 0..n_bits - 1 {
        let row = &a[i];
        a.push((0..n).map(|j| row[row[j]]).collect());
    }
    a
}
pub struct LevelAncestor {
    ancestor: Vec<Vec<usize>>,
    pub depth: Vec<usize>,
}
impl LevelAncestor {
    pub fn new(g: &[Vec<usize>], root: usize) -> Self {
        let (parent, depth) = bfs(g, root);
        let k = depth
            .iter()
            .max()
            .unwrap()
            .next_power_of_two()
            .trailing_zeros() as usize;
        let ancestor = doubling_table(&parent, k + 1);
        Self { ancestor, depth }
    }

    pub fn get(&self, mut u: usize, mut k: usize) -> usize {
        assert!(k <= self.depth[u]);
        for (i, a) in self.ancestor.iter().enumerate() {
            if k >> i & 1 == 0 {
                continue;
            }
            k ^= 1 << i;
            u = a[u];
        }
        debug_assert!(k == 0);
        u
    }
}
pub fn read_graph(
    n: usize, m: usize, offset: usize, directed: bool,
) -> Vec<Vec<usize>> {
    graph_from_edges(n, &read_edges(m, offset), directed)
}
pub fn read_edges(m: usize, offset: usize) -> Vec<(usize, usize)> {
    (0..m)
        .map(|_| (read::<usize>() - offset, read::<usize>() - offset))
        .collect()
}
pub fn graph_from_edges(
    n: usize, edges: &[(usize, usize)], directed: bool,
) -> Vec<Vec<usize>> {
    let mut g = vec![vec![]; n];
    for &(u, v) in edges {
        g[u].push(v);
        if !directed {
            g[v].push(u);
        }
    }
    g
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: usize = read();
    let g = read_graph(n, n - 1, 1, false);
    let q: usize = read();
    let queries: Vec<_> = (0..q)
        .map(|_| (read::<usize>() - 1, read::<usize>()))
        .collect();
    let path = diameter_path(&g);
    let u = path[0];
    let v = *path.last().unwrap();
    let la_u = LevelAncestor::new(&g, u);
    let la_v = LevelAncestor::new(&g, v);
    for (u, k) in queries.into_iter() {
        let res = if k <= la_u.depth[u] {
            la_u.get(u, k) as isize + 1
        } else if k <= la_v.depth[u] {
            la_v.get(u, k) as isize + 1
        } else {
            -1
        };
        writeln!(writer, "{}", res).unwrap();
    }
}
