
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
    let mut f: Vec<usize> = Vec::with_capacity(n);
    for _ in 0..n { f.push(sc.scan::<usize>() - 1); }

    let mut prev = vec![0usize; n];
    let mut last = vec![0usize; m];
    for i in 0..n {
        prev[i] = last[f[i]];
        last[f[i]] = i + 1;
    }

    const MOD: usize = 1_000_000_007;
    let mut dp = vec![0usize; n + 1];
    let mut s = 1usize;
    dp[0] = s;
    let mut l = 0usize;
    for i in 0..n {
        while l < prev[i] {
            if s < dp[l] { s += MOD; }
            s -= dp[l];
            l += 1;
        }
        dp[i + 1] = s;
        s += dp[i + 1];
        if s >= MOD { s -= MOD; }
    }
    writeln!(out, "{:?}", dp[n]).unwrap();

}
