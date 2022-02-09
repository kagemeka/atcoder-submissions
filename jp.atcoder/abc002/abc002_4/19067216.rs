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


// fn solve() {
// }

fn bit_count(n: i64) -> i64 {
  let mut cnt = 0;
  let mut n = n;
  while n > 0 {
    if n&1 == 1 {cnt += 1}
    n >>= 1;
  }
  cnt

}


fn main() {
  let mut sc = Scanner::default();
  // let out = &mut BufWriter::new(
  //   stdout());

  let n: i64 = sc.next();
  let m: i64 = sc.next();
  let mut relations =
    vec![0; n as usize];
  for _ in 0..m {
    let x = sc.next::<usize>() - 1;
    let y = sc.next::<usize>() - 1;
    relations[x] |= 1<<y;
    relations[y] |= 1<<x;
  }
  let mut cnt = 0;
  for s in 0..(1<<n) {
    let mut t = (1<<n) - 1;
    for i in 0..n {
      if !s>>i&1 == 1 {continue}
      t &= relations[i as usize]
        | 1<<i;
    }
    if s&t != s {continue}
    cnt = max(
      cnt, bit_count(s));
  }
  println!("{}", cnt);

}
