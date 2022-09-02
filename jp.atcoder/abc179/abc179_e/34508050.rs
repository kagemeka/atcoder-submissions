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
pub struct PrefixSum {
    s: Vec<usize>,
    start: usize,
}
impl PrefixSum {
    pub fn new(f: &[usize], src: usize, a: &[usize]) -> Self {
        let (nodes, start) = functional_graph_prop(f, src);
        let mut s: Vec<_> = nodes.into_iter().map(|i| a[i].clone()).collect();
        for i in 1..s.len() {
            if i == start {
                continue;
            }
            s[i] += s[i - 1];
        }
        Self { s, start }
    }

    /// 0-indexed
    pub fn calc(&self, mut k: usize) -> usize {
        let j = self.start;
        let s = &self.s;
        if k < j {
            return s[k];
        }
        let mut res = 0;
        let l = s.len() - j;
        if j > 0 {
            res = s[j - 1];
            k -= j;
        }
        res += k / l * s.last().unwrap();
        k %= l;
        res += s[j + k];
        res
    }
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: usize = read();
    let x: usize = read();
    let m: usize = read();
    let f: Vec<_> = (0..m).map(|x| x * x % m).collect();
    let a: Vec<_> = (0..m).collect();
    let s = PrefixSum::new(&f, x, &a);
    writeln!(writer, "{}", s.calc(n - 1)).unwrap();
}
