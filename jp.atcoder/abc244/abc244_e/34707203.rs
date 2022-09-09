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
pub fn graph_bfs<F>(g: &[Vec<usize>], mut f: F, src: usize)
where
    F: FnMut(usize, usize) -> bool,
{
    let mut que = std::collections::VecDeque::new();
    que.push_back(src);
    while let Some(u) = que.pop_front() {
        for &v in g[u].iter() {
            if f(u, v) {
                que.push_back(v);
            }
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
    let mut dp = vec![0; N];
    let s = encode(0, s, 0);
    dp[s] = 1;
    const MOD: usize = 998_244_353;
    let mut to_que = vec![false; N];
    to_que[s] = true;
    let mut f = |u: usize, v: usize| -> bool {
        dp[v] += dp[u];
        dp[v] %= MOD;
        if to_que[v] {
            false
        } else {
            to_que[v] = true;
            true
        }
    };
    graph_bfs(&g, &mut f, s);
    let t = encode(k, t, 0);
    writeln!(writer, "{}", dp[t]).unwrap();
}
