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
fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: usize = read();
    let s: String = read();
    let s = s.chars().collect::<Vec<_>>();
    let mut mx = 0;
    for i in 0..n {
        let lb = morris_pratt(&s[i..]);
        for (j, &d) in lb.iter().enumerate() {
            if d * 2 > j + 1 {
                continue;
            }
            mx = mx.max(d);
        }
    }
    writeln!(writer, "{}", mx).unwrap();
}
pub fn morris_pratt<T: PartialEq>(a: &[T]) -> Vec<usize> {
    let n = a.len();
    let mut lb = vec![0; n]; // longest border
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
