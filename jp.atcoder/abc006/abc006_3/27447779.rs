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

    let mut n: usize = sc.scan();
    let mut m: usize = sc.scan();
    let mut x: usize = 0;
    let mut y: usize = 0;
    let mut z: usize = 0;
    let ng = "-1 -1 -1";
    if m & 1 == 1 {
        if m == 1 {
            writeln!(out, "{}", ng).unwrap();
            return;
        }
        m -= 3;
        y += 1;
        n -= 1;
    }
    if m / 2 < n {
        writeln!(out, "{}", ng).unwrap();
        return;
    }
    z = m / 2 - n;
    if n < z {
        writeln!(out, "{}", ng).unwrap();
        return;
    }
    x = n - z;
    writeln!(out, "{} {} {}", x, y, z).unwrap();

}
