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
pub trait BinaryOp {
    type T;
    fn f(_: Self::T, _: Self::T) -> Self::T;
}
pub struct SparseTable<F: BinaryOp>(Vec<Vec<F::T>>);
impl<F: BinaryOp> SparseTable<F>
where
    F::T: Clone,
{
    pub fn new(a: &[F::T]) -> Self {
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
                .map(|j| {
                    F::f(data[i - 1][j].clone(), data[i - 1][j + d0].clone())
                })
                .collect();
        }
        Self(data)
    }

    pub fn size(&self) -> usize { self.0[0].len() }

    pub fn get(&self, l: usize, r: usize) -> F::T {
        assert!(l < r && r <= self.size());
        if r - l == 1 {
            return self.0[0][l].clone();
        }
        let i = (r - l).next_power_of_two().trailing_zeros() as usize - 1;
        F::f(self.0[i][l].clone(), self.0[i][r - (1 << i)].clone())
    }
}
pub fn gcd(a: i64, b: i64) -> i64 { if b == 0 { a } else { gcd(b, a % b) } }
fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
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
    struct F;
    impl BinaryOp for F {
        type T = i64;

        fn f(x: i64, y: i64) -> i64 { gcd(x, y) }
    }
    let spa = SparseTable::<F>::new(&da);
    let spb = SparseTable::<F>::new(&db);
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
