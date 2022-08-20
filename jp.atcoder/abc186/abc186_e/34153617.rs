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
/// find a solution for ax = b (mod m)
pub fn mod_linear_equation(mut m: i64, mut a: i64, mut b: i64) -> Option<i64> {
    let g = gcd(m, a);
    if b % g != 0 {
        return None;
    }
    m /= g;
    a /= g;
    b /= g;
    let x = b * modinv(m, a) % m;
    Some((x + m) % m)
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let t: usize = read();
    for _ in 0..t {
        let n: i64 = read();
        let s: i64 = read();
        let k: i64 = read();
        writeln!(
            writer,
            "{}",
            if let Some(x) = mod_linear_equation(n, k, -s) {
                x
            } else {
                -1
            }
        )
        .unwrap();
    }
}
