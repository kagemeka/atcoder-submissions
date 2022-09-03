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
pub fn xor_basis(a: &[usize], max_bit: usize) -> Vec<usize> {
    let mut basis = vec![0; max_bit];
    for &x in a.iter() {
        let mut v = x;
        for (k, b) in basis.iter_mut().enumerate() {
            if v >> k & 1 == 0 {
                continue;
            }
            if *b != 0 {
                v ^= *b;
                continue;
            }
            *b = x;
            break;
        }
    }
    basis.into_iter().filter(|b| *b != 0).collect()
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: usize = read();
    let n2 = 1 << n;
    let a: Vec<_> = (1..n2).map(|_| read::<usize>()).collect();
    let mut indices: Vec<_> = (1..n2).collect();
    indices.sort_unstable_by_key(|&i| a[i - 1]);
    let b = xor_basis(&indices, 30);
    let mut s = 0;
    for &i in b.iter() {
        s += a[i - 1];
    }
    writeln!(writer, "{}", s).unwrap();
}
