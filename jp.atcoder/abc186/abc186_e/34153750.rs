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
/// find a solution for ax = b (mod m)
pub fn mod_linear_equation(mut m: i64, a: i64, mut b: i64) -> Option<i64> {
    let (g, mut x) = mod_gcd_inv(m, a);
    if b % g != 0 {
        return None;
    }
    m /= g;
    b /= g;
    x = b * x % m;
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
