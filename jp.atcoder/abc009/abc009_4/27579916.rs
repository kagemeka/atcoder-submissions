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

    let k: usize = sc.scan();
    let m: usize = sc.scan();
    let mut a = vec![vec![0usize]; k];
    for i in 0..k {
        a[k - 1 - i][0] = sc.scan();
    }

    fn op(lhs: &Vec<Vec<usize>>, rhs: &Vec<Vec<usize>>) -> Vec<Vec<usize>> {
        let n = lhs[0].len();
        let h = lhs.len();
        assert_eq!(rhs.len(), n);
        let w = rhs[0].len();
        let mut res = vec![vec![0usize; w]; h];
        for i in 0..h {
            for j in 0..w {
                for k in 0..n {
                    res[i][j] ^= lhs[i][k] & rhs[k][j];
                }
            }
        }
        res
    }

    let e = || {
        let mut a = vec![vec![0usize; k]; k];
        for i in 0..k {
            a[i][i] = std::usize::MAX;
        }
        a
    };

    let mon = structs::Monoid {
        op: &op,
        e: &e,
        commutative: false,
        idempotent: false,
    };
    let pow = Power::new(mon);


    let mut c = vec![vec![0usize; k]; k];
    for i in 0..k {
        c[0][i] = sc.scan();
    }
    for i in 0..k - 1 {
        c[i + 1][i] = std::usize::MAX;
    }
    if m <= k {
        writeln!(out, "{}", a[k - m][0]).unwrap();
        return;
    }
    c = pow.r#do(&c, m - k);
    a = op(&c, &a);
    writeln!(out, "{}", a[0][0]).unwrap();

}

pub mod structs {
    /// Fn(&S, &S) -> S is a trait.
    /// this is a dynamic size object at compilation time.
    /// thus, it's needed to be enclosed with Box<dyn> pointer.
    pub struct Monoid<'a, S> {
        pub op: &'a dyn Fn(&S, &S) -> S,
        pub e: &'a dyn Fn() -> S,
        pub commutative: bool,
        pub idempotent: bool,
    }

    pub struct Semigroup<S> {
        pub op: Box<dyn Fn(&S, &S) -> S>,
        pub commutative: bool,
        pub idempotent: bool,
    }
}

// use structs;
pub struct Power<'a, T> {
    m: structs::Monoid<'a, T>,
}

impl<'a, T> Power<'a, T> {
    pub fn new(m: structs::Monoid<'a, T>) -> Self { Self { m } }

    pub fn r#do(&self, x: &T, n: usize) -> T{
        if n == 0 { return (self.m.e)(); }
        let mut y = self.r#do(x, n >> 1);
        y = (self.m.op)(&y, &y);
        if n & 1 == 1 { y = (self.m.op)(&y, &x); }
        y
    }
}
