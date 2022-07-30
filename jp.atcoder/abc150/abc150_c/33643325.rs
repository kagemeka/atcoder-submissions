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
pub fn permutation_rank(p: &[usize]) -> usize {
    let n = p.len();
    let mut s = (1usize << n) - 1;
    let mut fact = 1;
    let mut rank = 0;
    for (i, &p) in p.iter().rev().enumerate() {
        rank += (p - (s & ((1 << p) - 1)).count_ones() as usize) * fact;
        s &= !(1 << p);
        fact *= i + 1;
    }
    rank
}
fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: usize = read();
    let p: Vec<_> = (0..n).map(|_| read::<usize>() - 1).collect();
    let q: Vec<_> = (0..n).map(|_| read::<usize>() - 1).collect();
    let mut pr = permutation_rank(&p);
    let mut qr = permutation_rank(&q);
    use std::mem::swap;
    if pr > qr {
        swap(&mut pr, &mut qr);
    }
    writeln!(writer, "{}", qr - pr).unwrap();
}
