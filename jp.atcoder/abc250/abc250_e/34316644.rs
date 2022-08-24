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
pub fn xorshift64(seed: u64) -> u64 {
    let mut x = seed;
    x ^= x << 13;
    x ^= x >> 7;
    x ^= x << 17;
    x
}
pub fn static_xorshift64() -> u64 {
    use std::sync::atomic::{AtomicU64, Ordering::SeqCst};
    const DEFAULT_SEED: u64 = 88172645463325252;
    static CELL: AtomicU64 = AtomicU64::new(DEFAULT_SEED);
    let mut x = CELL.load(SeqCst);
    x = xorshift64(x);
    CELL.store(x, SeqCst);
    x
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: usize = read();
    let mut a: Vec<_> = (0..n).map(|_| read::<u64>()).collect();
    let mut b: Vec<_> = (0..n).map(|_| read::<u64>()).collect();
    use std::collections::{HashMap, HashSet};
    let mut hash = HashMap::new();
    for x in a.iter_mut() {
        let v = hash.entry(*x).or_insert(0);
        if *v == 0 {
            *v = static_xorshift64();
            *x = *v;
        } else {
            *x = 0;
        }
    }
    let mut s = HashSet::new();
    for x in b.iter_mut() {
        let v = hash.entry(*x).or_insert(0);
        if *v == 0 {
            *v = static_xorshift64();
        }
        if s.contains(x) {
            *x = 0;
        } else {
            s.insert(*x);
            *x = *v;
        }
    }
    for i in 0..n - 1 {
        a[i + 1] ^= a[i];
        b[i + 1] ^= b[i];
    }
    let q: usize = read();
    for _ in 0..q {
        let i = read::<usize>() - 1;
        let j = read::<usize>() - 1;
        writeln!(writer, "{}", if a[i] == b[j] { "Yes" } else { "No" })
            .unwrap();
    }
}
