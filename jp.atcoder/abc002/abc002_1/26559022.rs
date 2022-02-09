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
                .split_whitespace().rev()
                .map(String::from)
                .collect();
        }
    }
}


fn main() {
    let mut scanner: Scanner = Scanner::default();
    let x = scanner.next::<i32>();
    let y: i32 = scanner.next::<i32>();

    println!("{}", std::cmp::max(x, y));
}
