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
const INF: i64 = std::i64::MAX;
pub struct MinMaxLinear {
    delta: i64,
    low: i64,
    high: i64,
}
impl MinMaxLinear {
    pub fn new() -> Self { Self { delta: 0, low: -INF, high: INF } }

    pub fn add(&mut self, v: i64) {
        self.delta += v;
        if self.low != -INF {
            self.low += v;
        }
        if self.high != INF {
            self.high += v;
        }
    }

    pub fn max(&mut self, v: i64) {
        self.low = self.low.max(v);
        self.high = self.high.max(v);
    }

    pub fn min(&mut self, v: i64) {
        self.low = self.low.min(v);
        self.high = self.high.min(v);
    }

    pub fn calc(&self, x: i64) -> i64 {
        (x + self.delta).min(self.high).max(self.low)
    }
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: usize = read();
    let mut f = MinMaxLinear::new();
    for _ in 0..n {
        let a: i64 = read();
        let t: u8 = read();
        if t == 1 {
            f.add(a);
        }
        if t == 2 {
            f.max(a);
        }
        if t == 3 {
            f.min(a);
        }
    }
    let q: usize = read();
    for _ in 0..q {
        let x: i64 = read();
        writeln!(writer, "{}", f.calc(x)).unwrap();
    }
}
