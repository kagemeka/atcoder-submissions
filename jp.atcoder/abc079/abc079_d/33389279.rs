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
pub fn dijkstra_dense(inf: i64, g: &[Vec<i64>], src: usize) -> Vec<i64> {
    let n = g.len();
    let mut dist = vec![inf; n];
    dist[src] = 0;
    let mut visited = vec![false; n];
    loop {
        let mut u = n;
        let mut du = inf;
        for i in 0..n {
            if visited[i] || dist[i] >= du {
                continue;
            }
            u = i;
            du = dist[i];
        }
        if u == n {
            break;
        }
        visited[u] = true;
        for v in 0..n {
            if g[u][v] == inf {
                continue;
            }
            dist[v] = dist[v].min(du + g[u][v]);
        }
    }
    dist
}
pub fn floyd_warshall(mut g: Vec<Vec<u64>>) -> Vec<Vec<u64>> {
    let n = g.len();
    for k in 0..n {
        for i in 0..n {
            for j in 0..n {
                g[i][j] = g[i][j].min(g[i][k] + g[k][j]);
            }
        }
    }
    g
}
fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let h: usize = read();
    let w: usize = read();
    const K: usize = 10;
    const INF: u64 = 1 << 29;
    let mut g = vec![vec![INF; K]; K];
    for i in 0..K {
        for j in 0..K {
            g[i][j] = read();
        }
    }
    let mut s = 0;
    g = floyd_warshall(g);
    for _ in 0..h * w {
        let a: isize = read();
        if a == -1 {
            continue;
        }
        s += g[a as usize][1];
    }
    writeln!(writer, "{}", s).unwrap();
}
