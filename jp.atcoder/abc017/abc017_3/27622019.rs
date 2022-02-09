
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

    let n: usize = sc.scan();
    let m: usize = sc.scan();
    let mut a: Vec<isize> = vec![0; m + 1];
    let mut tot: isize = 0;
    for _ in 0..n {
        let l = sc.scan::<usize>() - 1;
        let r = sc.scan::<usize>() - 1;
        let s = sc.scan::<isize>();
        tot += s;
        a[l] += s;
        a[r + 1] -= s;
    }
    for i in 0..m { a[i + 1] += a[i]; }
    let mn = a[..m].iter().min().unwrap();
    writeln!(out, "{}", tot - mn).unwrap();

}
