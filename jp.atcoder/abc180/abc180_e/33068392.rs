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
pub mod traveling_salesperson_giving {
    use std::ops::*;
    pub fn tsp<T>(inf: T, g: &[Vec<T>], src: usize) -> T
    where
        T: Clone + Add<Output = T> + Ord,
    {
        let n = g.len();
        let mut dist = vec![vec![inf.clone(); n]; 1 << n];
        for i in 0..n {
            if i == src {
                continue;
            }
            dist[1 << i][i] = g[src][i].clone();
        }
        for s in 0..1 << n {
            for i in 0..n {
                if s >> i & 1 == 1 {
                    continue;
                }
                let t = s | 1 << i;
                for j in 0..n {
                    if !s >> j & 1 == 1 {
                        continue;
                    }
                    if dist[s][j] == inf || g[j][i] == inf {
                        continue;
                    }
                    dist[t][i] = dist[t][i]
                        .clone()
                        .min(dist[s][j].clone() + g[j][i].clone());
                }
            }
        }
        dist.last().unwrap()[src].clone()
    }
}
// pub mod traveling_salesperson_taking {
// }
fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: usize = read();
    const INF: i32 = 1 << 29;
    let mut g = vec![vec![INF; n]; n];
    let xyz = (0..n)
        .map(|_| {
            let x: i32 = read();
            let y: i32 = read();
            let z: i32 = read();
            (x, y, z)
        })
        .collect::<Vec<_>>();
    for i in 0..n {
        let (x, y, z) = xyz[i];
        for j in 0..n {
            let (a, b, c) = xyz[j];
            g[i][j] =
                a.abs_diff(x) as i32 + b.abs_diff(y) as i32 + 0.max(c - z);
        }
    }
    use traveling_salesperson_giving::tsp;
    let res = tsp(INF, &g, 0);
    writeln!(writer, "{}", res).unwrap();
}
