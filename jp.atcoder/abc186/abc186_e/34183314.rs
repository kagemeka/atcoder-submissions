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
pub fn extgcd(mut a: i64, mut b: i64) -> (i64, i64, i64) {
    use std::mem::swap;
    let (mut x00, mut x01, mut x10, mut x11) = (1, 0, 0, 1);
    while b != 0 {
        let q = a / b;
        a %= b;
        swap(&mut a, &mut b);
        x00 -= q * x01;
        swap(&mut x00, &mut x01);
        x10 -= q * x11;
        swap(&mut x10, &mut x11);
        // (a, b) = (b, a % b);
        // (x00, x01) = (x01, x00 - q * x01);
        // (x10, x11) = (x11, x10 - q * x11);
    }
    if a >= 0 { (a, x00, x10) } else { (-a, -x00, -x10) }
}
pub fn mod_gcd_inv(modulus: i64, n: i64) -> (i64, i64) {
    let (g, mut x, _) = extgcd(n, modulus);
    let u = modulus / g;
    if x < 0 {
        x += u;
    }
    debug_assert!(0 <= x && x <= u);
    (g, x)
}
pub fn modinv(modulus: i64, x: i64) -> i64 {
    let (g, inv) = mod_gcd_inv(modulus, x);
    assert!(g == 1);
    return inv;
}
pub fn garner_with_mod(modulus: i64, mr: &[(i64, i64)]) -> i64 {
    let n = mr.len();
    let mut mr = mr.to_vec();
    mr.push((modulus, 0)); // 0 is meaningless.
    let mut v = vec![0; n + 1]; // previsous value v_{i-1} (mod m_i)
    let mut m_prod = vec![1; n + 1]; // \prod_{j<i} m_j (mod m_i)
    for (i, &(m, r)) in mr.iter().enumerate().take(n) {
        let t = (r - v[i]) % m * modinv(m, m_prod[i]) % m;
        for ((v, p), x) in v[i + 1..]
            .iter_mut()
            .zip(m_prod[i + 1..].iter_mut())
            .zip(mr[i + 1..].iter())
        {
            *v += t * *p % x.0;
            *v %= x.0;
            *p *= m % x.0;
            *p %= x.0;
        }
    }
    if v[n] < 0 { v[n] + modulus } else { v[n] }
}
pub fn gcd(a: i64, b: i64) -> i64 {
    if b == 0 { a.abs() } else { gcd(b, a % b) }
}
/// find a solution for ax + b = 0 (mod m)
/// y := ax + b
/// y = 0 (mod m)
/// y = b (mod a)
pub fn mod_linear_equation(mut m: i64, mut a: i64, mut b: i64) -> Option<i64> {
    assert!(m > 0 && a > 0);
    let g = gcd(m, a);
    if b % g != 0 {
        return None;
    }
    m /= g;
    a /= g;
    b /= g;
    let lcm = m * a;
    let mut y = garner_with_mod(m * a, &[(m, 0), (a, b)]);
    if y < b {
        y += lcm;
    }
    let x = (y - b) / a;
    debug_assert!(0 <= x && x < lcm);
    Some(x)
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
            if let Some(x) = mod_linear_equation(n, k, s) { x } else { -1 }
        )
        .unwrap();
    }
}
