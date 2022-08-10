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
pub fn bellman_ford(
    inf: i64, v_size: usize, edges: &[(usize, usize, i64)], src: usize,
) -> Vec<i64> {
    let mut dist = vec![inf; v_size];
    dist[src] = 0;
    for t in 1..v_size << 1 {
        for &(u, v, w) in edges {
            if dist[u] == inf {
                continue;
            }
            let dv = if dist[u] == -inf { -inf } else { dist[u] + w };
            if dv >= dist[v] {
                continue;
            }
            dist[v] = if t >= v_size { -inf } else { dv };
        }
    }
    dist
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: usize = read();
    let m: usize = read();
    let p: i64 = read();
    let edges: Vec<_> = (0..m)
        .map(|_| {
            let a = read::<usize>() - 1;
            let b = read::<usize>() - 1;
            let w: i64 = read();
            (a, b, p - w)
        })
        .collect();
    let inf = 1 << 60;
    let dist = bellman_ford(inf, n, &edges, 0);
    let res = if dist[n - 1] != -inf { -dist[n - 1].min(0) } else { -1 };
    writeln!(writer, "{}", res).unwrap();
}
