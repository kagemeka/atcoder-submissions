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

    let w: usize = sc.scan();
    let n: usize = sc.scan();
    let k: usize = sc.scan();

    let mut dp: Vec<Vec<usize>> = vec![vec![0; w + 1]; n + 1];
    for _ in 0..n {
        let a: usize = sc.scan();
        let b: usize = sc.scan();
        for i in (1..n + 1).rev() {
            for j in a..w + 1 {
                dp[i][j] = std::cmp::max(dp[i][j], dp[i - 1][j - a] + b);
            }
        }
    }
    writeln!(out, "{}", dp[k][w]).unwrap();

}
