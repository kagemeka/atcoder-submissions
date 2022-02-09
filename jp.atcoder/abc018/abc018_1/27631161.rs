
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


    let n: usize = 3;
    let mut a = vec![0usize; n];
    for i in 0..n {
        a[i] = sc.scan();
    }
    let idx = argsort(&a);
    let mut rank = vec![0usize; n];
    for i in 0..n {
        rank[idx[n - 1 - i]] = i + 1;
    }
    for i in 0..n {
        writeln!(out, "{}", rank[i]).unwrap();
    }


}


pub fn argsort<T: std::cmp::Ord>(a: &Vec<T>) -> Vec<usize> {
    let mut idx: Vec<usize>  = (0..a.len()).collect();
    idx.sort_by_key(|&i| &a[i]);
    idx
}
