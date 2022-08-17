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
pub struct Fenwick(Vec<i32>);
impl Fenwick {
    pub fn new(size: usize) -> Self { Self(vec![0; size + 1]) }

    pub fn size(&self) -> usize { self.0.len() - 1 }

    pub fn add(&mut self, mut i: usize, x: i32) {
        let n = self.size();
        assert!(i < n);
        i += 1;
        while i <= n {
            self.0[i] += x;
            i += 1 << i.trailing_zeros();
        }
    }

    pub fn sum_lt(&self, mut i: usize) -> i32 {
        assert!(i <= self.size());
        let mut v = 0;
        while i > 0 {
            v += self.0[i];
            i -= 1 << i.trailing_zeros();
        }
        v
    }
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: usize = read();
    let q: usize = read();
    let a: Vec<_> = (0..n).map(|_| read::<i32>()).collect();
    let mut fw = Fenwick::new(n);
    for i in 0..n {
        fw.add(i, a[i]);
    }
    for _ in 0..q {
        let t: u8 = read();
        let x: usize = read();
        let y: i32 = read();
        if t == 0 {
            fw.add(x, y);
        } else {
            writeln!(writer, "{}", fw.sum_lt(y as usize) - fw.sum_lt(x))
                .unwrap();
        }
    }
}
