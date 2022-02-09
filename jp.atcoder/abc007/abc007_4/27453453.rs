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

    let a: usize = sc.scan();
    let b: usize = sc.scan();
    writeln!(out, "{}", count(b) - count(a - 1)).unwrap();
}


fn count(n: usize) -> usize {
    let mut dp: Vec<usize> = vec![1, 0];
    let ns = n.to_string();
    for d in ns.chars() {
        let d = d.to_digit(10).unwrap() as usize;
        dp[1] = dp[1] * 8 + dp[0] * (if d <= 4 { d } else { d - 1 });
        if d == 4 || d == 9 { dp[0] = 0; }
    }
    n + 1 - dp[0] - dp[1]
}
