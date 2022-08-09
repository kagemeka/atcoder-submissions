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
pub fn factorize_factorial(n: usize) -> Vec<usize> {
    let mut cnt = vec![0; n + 1];
    for mut x in 2..n + 1 {
        for i in 2..x {
            if i * i > x {
                break;
            }
            while x % i == 0 {
                x /= i;
                cnt[i] += 1;
            }
        }
        if x > 1 {
            cnt[x] += 1;
        }
    }
    cnt
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: usize = read();
    let mut c = vec![0; 100];
    for e in factorize_factorial(n) {
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
