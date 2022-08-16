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
pub fn lcp_array(a: &[usize], sa: &[usize]) -> Vec<usize> {
    let n = a.len();
    assert!(n > 0 && sa.len() == n);
    let mut rank = vec![0; n];
    for (r, &i) in sa.iter().enumerate() {
        rank[i] = r;
    }
    let mut lcp = vec![0; n - 1];
    let mut h = 0;
    for i in 0..n {
        if h != 0 {
            h -= 1;
        }
        let r = rank[i];
        if r == n - 1 {
            continue;
        }
        let j = sa[r + 1];
        while i.max(j) + h < n && a[i + h] == a[j + h] {
            h += 1;
        }
        lcp[r] = h;
    }
    lcp
}
pub fn suffix_array<T: Ord>(a: &[T]) -> Vec<usize> {
    let mut v: Vec<_> = a.iter().collect();
    v.sort_unstable();
    v.dedup();
    let mut a: Vec<_> =
        a.iter().map(|x| v.binary_search(&x).unwrap() + 1).collect();
    let n = a.len();
    let mut d = 1;
    let mut b: Vec<_> = (0..n as u32).map(|i| (0, i)).collect();
    loop {
        for x in b.iter_mut() {
            x.0 = a[x.1 as usize] << 30
                | a.get(x.1 as usize + d).map_or(0, |r| *r);
        }
        b.sort_unstable_by_key(|&x| x.0);
        d <<= 1;
        if d >= n {
            break;
        }
        let mut rank = 0;
        let mut prev = 0;
        for x in b.iter() {
            if x.0 > prev {
                rank += 1;
                prev = x.0;
            }
            a[x.1 as usize] = rank;
        }
        if rank == n {
            break;
        }
    }
    b.into_iter().map(|x| x.1 as usize).collect()
}
pub fn count_substrings(a: &[usize]) -> usize {
    let sa = suffix_array(a);
    let lcp = lcp_array(&a, &sa);
    let n = sa.len();
    n * (n + 1) / 2 - lcp.iter().sum::<usize>()
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let s: String = read();
    writeln!(
        writer,
        "{}",
        count_substrings(&s.chars().map(|x| x as usize).collect::<Vec<_>>())
    )
    .unwrap();
}
