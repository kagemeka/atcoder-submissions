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
pub fn solve_ghost_leg(n: usize, edges: &[usize]) -> Vec<usize> {
    let mut res = (0..n).collect::<Vec<_>>();
    for &i in edges.iter().rev() {
        res.swap(i, i + 1);
    }
    res
}
pub fn pow_semigroup<F, X>(f: F, mut x: X, mut exp: u64) -> X
where
    F: Fn(X, X) -> X,
    X: Clone,
{
    assert!(exp > 0);
    let mut y = x.clone();
    exp -= 1;
    while exp > 0 {
        if exp & 1 == 1 {
            y = f(y, x.clone());
        }
        x = f(x.clone(), x);
        exp >>= 1;
    }
    y
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: usize = read();
    let m: usize = read();
    let k: usize = read();
    let b: Vec<_> = (0..m).map(|_| read::<usize>() - 1).collect();
    let a = solve_ghost_leg(n, &b);
    let f =
        |a: Vec<usize>, b: Vec<usize>| a.into_iter().map(|i| b[i]).collect();
    let res = pow_semigroup(f, a, k as u64);
    for i in 0..n {
        writeln!(writer, "{}", res[i] + 1).unwrap();
    }
}
