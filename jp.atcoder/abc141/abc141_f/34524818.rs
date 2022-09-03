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
pub fn xor_gaussian_elimination(mut a: Vec<usize>) -> Vec<usize> {
    let n = a.len();
    let mut i = 0;
    for k in (0..64).rev() {
        let mut j = i;
        while j < n {
            if a[j] >> k & 1 == 1 {
                break;
            }
            j += 1;
        }
        if j == n {
            continue;
        }
        a.swap(i, j);
        let v = a[i];
        for (j, x) in a.iter_mut().enumerate() {
            if j == i {
                continue;
            }
            if *x >> k & 1 == 1 {
                *x ^= v;
            }
        }
        i += 1;
    }
    a
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: usize = read();
    let mut a: Vec<_> = (0..n).map(|_| read::<usize>()).collect();
    let mut s = 0;
    for &x in a.iter() {
        s ^= x;
    }
    for x in a.iter_mut() {
        *x &= !s;
    }
    a = xor_gaussian_elimination(a);
    s += a.into_iter().fold(0, |x, y| x ^ y) << 1;
    writeln!(writer, "{}", s).unwrap();
}
