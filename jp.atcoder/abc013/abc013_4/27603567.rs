use std::ops::Add;

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
    let m: usize = sc.scan();
    let d: usize = sc.scan();
    let mut a: Vec<usize> = Vec::with_capacity(m);
    for _ in 0..m {
        a.push(sc.scan::<usize>() - 1);
    }
    let mut b = vec![0usize; n];
    for i in 0..n { b[i] = i; }
    for &i in a.iter().rev() {
        b.swap(i, i + 1);
    }

    let e = || {
        let mut a = vec![0usize; n];
        for i in 0..n {
            a[i] = i;
        }
        a
    };

    let op = |a: &Vec<usize>, b: &Vec<usize>| -> Vec<usize> {
        let mut res = vec![0usize; n];
        for i in 0..n {
            res[i] = a[b[i]];
        }
        res
    };


    let pow = |a: &Vec<usize>, mut k: usize| -> Vec<usize> {
        let mut x = a.clone();
        let mut y = e();
        while k > 0 {
            if k & 1 == 1{
                y = op(&y, &x);
            }
            x = op(&x, &x);
            k >>= 1;
        }
        y
    };

    b = pow(&b, d);
    for x in b.iter() {
        writeln!(out, "{}", x + 1).unwrap();
    }

}
