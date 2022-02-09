use std::ops::Add;

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


    let n: isize = sc.scan();
    let h: isize = sc.scan();
    let a: isize = sc.scan();
    let b: isize = sc.scan();
    let c: isize = sc.scan();
    let d: isize = sc.scan();
    let e: isize = sc.scan();

    let mut res = c * n;
    for x in 0..n + 1 {
        let y = ((n * e - (b + e) * x - h) as f64 / (d + e) as f64).floor() as isize + 1;
        let y = std::cmp::max(y, 0);
        if x + y > n { continue; }
        res = std::cmp::min(res, a * x + c * y);
    }
    writeln!(out, "{}", res).unwrap();
}
