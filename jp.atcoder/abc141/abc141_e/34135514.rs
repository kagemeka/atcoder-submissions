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
pub fn longest_border<T: PartialEq>(a: &[T]) -> Vec<usize> {
    let n = a.len();
    let mut lb = vec![0; n];
    let mut d = 0;
    for i in 1..n {
        while d != 0 && a[d] != a[i] {
            d = lb[d - 1];
        }
        if a[d] == a[i] {
            d += 1;
        }
        lb[i] = d;
    }
    lb
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: usize = read();
    let s: String = read();
    let s = s.as_bytes();
    let mut mx = 0;
    for i in 0..n {
        let lb = longest_border(&s[i..]);
        for j in 0..n - i {
            mx = mx.max((j + 1 - lb[j]).min(lb[j]));
        }
    }
    writeln!(writer, "{}", mx).unwrap();
}
