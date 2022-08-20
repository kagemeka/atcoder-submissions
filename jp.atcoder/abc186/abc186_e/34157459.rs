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
pub fn extgcd(a: i64, b: i64) -> (i64, i64, i64) {
    if b == 0 {
        return if a < 0 { (-a, -1, 0) } else { (a, 1, 0) };
    }
    let (g, s, t) = extgcd(b, a % b);
    (g, t, s - a / b * t)
}
pub fn crt(mr: &[(i64, i64)]) -> Option<(i64, i64)> {
    let (mut m, mut r) = (1, 0);
    for &(m1, mut r1) in mr.iter() {
        assert!(m1 > 0);
        r1 %= m1;
        let (g, inv_u, _) = extgcd(m, m1);
        if (r1 - r) % g != 0 {
            return None;
        }
        let u1 = m1 / g;
        let x = (r1 - r) / g * inv_u % u1;
        r += x * m;
        m *= u1;
    }
    if r < 0 {
        r += m;
    }
    debug_assert!(0 <= r && r < m);
    Some((m, r))
}
/// find a solution for ax + b = 0 (mod m)
/// y := ax + b
/// y = 0 (mod m)
/// y = b (mod a)
pub fn mod_linear_equation(m: i64, a: i64, mut b: i64) -> Option<i64> {
    if b < 0 {
        b += m;
    }
    let (m, mut y) = crt(&[(m, 0), (a, b)])?;
    if y < b {
        y += m;
    }
    let x = (y - b) / a;
    // if x < 0 {
    //     x += m;
    // }
    debug_assert!(0 <= x && x < m);
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
