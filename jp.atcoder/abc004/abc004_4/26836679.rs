pub fn readline() -> String {
    let mut buf: String = String::new();
    std::io::stdin().read_line(&mut buf).unwrap();
    buf
}

pub fn read_int() -> i64 {
    readline().trim().parse::<i64>().unwrap()
}


#[derive(Default)]
pub struct Scanner {
    buffer: Vec<String>,
}

/// ```
/// let mut sc: Scanner = Scanner::default();
/// let a: i32 = sc.scan::<i32>();
/// ```
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


pub fn scan<T: ::std::str::FromStr>() -> T {
    use std::io::Read;
    std::io::stdin().lock().bytes().map(|c|c.unwrap()as char)
    .skip_while(|c|c.is_whitespace())
    .take_while(|c|!c.is_whitespace())
    .collect::<String>().parse::<T>().ok().unwrap()
}


// use std::io::Write;
/// let out = &mut std::io::BufWriter::new(std::io::stdout());


// #[allow(warnings)]
fn main() {
    let (r, g, b) = (scan::<usize>(), scan::<usize>(), scan::<usize>());
    let k: usize = 1 << 10;

    let inf = 1 << 30;
    let mut dp = vec![inf; k];
    dp[0] = 0;
    // let mut dp: Vec<Vec<i32>> = (0..k).map(|_| vec![0; k]).collect();
    let mut x = vec![-1; k];
    for j in 0..k {
        x[j] = if j <= r { 400 } else if j <= r + g { 500 } else { 600 };
    }
    for i in 0..k {
        let mut ndp = dp.clone();
        for j in 1..k {
            ndp[j] = std::cmp::min(ndp[j], dp[j - 1] + (i as i32 - x[j]).abs());
        }
        std::mem::swap(&mut dp, &mut ndp);
    }
    println!("{}", dp[r + g + b]);
}
