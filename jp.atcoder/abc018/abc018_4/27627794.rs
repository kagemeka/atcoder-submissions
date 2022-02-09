
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
    let p: usize = sc.scan();
    let q: usize = sc.scan();
    let r: usize = sc.scan();
    let mut g: Vec<Vec<usize>> = vec![vec![0; m]; n];
    for _ in 0..r {
        let x: usize = sc.scan::<usize>() - 1;
        let y: usize = sc.scan::<usize>() - 1;
        let z: usize = sc.scan();
        g[x][y] = z;
    }
    let mut mx = 0usize;
    for s in 0usize..1 << n {
        if s.count_ones() as usize != p { continue; }
        let mut a = vec![0usize; m];
        for i in 0..n {
            if s >> i & 1 != 1 { continue; }
            for j in 0..m {
                a[j] += g[i][j];
            }
        }
        a.sort();
        mx = std::cmp::max(mx, a[m - q..].iter().sum());
    }
    writeln!(out, "{}", mx).unwrap();
}
