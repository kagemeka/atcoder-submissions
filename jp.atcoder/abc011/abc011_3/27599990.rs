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

    let mut n: isize = sc.scan();
    let mut ng = std::collections::HashSet::new();
    for _ in 0..3 {
        ng.insert(sc.scan::<isize>());
    }
    if ng.contains(&n) {
        writeln!(out, "NO").unwrap();
        return;
    }
    for _ in 0..100 {
        let mut ok = false;
        for d in (1..4).rev() {
            if ng.contains(&(n + d)) {
                continue;
            }
            n -= d;
            ok = true;
            break;
        }
        if n <= 0 {
            writeln!(out, "YES").unwrap();
            return;
        }
        if ok { continue; }
        writeln!(out, "NO").unwrap();
        return;
    }
    writeln!(out, "NO").unwrap();
}
