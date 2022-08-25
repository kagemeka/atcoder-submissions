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
use std::collections::{HashMap, HashSet};
/// pseudo random hash function: xorshift64
/// prefix set hashing method: cumulative xor
pub struct PrefixSetHash<T>(HashMap<T, u64>);
impl<T: Clone + std::hash::Hash + Eq> PrefixSetHash<T> {
    pub fn new() -> Self { Self(HashMap::new()) }

    pub fn calc(&mut self, a: &[T]) -> Vec<u64> {
        let mut s = HashSet::new();
        let mut b: Vec<_> = a
            .iter()
            .map(|x| {
                let v = self
                    .0
                    .entry(x.clone())
                    .or_insert_with(|| static_xorshift64());
                if s.contains(x) {
                    0
                } else {
                    s.insert(x.clone());
                    *v
                }
            })
            .collect();
        for i in 0..a.len() - 1 {
            b[i + 1] ^= b[i];
        }
        b
    }
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: usize = read();
    let mut a: Vec<_> = (0..n).map(|_| read::<u64>()).collect();
    let mut b: Vec<_> = (0..n).map(|_| read::<u64>()).collect();
    let mut hash = PrefixSetHash::new();
    a = hash.calc(&a);
    b = hash.calc(&b);
    let q: usize = read();
    for _ in 0..q {
        let i = read::<usize>() - 1;
        let j = read::<usize>() - 1;
        writeln!(writer, "{}", if a[i] == b[j] { "Yes" } else { "No" })
            .unwrap();
    }
}
