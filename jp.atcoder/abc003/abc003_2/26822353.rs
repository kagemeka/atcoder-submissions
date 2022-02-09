
pub fn readline() -> String {
    let mut buf: String = String::new();
    std::io::stdin().read_line(&mut buf).unwrap();
    buf
}

pub fn read_int() -> i64 {
    readline().trim().parse::<i64>().unwrap()
}


#[derive(Default)]
pub struct Scanner {
    buffer: Vec<String>,
}

/// example
/// let mut scanner: Scanner = Scanner::default();
/// let a: i32 = scanner.next::<i32>();
impl Scanner {
    pub fn scan<T: std::str::FromStr>(&mut self) -> T
    where
        <T as std::str::FromStr>::Err: std::fmt::Debug,
    {
        loop {
            if let Some(token) = self.buffer.pop() {
                return token.parse::<T>().unwrap();
            }
            self.buffer =
                readline()
                .trim()
                .split_whitespace().rev()
                .map(String::from)
                .collect();
        }
    }

    pub fn i32(&mut self) -> i32 {
        self.scan::<i32>()
    }

    pub fn string(&mut self) -> String {
        self.scan::<String>()
    }
}


use std::io::Write;
/// let out = &mut std::io::BufWriter::new(std::io::stdout());


// #[allow(warnings)]
fn main() {
    let mut sc = Scanner::default();
    let s: Vec<char> = sc.string().chars().collect();
    let t: Vec<char> = sc.string().chars().collect();

    let n = s.len();
    for i in 0..n {
        if s[i] == t[i] { continue; }
        if s[i] == '@' && "atcoder".contains(t[i]) { continue; }
        if t[i] == '@' && "atcoder".contains(s[i]) { continue; }
        println!("You will lose");
        return;
    }
    println!("You can win");
}
vv
