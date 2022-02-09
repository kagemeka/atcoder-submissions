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

    let n: usize = sc.scan();
    let m: usize = sc.scan();

    let inf = std::i64::MAX;
    let mut g: Vec<Vec<i64>> = vec![vec![inf; n]; n];
    for _ in 0..m {
        let mut a: usize = sc.scan();
        let mut b: usize = sc.scan();
        a -= 1;
        b -= 1;
        let t: i64 = sc.scan();
        g[a][b] = t;
        g[b][a] = t;
    }
    for i in 0..n { g[i][i] = 0; }
    let dist = floyd_warshall(g.clone()).ok().unwrap();
    writeln!(out, "{:?}", dist.iter().map(|x| x.iter().max().unwrap()).min().unwrap()).unwrap();

}


#[derive(Debug)]
pub struct NegativeCycleError {
    msg: &'static str,
}

impl NegativeCycleError {
    fn new() -> Self {
        Self { msg: "Negative Cycle Found." }
    }
}

impl std::fmt::Display for NegativeCycleError {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        write!(f, "{}", self.msg)
    }
}

impl std::error::Error for NegativeCycleError {
    fn description(&self) -> &str { &self.msg }
}



/// O(V^3)
pub fn floyd_warshall(mut g: Vec<Vec<i64>>) -> Result<Vec<Vec<i64>>, NegativeCycleError> {
    let inf = std::i64::MAX;
    let n = g.len();
    for k in 0..n {
        for i in 0..n {
            for j in 0..n {
                if g[i][k] == inf || g[k][j] == inf { continue; }
                g[i][j] = std::cmp::min(g[i][j], g[i][k] + g[k][j]);
            }
        }
    }
    for i in 0..n {
        if g[i][i] < 0 { return Err(NegativeCycleError::new()); }
    }
    Ok(g)
}
