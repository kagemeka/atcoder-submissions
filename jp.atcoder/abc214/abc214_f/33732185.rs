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
pub fn number_of_subsequences<T: std::hash::Hash + Eq>(
    m: i64, a: &[T], min_step: usize,
) -> i64 {
    let n: usize = a.len();
    let mut dp = vec![0; n + 1];
    dp[0] = 1;
    let mut prev = std::collections::HashMap::new();
    for i in 0..n {
        dp[i + 1] = dp[i] + dp[i.max(min_step) - min_step];
        let j = prev.entry(&a[i]).or_insert(n);
        if *j != n {
            dp[i + 1] -= dp[(*j).max(min_step) - min_step];
        }
        dp[i + 1] %= m;
        *j = i;
    }
    (*dp.last().unwrap() + m) % m
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let s: String = read();
    const MOD: i64 = 1_000_000_007;
    let res = number_of_subsequences(MOD, s.as_bytes(), 1);
    writeln!(writer, "{}", (res - 1 + MOD) % MOD).unwrap();
}
