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
pub fn functional_graph_prop(f: &[usize], src: usize) -> (Vec<usize>, usize) {
    let n = f.len();
    let mut idx = vec![n; n];
    let mut preorder = Vec::with_capacity(n);
    let mut x = src;
    for i in 0..n + 1 {
        if idx[x] == n {
            idx[x] = i;
            preorder.push(x);
            x = f[x];
            continue;
        }
        return (preorder, idx[x]);
    }
    panic!();
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: usize = read();
    let x: usize = read();
    let m: usize = read();
    let f: Vec<_> = (0..m).map(|x| x * x % m).collect();
    let (mut a, k) = functional_graph_prop(&f, x);
    let l = a.len() - k;
    for i in 1..a.len() {
        if i == k {
            continue;
        }
        a[i] += a[i - 1];
    }
    let mut n = n - 1;
    if n < k {
        writeln!(writer, "{}", a[n]).unwrap();
        return;
    }
    let mut res = 0;
    if k > 0 {
        res += a[k - 1];
        n -= k;
    }
    res += n / l * *a.last().unwrap();
    n %= l;
    res += a[k + n];
    writeln!(writer, "{}", res).unwrap();
}
