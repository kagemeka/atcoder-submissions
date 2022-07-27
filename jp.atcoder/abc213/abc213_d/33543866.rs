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
fn main() {
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
    for i in 0..n {
        g[i].sort();
    }
    let tour = euler_tour_nodes(&g, 0);
    let m = tour.len();
    for i in 0..m {
        write!(
            writer,
            "{}{}",
            tour[i] + 1,
            if i == m - 1 { '\n' } else { ' ' }
        )
        .unwrap();
    }
}
