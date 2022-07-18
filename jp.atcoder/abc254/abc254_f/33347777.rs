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
pub struct SparseTable<T, F> {
    data: Vec<Vec<T>>,
    f: F,
}
impl<T: Clone, F: Fn(T, T) -> T> SparseTable<T, F> {
    pub fn new(f: F, a: &[T]) -> Self {
        let n = a.len();
        assert!(n > 0);
        let h = n.next_power_of_two().trailing_zeros().max(1) as usize;
        let mut data = vec![vec![]; h];
        data[0] = a.to_vec();
        for i in 1..h {
            let d1 = 1 << i;
            let d0 = d1 >> 1;
            let w = n - d1 + 1;
            data[i] = (0..w)
                .map(|j| f(data[i - 1][j].clone(), data[i - 1][j + d0].clone()))
                .collect();
        }
        Self { data, f }
    }

    pub fn size(&self) -> usize { self.data[0].len() }

    pub fn get(&self, l: usize, r: usize) -> T {
        assert!(l < r && r <= self.size());
        if r - l == 1 {
            return self.data[0][l].clone();
        }
        let i = (r - l).next_power_of_two().trailing_zeros() as usize - 1;
        (self.f)(self.data[i][l].clone(), self.data[i][r - (1 << i)].clone())
    }
}
pub fn gcd(a: i64, b: i64) -> i64 { if b == 0 { a } else { gcd(b, a % b) } }
fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    // let f = |a: i64, b: i64| gcd(a, b);
    let n: usize = read();
    let q: usize = read();
    let a: Vec<_> = (0..n).map(|_| read::<i64>()).collect();
    let b: Vec<_> = (0..n).map(|_| read::<i64>()).collect();
    let mut da = a.clone();
    let mut db = b.clone();
    for i in 0..n - 1 {
        da[i] = da[i + 1] - da[i];
        db[i] = db[i + 1] - db[i];
    }
    let spa = SparseTable::new(gcd, &da);
    let spb = SparseTable::new(gcd, &db);
    for _ in 0..q {
        let h0 = read::<usize>() - 1;
        let h1 = read::<usize>() - 1;
        let w0 = read::<usize>() - 1;
        let w1 = read::<usize>() - 1;
        let mut g = a[h0] + b[w0];
        if h0 < h1 {
            g = gcd(g, spa.get(h0, h1));
        }
        if w0 < w1 {
            g = gcd(g, spb.get(w0, w1));
        }
        writeln!(writer, "{}", g.abs()).unwrap();
    }
}
