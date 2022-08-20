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
pub fn phi(mut n: i64) -> i64 {
    let mut c = n;
    for i in 2..n {
        if i * i > n {
            break;
        }
        if n % i != 0 {
            continue;
        }
        c -= c / i;
        while n % i == 0 {
            n /= i;
        }
    }
    if n > 1 {
        c -= c / n;
    }
    c
}
pub fn gcd(a: i64, b: i64) -> i64 {
    if b == 0 { a.abs() } else { gcd(b, a % b) }
}
pub fn pow(modulus: i64, mut x: i64, n: i64) -> i64 {
    x %= modulus;
    if n == 0 {
        return 1;
    }
    let mut y = pow(modulus, x, n >> 1);
    y = y * y % modulus;
    if n & 1 == 1 {
        y = y * x % modulus;
    }
    y
}
pub fn modinv(modulus: i64, x: i64) -> i64 {
    assert_eq!(gcd(modulus, x), 1);
    pow(modulus, x, phi(modulus) - 1)
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let t: usize = read();
    for _ in 0..t {
        let mut n: i64 = read();
        let mut s: i64 = read();
        let mut k: i64 = read();
        let g = gcd(k, n);
        if s % g != 0 {
            writeln!(writer, "{}", -1).unwrap();
            continue;
        }
        n /= g;
        s /= g;
        k /= g;
        let mut x = -s * modinv(n, k) % n;
        x = (x + n) % n;
        writeln!(writer, "{}", x).unwrap();
    }
}
