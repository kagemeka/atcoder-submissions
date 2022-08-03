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
pub fn lucas_numbers(size: usize) -> Vec<usize> {
    let mut l = vec![0; size];
    l[0] = 2;
    l[1] = 1;
    for i in 2..size {
        l[i] = l[i - 1] + l[i - 2];
    }
    l
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: usize = read();
    let l = lucas_numbers(n + 1);
    writeln!(writer, "{}", l[n]).unwrap();
}
