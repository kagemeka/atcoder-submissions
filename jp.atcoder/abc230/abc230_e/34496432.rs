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
pub fn isqrt(n: usize) -> usize {
    if n < 2 {
        return n;
    }
    let mut ok = 0;
    let mut ng = n.min(1 << 32);
    while ng - ok > 1 {
        let x = (ok + ng) >> 1;
        if x * x <= n {
            ok = x;
        } else {
            ng = x;
        }
    }
    ok
}
/// \sum_{i=1}^{n} [n/i]
pub fn floor_sum(n: usize) -> usize {
    let mut s = 0;
    let k = isqrt(n);
    for i in 1..n / (k + 1) + 1 {
        s += n / i;
    }
    for x in 1..k + 1 {
        s += x * (n / x - n / (x + 1))
    }
    s
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: usize = read();
    writeln!(writer, "{}", floor_sum(n)).unwrap();
}
