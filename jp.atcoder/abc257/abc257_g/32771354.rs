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

pub fn z_algorithm<T>(a: &[T]) -> Vec<usize>
where
    T: PartialEq,
{
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

fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());

    let mut s = read::<String>().chars().collect::<Vec<_>>();
    let mut t = read::<String>().chars().collect::<Vec<_>>();
    let n = s.len();
    let m = t.len();
    s.push('$');
    s.append(&mut t);
    let lcp = &z_algorithm(&s)[n + 1..];
    let mut r = 0;
    let mut i = 0;
    let mut k = 0;
    while r < m {
        let mut nr = r;
        while i <= r {
            nr = nr.max(i + lcp[i]);
            i += 1;
        }
        if nr == r {
            writeln!(writer, "-1").unwrap();
            return;
        }
        r = nr;
        k += 1;
    }
    writeln!(writer, "{}", k).unwrap();
}
