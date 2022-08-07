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
pub fn combinations(n: usize, k: usize) -> Vec<Vec<usize>> {
    assert!(k <= n);
    let mut res = vec![];
    let mut a: Vec<_> = (0..k).collect();
    loop {
        res.push(a.clone());
        let mut i = k;
        for j in (0..k).rev() {
            if a[j] != j + n - k {
                i = j;
                break;
            }
        }
        if i == k {
            return res;
        }
        a[i] += 1;
        for j in i + 1..k {
            a[j] = a[j - 1] + 1;
        }
    }
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: usize = read();
    let m: usize = read();
    for c in combinations(m, n).into_iter() {
        for i in 0..n {
            write!(
                writer,
                "{}{}",
                c[i] + 1,
                if i == n - 1 { '\n' } else { ' ' }
            )
            .unwrap();
        }
    }
}
