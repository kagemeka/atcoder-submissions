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
use std::ops::*;
type G<T> = Vec<Vec<T>>;
pub fn floyd_warshall<T, F>(adj_mat: G<T>, mut f: F) -> G<T>
where
    T: Clone,
    F: FnMut(T, T, T) -> T,
{
    let mut g = adj_mat;
    let n = g[0].len();
    for k in 0..n {
        for i in 0..n {
            for j in 0..n {
                g[i][j] = f(g[i][j].clone(), g[i][k].clone(), g[k][j].clone());
            }
        }
    }
    g
}
fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: usize = read();
    let m: usize = read();
    const INF: u32 = 1 << 30;
    let mut g: Vec<Vec<u32>> = vec![vec![INF; n]; n];
    for _ in 0..m {
        let a: usize = read();
        let b: usize = read();
        let c: u32 = read();
        g[a - 1][b - 1] = c;
    }
    for i in 0..n {
        g[i][i] = 0;
    }
    let mut tot: u64 = 0;
    let f = &mut |x: u32, y, z| {
        let res = x.min(y + z);
        if res != INF {
            tot += res as u64;
        }
        return res;
    };
    floyd_warshall(g, f);
    writeln!(writer, "{}", tot).unwrap();
}
