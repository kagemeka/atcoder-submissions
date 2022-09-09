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
/// edges are directed.
/// similar to bellman ford.
/// but epochs must be specified by user.
pub fn bellman_ford_strict<F>(edges: &[(usize, usize)], mut f: F, epochs: usize)
where
    F: FnMut(usize, usize),
{
    for _ in 0..epochs {
        for &(u, v) in edges.iter() {
            f(u, v);
        }
    }
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
    let encode = |u: usize, p: usize| -> usize { p * n + u };
    let mut edges = Vec::with_capacity(m * 2 * 4);
    for _ in 0..m {
        let u = read::<usize>() - 1;
        let v = read::<usize>() - 1;
        let p = if v == x { 1 } else { 0 };
        let q = if u == x { 1 } else { 0 };
        for j in 0..2 {
            edges.push((encode(u, j), encode(v, j ^ p)));
            edges.push((encode(v, j), encode(u, j ^ q)));
        }
    }
    let mut dp = vec![0; n * 2];
    let mut ndp = vec![0; n * 2];
    let s = encode(s, 0);
    let t = encode(t, 0);
    dp[s] = 1;
    let mut epochs = 0;
    const MOD: usize = 998_244_353;
    let m = edges.len();
    let mut f = |u: usize, v: usize| {
        ndp[v] += dp[u];
        ndp[v] %= MOD;
        epochs += 1;
        if epochs % m == 0 {
            std::mem::swap(&mut dp, &mut ndp);
            for x in ndp.iter_mut() {
                *x = 0;
            }
        }
    };
    bellman_ford_strict(&edges, &mut f, k);
    writeln!(writer, "{}", dp[t]).unwrap();
}
