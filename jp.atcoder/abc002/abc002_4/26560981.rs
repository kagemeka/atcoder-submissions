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

    pub fn i32(&mut self) -> i32 {
        self.scan::<i32>()
    }

    pub fn string(&mut self) -> String {
        self.scan::<String>()
    }
}


// #[allow(warnings)]
fn main() {
    let mut scanner: Scanner = Scanner::default();
    let n = scanner.i32();
    let m = scanner.i32();
    let mut relations = vec![0; n as usize];
    for i in 0..n {
        relations[i as usize] |= 1 << i ;
    }
    for _ in 0..m {
        let x = scanner.i32() - 1;
        let y = scanner.i32() - 1;
        relations[x as usize] |= 1 << y;
        relations[y as usize] |= 1 << x;
    }

    let mut mx = 0;
    for s in 0..1usize << n {
        let mut t = s;
        for i in 0..n {
            if s >> i & 1 == 0 { continue; }
            t &= relations[i as usize];
        }
        if t != s { continue; }
        mx = std::cmp::max(mx, s.count_ones());
    }
    println!("{}", mx);
}
