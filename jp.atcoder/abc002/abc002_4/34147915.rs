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
pub fn max_clique(adj_bits: &[usize]) -> usize {
    let g = adj_bits;
    let n = g.len();
    let mut mx = 0;
    for s in 0..1 << n {
        let mut cnt = 0;
        let mut t = s;
        for i in 0..n {
            if s >> i & 1 == 0 {
                continue;
            }
            cnt += 1;
            t &= g[i] | 1 << i;
        }
        if t == s {
            mx = mx.max(cnt);
        }
    }
    mx
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: usize = read();
    let m: usize = read();
    let mut g = vec![0; n];
    for _ in 0..m {
        let u = read::<usize>() - 1;
        let v = read::<usize>() - 1;
        g[u] |= 1 << v;
        g[v] |= 1 << u;
    }
    writeln!(writer, "{}", max_clique(&g)).unwrap();
}
