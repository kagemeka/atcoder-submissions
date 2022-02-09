fn readline() -> String {
    let mut buf: String = String::new();
    std::io::stdin().read_line(&mut buf).unwrap();
    buf
}

fn read_int() -> i64 {
    readline().trim().parse::<i64>().unwrap()
}

fn main() {
    println!("{}", read_int() - read_int());
}
