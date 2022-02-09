pub fn readline() -> String {
    let mut buf = String::new();
    std::io::stdin().read_line(&mut buf).unwrap();
    buf
}


#[derive(Default)]
pub struct Scanner {
  buffer: Vec<String>,
}


impl Scanner {
    pub fn next<T: std::str::FromStr>(&mut self) -> T
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
}


fn main() {
    let mut scanner: Scanner = Scanner::default();
    let mut set = std::collections::BTreeSet::<char>::default();
    for c in "aeiou".chars() {
        set.insert(c);
    }
    let s = scanner.next::<String>();
    let mut t: String = String::new();
    for c in s.chars() {
        if !set.contains(&c) {t.push(c);}
    }
    print!("{}", t);
}
