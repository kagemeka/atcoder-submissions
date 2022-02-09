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
}

// #[allow(warnings)]
fn main() {
    let mut scanner: Scanner = Scanner::default();
    let x0 = scanner.scan::<i32>();
    let y0 = scanner.scan::<i32>();
    let mut x1 = scanner.scan::<i32>();
    let mut y1 = scanner.scan::<i32>();
    let mut x2 = scanner.scan::<i32>();
    let mut y2 = scanner.scan::<i32>();
    x1 -= x0;
    y1 -= y0;
    x2 -= x0;
    y2 -= y0;
    println!("{}", (x1 * y2 - x2 * y1).abs() as f32 / 2.);
}
