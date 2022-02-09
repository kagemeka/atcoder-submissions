


fn readline()
-> String
{
  use std::io;
  let stdin = io::stdin();
  let mut buf = String::new();
  stdin.read_line(&mut buf)
  .expect("");
  buf
}



fn read_int()
-> i64
{
  let n = readline();
  let n = n.trim().parse()
  .expect("");
  n
}



fn solve(
  h1: i64,
  h2: i64,
) {
  println!("{}", h1 - h2);
}


fn main()
{
  let h1 = read_int();
  let h2 = read_int();
  solve(h1, h2);
}
