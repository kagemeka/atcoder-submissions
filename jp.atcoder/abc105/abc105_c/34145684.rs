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
pub fn decimal_to_base_k(k: i64, mut n: i64) -> Vec<i64> {
    assert!(k.abs() >= 2);
    let mut nums = vec![];
    loop {
        nums.push(n.rem_euclid(k));
        n = n.div_euclid(k);
        if n == 0 {
            return nums;
        }
    }
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: i64 = read();
    let mut a = decimal_to_base_k(-2, n);
    a.reverse();
    let n = a.len();
    for i in 0..n {
        write!(writer, "{}", a[i]).unwrap();
    }
    writeln!(writer).unwrap();
}
