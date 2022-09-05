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
pub fn dfs_tree(g: &[Vec<usize>], root: usize) -> Vec<(usize, usize)> {
    let n = g.len();
    let mut visited = vec![false; n];
    let mut used = Vec::with_capacity(n - 1);
    fn dfs(
        g: &[Vec<usize>], visited: &mut [bool], used: &mut Vec<(usize, usize)>,
        u: usize,
    ) {
        visited[u] = true;
        for &v in g[u].iter() {
            if visited[v] {
                continue;
            }
            used.push(if u < v { (u, v) } else { (v, u) });
            dfs(g, visited, used, v);
        }
    }
    dfs(g, &mut visited, &mut used, root);
    used
}
pub fn bfs_tree(g: &[Vec<usize>], root: usize) -> Vec<(usize, usize)> {
    let n = g.len();
    let mut used = Vec::with_capacity(n - 1);
    let mut que = std::collections::VecDeque::new();
    que.push_back(root);
    let mut to_que = vec![false; n];
    to_que[root] = true;
    while let Some(u) = que.pop_front() {
        for &v in g[u].iter() {
            if to_que[v] {
                continue;
            }
            que.push_back(v);
            to_que[v] = true;
            used.push(if u < v { (u, v) } else { (v, u) });
        }
    }
    used
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: usize = read();
    let m: usize = read();
    let mut g = vec![vec![]; n];
    for _ in 0..m {
        let u = read::<usize>() - 1;
        let v = read::<usize>() - 1;
        g[u].push(v);
        g[v].push(u);
    }
    for (u, v) in dfs_tree(&g, 0).into_iter() {
        writeln!(writer, "{} {}", u + 1, v + 1).unwrap();
    }
    for (u, v) in bfs_tree(&g, 0).into_iter() {
        writeln!(writer, "{} {}", u + 1, v + 1).unwrap();
    }
}
