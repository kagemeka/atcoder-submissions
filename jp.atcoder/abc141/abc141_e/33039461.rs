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
        let lcp = z_algorithm(&s[i..]);
        for (j, &d) in lcp.iter().enumerate() {
            if d > j {
                continue;
            }
            mx = mx.max(d);
        }
    }
    writeln!(writer, "{}", mx).unwrap();
}
pub fn z_algorithm<T: PartialEq>(a: &[T]) -> Vec<usize> {
    let n = a.len();
    let mut lcp = vec![0; n];
    let mut l = 0;
    for i in 1..n {
        let r = l + lcp[l];
        let mut d = if r <= i { 0 } else { lcp[i - l].min(r - i) };
        while i + d < n && a[i + d] == a[d] {
            d += 1;
        }
        lcp[i] = d;
        if r < i + d {
            l = i;
        }
    }
    lcp[0] = n;
    lcp
}
