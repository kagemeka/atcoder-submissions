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
pub fn path_count(g: &[Vec<usize>], src: usize, modulus: usize) -> Vec<usize> {
    let n = g.len();
    let mut f = vec![0; n];
    f[src] = 1;
    let mut que = std::collections::VecDeque::new();
    que.push_back(src);
    let mut to_que = vec![false; n];
    to_que[src] = true;
    while let Some(u) = que.pop_front() {
        for &v in g[u].iter() {
            f[v] += f[u];
            f[v] %= modulus;
            if to_que[v] {
                continue;
            }
            to_que[v] = true;
            que.push_back(v);
        }
    }
    f
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: usize = read();
    let m: usize = read();
    let k: usize = read();
    let s: usize = read();
    let t: usize = read();
    let x: usize = read();
    let s = s - 1;
    let t = t - 1;
    let x = x - 1;
    const B: usize = 1 << 11;
    let encode =
        |i: usize, u: usize, p: usize| -> usize { (p * n + u) * B + i };
    const N: usize = 1 << 23;
    let mut g = vec![vec![]; N];
    for _ in 0..m {
        let u = read::<usize>() - 1;
        let v = read::<usize>() - 1;
        let p = if v == x { 1 } else { 0 };
        let q = if u == x { 1 } else { 0 };
        for i in 0..k {
            for j in 0..2 {
                let x = encode(i, u, j);
                let y = encode(i + 1, v, j ^ p);
                g[x].push(y);
                let x = encode(i, v, j);
                let y = encode(i + 1, u, j ^ q);
                g[x].push(y);
            }
        }
    }
    let s = encode(0, s, 0);
    let t = encode(k, t, 0);
    const MOD: usize = 998_244_353;
    let cnt = path_count(&g, s, MOD);
    writeln!(writer, "{}", cnt[t]).unwrap();
}
