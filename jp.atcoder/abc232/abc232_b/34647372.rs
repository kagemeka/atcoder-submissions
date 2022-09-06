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
use std::hash::Hash;
/// caesart cipher
pub fn encrypt<T: Eq + Hash + Clone>(table: &[T], a: &[T], k: usize) -> Vec<T> {
    let mut idx = std::collections::HashMap::new();
    for (i, x) in table.iter().enumerate() {
        idx.insert(x.clone(), i);
    }
    let n = table.len();
    assert_eq!(idx.len(), n);
    a.iter().map(|x| table[(idx[x] + k) % n].clone()).collect()
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let s: String = read();
    let t: String = read();
    let s = s.as_bytes();
    let t = t.as_bytes();
    let d = (t[0] + 26 - s[0]) % 26;
    let table = "abcdefghijklmnopqrstuvwxyz".as_bytes();
    let s = encrypt(&table, &s, d as usize);
    writeln!(writer, "{}", if s == t { "Yes" } else { "No" }).unwrap();
}
