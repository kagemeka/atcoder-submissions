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
pub fn legendre(n: usize, p: usize) -> usize {
    if n == 0 { 0 } else { n / p + legendre(n / p, p) }
}
pub fn enumerate_primes(less_than: usize) -> Vec<usize> {
    let n = less_than;
    let mut primes = Vec::with_capacity(n >> 4);
    if n > 2 {
        primes.push(2);
    }
    let mut is_prime = vec![true; n >> 1];
    for i in (3..n).step_by(2) {
        if !is_prime[i >> 1] {
            continue;
        }
        primes.push(i);
        for j in (i * i >> 1..n >> 1).step_by(i) {
            is_prime[j] = false;
        }
    }
    primes
}
pub fn factorize_combination(n: usize, mut k: usize) -> Vec<(usize, usize)> {
    let mut factors = vec![];
    if k > n {
        return factors;
    }
    k = k.min(n - k);
    let lo = n - k + 1;
    let mut v: Vec<_> = (lo..=n).collect();
    for p in enumerate_primes(isqrt(n).max(k) + 1) {
        let e = legendre(n, p) - legendre(k, p) - legendre(n - k, p);
        if e > 0 {
            factors.push((p, e));
        }
        for i in ((lo + p - 1) / p * p..=n).step_by(p) {
            while v[i - lo] % p == 0 {
                v[i - lo] /= p;
            }
        }
    }
    for i in 0..k {
        if v[i] > 1 {
            factors.push((v[i], 1));
        }
    }
    factors.sort();
    factors
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: usize = read();
    let k: usize = read();
    const MOD: usize = 998_244_353;
    let mut res = 1;
    for (_, e) in factorize_combination(n, k) {
        res *= e + 1;
        res %= MOD;
    }
    writeln!(writer, "{}", res).unwrap();
}
