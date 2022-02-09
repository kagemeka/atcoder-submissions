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
    let d: usize = sc.scan();
    let mut x = sc.scan::<isize>().abs() as usize;
    let mut y = sc.scan::<isize>().abs() as usize;
    if x % d != 0 || y % d != 0 {
        writeln!(out, "{}", 0).unwrap();
        return;
    }
    x /= d;
    y /= d;
    if n < x + y || (n - x - y) & 1 == 1 {
        writeln!(out, "{}", 0).unwrap();
        return;
    }
    let p = pascal::<Num>(1 << 10);

    let mut res: f64 = 0.;
    for k in 0..(n - x - y) / 2 + 1 {
        let d = k;
        let u = y + d;
        let l = (n - x - y) / 2 - k;
        let r = x + l;
        res += p[n][u].0 * p[n - u][d].0 * p[n - u - d][l].0 * p[n - u - d - l][r].0;
    }
    writeln!(out, "{:0.10}", res).unwrap();
}

#[derive(Debug, Clone, Copy, Default)]
pub struct Num(f64);


impl traits::AddIdentity for Num {
    fn e() -> Self { Self(0.) }
}


impl traits::MulIdentity for Num {
    fn e() -> Self { Self(1.) }
}

impl std::ops::Add for Num {
    type Output = Self;
    fn add(self, rhs: Self) -> Self {
        Self(self.0 + rhs.0 / 4f64)
    }
}

impl std::ops::Mul for Num {
    type Output = Self;
    fn mul(self, rhs: Self) -> Self {
        Self(self.0 * rhs.0)
    }
}

impl traits::Semiring for Num {
    const MUL_COMMUTATIVE: bool = false;
    const ADD_IDEMPOTNET: bool = false;
}



pub mod traits {
    pub trait Identity { fn e() -> Self; }
    pub trait Inverse { fn inv(&self) -> Self;}
    pub trait Semigroup {
        fn op(_: &Self, _: &Self) -> Self;
        const COMMUTATIVE: bool;
        const IDEMPOTENT: bool;
    }

    pub trait Monoid: Semigroup + Identity {}
    pub trait Group: Monoid + Inverse {}
    pub trait MulIdentity { fn e() -> Self; }

    pub trait AddIdentity { fn e() -> Self;}
    pub trait AddInverse { fn inv(&self) -> Self; }
    pub trait MulInverse { fn inv(&self) -> Self; }
    pub trait Semiring: Sized + std::ops::Add<Output=Self> + std::ops::Mul<Output=Self> + AddIdentity + MulIdentity {
        const MUL_COMMUTATIVE: bool;
        const ADD_IDEMPOTNET: bool;
    }
    pub trait Ring: Semiring + AddInverse {}

}


pub fn pascal<T: Copy + Default + traits::Semiring>(n: usize) -> Vec<Vec<T>> {
    let mut p: Vec<Vec<T>> = vec![vec![<T as traits::AddIdentity>::e(); n]; n];
    for i in 0..n { p[i][0] = <T as traits::MulIdentity>::e(); }
    for i in 1..n {
        for j in 1..i + 1 {
            p[i][j] = p[i - 1][j] + p[i - 1][j - 1];
        }
    }
    p
}
