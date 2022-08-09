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
pub fn enumerate_primes(less_than: u32) -> Vec<u32> {
    let n = less_than as usize;
    let mut primes = Vec::with_capacity(n >> 4);
    if n > 2 {
        primes.push(2);
    }
    let mut is_prime = vec![true; n >> 1];
    for i in (3..n).step_by(2) {
        if !is_prime[i >> 1] {
            continue;
        }
        primes.push(i as u32);
        for j in (i * i >> 1..n >> 1).step_by(i) {
            is_prime[j] = false;
        }
    }
    primes
}
pub fn legendre_function(mut n: u64, p: u64) -> u64 {
    let mut cnt = 0;
    while n > 0 {
        cnt += n / p;
        n /= p;
    }
    cnt
}
pub fn factorize_factorial(n: usize) -> Vec<(usize, usize)> {
    enumerate_primes(n as u32 + 1)
        .into_iter()
        .map(|p| (p as usize, legendre_function(n as u64, p as u64) as usize))
        .collect()
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: usize = read();
    let mut c = vec![0; 100];
    for (_, e) in factorize_factorial(n) {
        c[e] += 1;
    }
    for i in (0..n - 1).rev() {
        c[i] += c[i + 1];
    }
    let mut s = 0;
    s += c[74];
    s += c[24] * (c[2] - 1);
    s += c[14] * (c[4] - 1);
    s += c[4] * (c[4] - 1) * (c[2] - 2) / 2;
    writeln!(writer, "{}", s).unwrap();
}
