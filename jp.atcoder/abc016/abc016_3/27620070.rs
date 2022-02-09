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

    let mut relation = vec![0usize; n];
    for _ in 0..m {
        let a: usize = sc.scan::<usize>() - 1;
        let b: usize = sc.scan::<usize>() - 1;
        relation[a] |= 1 << b;
        relation[b] |= 1 << a;
    }
    for i in 0..n {
        let mut ff = 0usize;
        for j in 0..n {
            if relation[i] >> j & 1 == 0 { continue; }
            ff |= relation[j];
        }
        ff &= !(relation[i] | 1 << i);
        writeln!(out, "{}", ff.count_ones()).unwrap();
    }
}
