fn main()
{
  use std::io::{
    stdin,
  };

  let s = stdin();

  let mut y = String::new();

  s.read_line(&mut y).unwrap();
  let y: i64 =
    y
    .trim()
    .parse()
    .unwrap();
  if y % 400 == 0
  {
    println!("YES");
    return;
  }
  if y % 100 == 0
  {
    println!("NO");
    return;
  }
  if y % 4 == 0
  {
    println!("YES");
    return;
  }
  println!("NO");
}
