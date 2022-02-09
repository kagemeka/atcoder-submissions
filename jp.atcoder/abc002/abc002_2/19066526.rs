#[allow(unused_imports)]
use std::{
  cmp::{min, max},
  io::{
    BufWriter,
    stdin,
    stdout,
    Write
  },
  collections::HashSet,

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
        return {
          token.parse().ok()
          .expect("Failed parse")
        };
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


fn solve(s: String) {
  let mut vowels = HashSet::new();
  for c in "aeiou".chars() {
    vowels.insert(c);
  }
  let mut t = String::new();
  for c in s.chars() {
    if vowels.contains(&c) {
      continue;
    } else {
      t += &c.to_string();
    }
  }
  println!("{}", t);

}


fn main() {
  let mut sc = Scanner::default();
  // let out = &mut BufWriter::new(
  //   stdout());

  let w: String = sc.next();
  solve(w);

}
