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
/// online Xor Vectors Rank
pub struct XorVectorsRank {
    rank: usize,
    basis: Vec<usize>,
}
impl XorVectorsRank {
    pub fn new(n_bits: usize) -> Self {
        Self { rank: 0, basis: vec![0; n_bits] }
    }

    pub fn get_rank(&self) -> usize { self.rank }

    fn eliminate(&self, mut x: usize) -> usize {
        for (i, b) in self.basis.iter().enumerate() {
            if x >> i & 1 == 1 {
                x ^= b;
            }
        }
        x
    }

    fn normalize_basis(&mut self, i: usize) {
        let x = self.basis[i];
        for (j, b) in self.basis.iter_mut().enumerate() {
            if i != j && *b >> i & 1 == 1 {
                *b ^= x;
            }
        }
    }

    pub fn push(&mut self, mut x: usize) {
        x = self.eliminate(x);
        for (i, b) in self.basis.iter_mut().enumerate() {
            if x >> i & 1 == 0 {
                continue;
            }
            debug_assert!(*b == 0);
            *b = x;
            self.rank += 1;
            self.normalize_basis(i);
            break;
        }
    }

    pub fn is_independent(&self, x: usize) -> bool { self.eliminate(x) != 0 }
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: usize = read();
    let m = 1 << n;
    let mut c: Vec<_> = (1..m).map(|i| (read::<usize>(), i)).collect();
    c.sort();
    let mut f = XorVectorsRank::new(n);
    let mut s = 0;
    for &(x, i) in c.iter() {
        if !f.is_independent(i) {
            continue;
        }
        f.push(i);
        s += x;
    }
    writeln!(writer, "{}", s).unwrap();
}
