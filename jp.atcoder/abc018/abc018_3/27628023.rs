
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

    let h: usize = sc.scan();
    let w: usize = sc.scan();
    let k: usize = sc.scan();
    let mut s = vec![vec![0usize; w + 2]; h + 2];
    const INF: usize = std::usize::MAX;
    for i in 0..h {
        for (j, c) in sc.scan::<String>().chars().enumerate() {
            if c == 'o' { s[i + 1][j + 1] = INF; }
        };
    }
    for i in 0..h {
        for j in 1..w + 1 {
            s[i + 1][j] = std::cmp::min(s[i + 1][j], s[i][j] + 1);
        }
    }

    for i in (0..h).rev() {
        for j in 1..w + 1 {
            s[i + 1][j] = std::cmp::min(s[i + 1][j], s[i + 2][j] + 1);
        }
    }

    for j in 0..w {
        for i in 1..h + 1 {
            s[i][j + 1] = std::cmp::min(s[i][j + 1], s[i][j] + 1);
        }
    }

    for j in (0..w).rev() {
        for i in 1..h + 1 {
            s[i][j + 1] = std::cmp::min(s[i][j + 1], s[i][j + 2] + 1);
        }
    }
    let mut cnt = 0;
    for i in 0..h {
        for j in 0..w {
            if s[i][j] >= k { cnt += 1; }
        }
    }
    writeln!(out, "{:?}", cnt).unwrap();
}
