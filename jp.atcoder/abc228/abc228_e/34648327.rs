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
pub fn pow_of_pow(p: i64, mut x: i64, mut y: i64, z: i64) -> i64 {
    x %= p;
    if x == 0 {
        return if y == 0 { 1 } else { 0 };
    }
    y %= p - 1;
    pow(p, x, pow(p - 1, y, z))
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: i64 = read();
    let k: i64 = read();
    let m: i64 = read();
    writeln!(writer, "{}", pow_of_pow(998_244_353, m, k, n)).unwrap();
}
