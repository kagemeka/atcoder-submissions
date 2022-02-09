pub struct Scanner<R: std::io::Read> {
    reader: R,
}

impl<R: std::io::Read> Scanner<R> {
    /// let stdin = std::io::stdin();
    /// let mut sc = Scanner::new(stdin.lock());
    pub fn new(reader: R) -> Self { Self { reader: reader } }

    pub fn scan<T: std::str::FromStr>(&mut self) -> T {
        use std::io::Read;
        self.reader.by_ref().bytes().map(|c| c.unwrap() as char)
        .skip_while(|c| c.is_whitespace())
        .take_while(|c| !c.is_whitespace())
        .collect::<String>().parse::<T>().ok().unwrap()
    }
}



// #[allow(warnings)]
fn main() {
    use std::io::Write;
    let stdin = std::io::stdin();
    let mut sc = Scanner::new(std::io::BufReader::new(stdin.lock()));
    let stdout = std::io::stdout();
    let out = &mut std::io::BufWriter::new(stdout.lock());

    let n: usize = sc.scan();
    let mut c: Vec<usize> = vec![0; n];
    for i in 0..n {
        c[i] = sc.scan();
    }
    let lis = longest_increasing_sequence(&c);
    writeln!(out, "{}", n - lis.len()).unwrap();
}


pub trait Inf { const INF: Self; }


impl Inf for usize {
    const INF: usize = usize::MAX;
}


pub fn longest_increasing_sequence<T: Ord + Inf + Clone + Copy>(a: &[T]) -> Vec<T> {
    let n = a.len();
    println!("{}", n);
    let mut lis = vec![T::INF; n];
    for &x in a.iter() {
        let i = lower_bound(&lis, &x);
        lis[i] = x;
    }
    let i = lower_bound(&lis, &T::INF);
    lis[..i].to_vec()
}



pub fn bisect<T>(is_ok: &dyn Fn(&T) -> bool, a: &[T]) -> usize {
    let mut lo = 0;
    let mut hi = a.len();
    while lo < hi {
        let i = (lo + hi) >> 1;
        if is_ok(&a[i]) { hi = i; } else { lo = i + 1; }
    }
    lo
}

pub fn lower_bound<T: Ord>(a: &[T], x: &T) -> usize {
    let is_ok = |y: &T| y >= x;
    bisect(&is_ok, a)
}
