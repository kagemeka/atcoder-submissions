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
pub fn count_toposort(adj_bits: &[usize]) -> usize {
    let g = adj_bits;
    let n = g.len();
    let mut dp = vec![0; 1 << n];
    dp[0] = 1;
    for s in 0..1 << n {
        for i in 0..n {
            if s >> i & 1 == 0 && g[i] & s == 0 {
                dp[s | 1 << i] += dp[s];
            }
        }
    }
    *dp.last().unwrap()
}
fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: usize = read();
    let m: usize = read();
    let mut g = vec![0; n];
    for _ in 0..m {
        let u: usize = read();
        let v: usize = read();
        g[u - 1] |= 1 << v - 1;
    }
    writeln!(writer, "{}", count_toposort(&g)).unwrap();
}
