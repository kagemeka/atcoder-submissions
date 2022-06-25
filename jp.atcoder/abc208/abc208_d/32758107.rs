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

type G<T> = Vec<Vec<T>>;

pub fn floyd_warshall<T, F, H>(adj_mat: G<T>, f: &F, cb: &mut H) -> G<T>
where
    T: Clone,
    F: Fn(T, T, T) -> T,
    H: FnMut(usize, &G<T>),
{
    let mut g = adj_mat;
    let n = g.len();
    for k in 0..n {
        for i in 0..n {
            for j in 0..n {
                g[i][j] = f(
                    g[i][j].clone(),
                    g[i][k].clone(),
                    g[k][j].clone(),
                );
            }
        }
        cb(k, &g);
    }
    g
}

fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());

    let n: usize = read();
    let m: usize = read();

    const INF: u64 = 1 << 60;
    let mut g = vec![vec![INF; n]; n];
    for i in 0..n {
        g[i][i] = 0;
    }
    for _ in 0..m {
        let a: usize = read::<usize>() - 1;
        let b: usize = read::<usize>() - 1;
        let c: u64 = read();
        g[a][b] = c;
    }

    let mut sum = 0;
    let mut f = |_, g: &G<u64>| {
        for i in 0..n {
            for j in 0..n {
                sum += if g[i][j] == INF { 0 } else { g[i][j] };
            }
        }
    };
    floyd_warshall(
        g,
        &|x, y, z| x.min(y + z),
        &mut f,
    );
    writeln!(writer, "{}", sum).unwrap();
}
