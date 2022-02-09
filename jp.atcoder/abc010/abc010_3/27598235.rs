pub struct Scanner<R: std::io::Read> {
    reader: R,
}

impl<R: std::io::Read> Scanner<R> {
    /// let stdin = std::io::stdin();
    /// let mut sc = Scanner::new(stdin.lock());
    pub fn new(reader: R) -> Self { Self { reader: reader } }

    pub fn scan<T: std::str::FromStr>(&mut self) -> T {
        use std::io::Read;
        self.reader.by_ref().bytes().map(|c| c.unwrap() as char)
        .skip_while(|c| c.is_whitespace())
        .take_while(|c| !c.is_whitespace())
        .collect::<String>().parse::<T>().ok().unwrap()
    }
}



// #[allow(warnings)]
fn main() {
    use std::io::Write;
    let stdin = std::io::stdin();
    let mut sc = Scanner::new(std::io::BufReader::new(stdin.lock()));
    let stdout = std::io::stdout();
    let out = &mut std::io::BufWriter::new(stdout.lock());

    let sx: i64 = sc.scan();
    let sy: i64 = sc.scan();
    let gx: i64 = sc.scan();
    let gy: i64 = sc.scan();
    let t: i64 = sc.scan();
    let v: i64 = sc.scan();
    let n: usize = sc.scan();
    let mut ok = true;
    for _ in 0..n {
        let x: i64 = sc.scan();
        let y: i64 = sc.scan();
        let mut d = (((x - sx).pow(2) + (y - sy).pow(2)) as f64).sqrt();
        d += (((gx - x).pow(2) + (gy - y).pow(2)) as f64).sqrt();
        if d <= (t * v) as f64 { ok = false; }
    }
    writeln!(out, "{}", if ok { "NO" } else { "YES" }).unwrap();
}
