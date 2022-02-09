
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


    let s: String = sc.scan();

    fn is_choku(s: &str) -> bool {
        let choku_tail = ["ch", "o", "k", "u"];
        let n = s.len();
        if s.len() == 0 { return true; }
        if choku_tail.contains(&&s[n - 1..n]) && is_choku(&s[..n - 1]) {
            return true;
        }
        if n >= 2 && &s[n - 2..n] == "ch" && is_choku(&s[..n - 2]) {
            return true;
        }
        false
    }
    writeln!(out, "{}", if is_choku(&s) { "YES" } else { "NO" }).unwrap();
}
