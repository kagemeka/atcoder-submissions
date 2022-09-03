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
pub fn xor_basis_original(a: &[usize], n_bits: usize) -> Vec<usize> {
    let mut basis = vec![0; n_bits];
    let mut res = Vec::with_capacity(n_bits);
    for &v in a.iter() {
        let mut x = v;
        for (i, b) in basis.iter().enumerate() {
            if x >> i & 1 == 1 {
                x ^= b;
            }
        }
        if x == 0 {
            continue;
        }
        for (i, b) in basis.iter_mut().enumerate() {
            if x >> i & 1 == 0 {
                continue;
            }
            assert!(*b == 0);
            *b = x;
            res.push(v);
            for (j, b) in basis.iter_mut().enumerate() {
                if i == j {
                    continue;
                }
                if *b >> i & 1 == 1 {
                    *b ^= x;
                }
            }
            break;
        }
    }
    res
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
    let b = xor_basis_original(&indices, n);
    let mut s = 0;
    for &i in b.iter() {
        s += a[i - 1];
    }
    writeln!(writer, "{}", s).unwrap();
}
