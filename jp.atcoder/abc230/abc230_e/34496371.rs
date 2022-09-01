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
/// \sum_{i=1}^{n} [n/i]
pub fn floor_sum(n: usize) -> usize {
    let mut i = 1;
    let mut s = 0;
    while i <= n {
        let x = n / i;
        let ni = n / x + 1;
        s += x * (ni - i);
        i = ni;
    }
    s
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: usize = read();
    writeln!(writer, "{}", floor_sum(n)).unwrap();
}
