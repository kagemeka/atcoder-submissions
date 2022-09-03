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
pub fn xor_basis_original(a: &[usize]) -> Vec<usize> {
    let m = *a.iter().max().unwrap() + 1;
    let mut ok = vec![false; m];
    ok[0] = true;
    let mut res = Vec::new();
    for &x in a.iter() {
        if ok[x] {
            continue;
        }
        res.push(x);
        for i in 0..m {
            ok[i ^ x] |= ok[i];
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
    let b = xor_basis_original(&indices);
    let mut s = 0;
    for &i in b.iter() {
        s += a[i - 1];
    }
    writeln!(writer, "{}", s).unwrap();
}
