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
    let k: usize = sc.scan();

    let mut a: Vec<usize> = vec![0];

    for _ in 0..n {
        let mut b: Vec<usize> = Vec::new();
        for _ in 0..k {
            let t: usize = sc.scan();
            for &x in a.iter() {
                b.push(t ^ x);
            }
        }
        b.sort();
        b.dedup();
        a = b;
    }
    writeln!(out, "{}", if a.contains(&0) { "Found" } else { "Nothing" }).unwrap();
}
