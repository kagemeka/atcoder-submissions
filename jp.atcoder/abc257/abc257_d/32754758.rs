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

pub fn floyd_warshall<T, F, H>(adj_mat: G<T>, f: &F, cb: &H) -> G<T>
where
    T: Clone,
    F: Fn(T, T, T) -> T,
    H: Fn(usize, &G<T>),
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

    let a: Vec<(i64, i64, i64)> = (0..n)
        .map(|_| {
            let x: i64 = read();
            let y: i64 = read();
            let p: i64 = read();
            (x, y, p)
        })
        .collect();

    let mut g: Vec<Vec<i64>> = vec![vec![0; n]; n];
    for i in 0..n {
        let (xi, yi, pi) = a[i];
        for j in 0..n {
            let (xj, yj, pj) = a[j];
            let mut d = (xi - xj).abs() + (yi - yj).abs();
            d = (d + pi - 1) / pi;
            g[i][j] = d;
        }
    }

    let min_w = floyd_warshall(
        g,
        &|x, y, z| x.min(y.max(z)),
        &|_, _| {},
    );

    let res = min_w
        .iter()
        .map(|row| *row.iter().max().unwrap())
        .min()
        .unwrap();
    writeln!(writer, "{}", res).unwrap();
}
