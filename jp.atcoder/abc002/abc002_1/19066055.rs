#[allow(unused_imports)]
use std::{
  cmp::{min, max},
  io::{
    BufWriter,
    stdin,
    stdout,
    Write
  },
};


#[derive(Default)]
struct Scanner {
  buffer: Vec<String>,
}

impl Scanner {
  fn next<T: std::str::FromStr>(
    &mut self,
  ) -> T {
    loop {
      if let Some(token) =
      self.buffer.pop() {
        return token.parse().ok()
        .expect("Failed parse");
      }
      let mut input = String::new();
      stdin().read_line(
        &mut input,
      ).expect("Failed read");
      self.buffer = input
        .split_whitespace().rev()
        .map(String::from)
        .collect();
    }
  }
}


fn solve(x: i64, y: i64) {
  println!("{}", max(x, y));
}


fn main() {
  let mut sc = Scanner::default();
  let x = sc.next::<i64>();
  let y = sc.next::<i64>();
  solve(x, y);
}
