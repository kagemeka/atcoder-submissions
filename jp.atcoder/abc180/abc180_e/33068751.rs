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
pub mod traveling_salesperson_taking {
    use std::ops::*;
    pub fn tsp<T>(inf: T, g: &[Vec<T>], src: usize) -> T
    where
        T: Clone + Add<Output = T> + Ord + From<i32>,
    {
        let n = g.len();
        let mut dist = vec![vec![inf.clone(); n]; 1 << n];
        dist[1 << src][src] = 0.into();
        for s in 0..1 << n {
            for i in 0..n {
                if !s >> i & 1 == 1 {
                    continue;
                }
                let t = s & !(1 << i);
                for j in 0..n {
                    if !t >> j & 1 == 1 {
                        continue;
                    }
                    if dist[t][j] == inf || g[j][i] == inf {
                        continue;
                    }
                    dist[s][i] = dist[s][i]
                        .clone()
                        .min(dist[t][j].clone() + g[j][i].clone());
                }
            }
        }
        let mut mn = inf.clone();
        let s = (1 << n) - 1;
        for i in 0..n {
            if i == src || dist[s][i] == inf || g[i][src] == inf {
                continue;
            }
            mn = mn.min(dist[s][i].clone() + g[i][src].clone());
        }
        mn
    }
}
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
            g[i][j] = (a - x).abs() + (b - y).abs() + 0.max(c - z);
        }
    }
    use traveling_salesperson_taking::tsp;
    let res = tsp(INF, &g, 0);
    writeln!(writer, "{}", res).unwrap();
}
