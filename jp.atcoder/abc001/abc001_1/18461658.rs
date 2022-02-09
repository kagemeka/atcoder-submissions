use std::io;
// use std::mem;


fn read() -> String {
  let mut s = String::new();
  io::stdin().read_line(&mut s).expect("cannot read");
  // return s.trim();
  return s;
}

fn read_int() -> i32 {
  let x: i32 = read().trim().parse().expect("cannot convert");
  return x;
}

fn abc001a() {
  let h1 = read_int();
  let h2 = read_int();
  println!("{}", h1-h2);
}

fn main() {
  abc001a();
}
