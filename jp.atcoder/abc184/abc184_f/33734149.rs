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
pub fn subset_sum_max(less_than: usize, a: &[usize]) -> usize {
    let merge = |a: &[usize], x: usize| -> Vec<usize> {
        let mut i = 0;
        let n = a.len();
        let mut b = Vec::with_capacity(n << 1);
        for &y in a.iter() {
            while i < n && a[i] + x <= y {
                b.push(a[i] + x);
                i += 1;
            }
            b.push(y);
        }
        while i < n {
            b.push(a[i] + x);
            i += 1;
        }
        b
    };
    let mut b = vec![0];
    let mut c = vec![0];
    for &x in a {
        b = merge(&b, x);
        std::mem::swap(&mut b, &mut c);
    }
    let mut mx = 0;
    c.reverse();
    let mut i = 0;
    for x in b.into_iter().take_while(|&x| x < less_than) {
        while x + c[i] >= less_than {
            i += 1;
        }
        mx = mx.max(x + c[i]);
    }
    mx
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: usize = read();
    let t: usize = read();
    let a: Vec<_> = (0..n).map(|_| read::<usize>()).collect();
    writeln!(writer, "{}", subset_sum_max(t + 1, &a)).unwrap();
}
