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
pub fn bfs<F, H>(g: &[Vec<usize>], mut f: F, mut h: H)
where
    F: FnMut(usize, usize),
    H: FnMut(usize),
{
    let n = g.len();
    let mut in_deg = vec![0; n];
    for u in 0..n {
        for &v in g[u].iter() {
            in_deg[v] += 1;
        }
    }
    let mut que = std::collections::VecDeque::new();
    for i in 0..n {
        if in_deg[i] == 0 {
            que.push_back(i);
        }
    }
    while let Some(u) = que.pop_front() {
        h(u);
        for &v in g[u].iter() {
            f(u, v);
            in_deg[v] -= 1;
            if in_deg[v] == 0 {
                que.push_back(v);
            }
        }
    }
}
pub fn transpose(g: &[Vec<usize>]) -> Vec<Vec<usize>> {
    let n = g.len();
    let mut t = vec![vec![]; n];
    for u in 0..n {
        for &v in g[u].iter() {
            t[v].push(u);
        }
    }
    t
}
fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: usize = read();
    let m: usize = read();
    let mut cnt = n;
    let mut f = |_, _| {};
    let mut h = |_| {
        cnt -= 1;
    };
    let mut g = vec![vec![]; n];
    for _ in 0..m {
        let u = read::<usize>() - 1;
        let v = read::<usize>() - 1;
        g[u].push(v);
    }
    g = transpose(&g);
    bfs(&g, &mut f, &mut h);
    writeln!(writer, "{}", cnt).unwrap();
}
