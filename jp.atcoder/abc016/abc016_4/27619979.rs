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


    // let a = Vector { data: [1, 2] };
    // let b = Vector { data: [3, 4] };
    let ax: i64 = sc.scan();
    let ay: i64 = sc.scan();
    let bx: i64 = sc.scan();
    let by: i64 = sc.scan();
    let seg0 = LineSegment { v0: Vector { data: [ax, ay] }, v1: Vector { data: [ bx, by ] } };
    let n: usize = sc.scan();
    let mut x: Vec<i64> = Vec::with_capacity(n);
    let mut y: Vec<i64> = Vec::with_capacity(n);
    for i in 0..n {
        x.push(sc.scan());
        y.push(sc.scan());
    }
    let mut cnt = 0usize;
    for i in 0..n {
        let seg1 = LineSegment { v0: Vector { data: [x[i], y[i]] }, v1: Vector { data: [x[(i + 1) % n], y[(i + 1) % n]] } };
        if LineSegment::intersect(&seg0, &seg1) { cnt += 1; }
    }
    writeln!(out, "{}", 1 + cnt / 2).unwrap();

}


#[derive(Debug, Clone)]
pub struct Vector<T, const DIM: usize> {
    data: [T; DIM],
}


impl<T: Default + Copy, const DIM:usize> Default for Vector<T, DIM> {
    fn default() -> Self {
        Self { data: [T::default(); DIM] }
    }
}

impl<T: Default + Copy + std::ops::Add<Output=T>, const DIM: usize> std::ops::Add<Self> for Vector<T, DIM> {
    type Output = Self;
    fn add(self, rhs: Self) -> Self {
        let mut res = Self::default();
        for i in 0..DIM {
            res.data[i] = self.data[i] + rhs.data[i];
        }
        res
    }
}


impl<T: Default + Copy + std::ops::Sub<Output=T>, const DIM: usize> std::ops::Sub<Self> for Vector<T, DIM> {
    type Output = Self;
    fn sub(self, rhs: Self) -> Self {
        let mut res = Self::default();
        for i in 0..DIM {
            res.data[i] = self.data[i] - rhs.data[i];
        }
        res
    }
}


impl<T: Default + Copy + std::ops::Neg<Output=T>, const DIM: usize> std::ops::Neg for Vector<T, DIM> {
    type Output = Self;
    fn neg(self) -> Self {
        let mut res = Self::default();
        for i in 0..DIM {
            res.data[i] = -self.data[i];
        }
        res
    }
}


impl<T, const DIM: usize> Vector<T, DIM>
where
    T:  Copy + std::ops::Add<Output=T> + std::ops::Mul<Output=T>,
{
    pub fn inner_prod(&self, rhs: &Self) -> T {
        self.data.iter().zip(rhs.data).map(|(&x, y)| x * y).reduce(T::add).unwrap()
    }
}

impl<T: Copy + std::ops::Sub<Output=T> + std::ops::Mul<Output=T>> Vector<T, 2> {
    pub fn cross_prod(&self, rhs: &Self) -> T {
        self.data[0] * rhs.data[1] - self.data[1] * rhs.data[0]
    }
}


#[derive(Clone)]
pub struct LineSegment<T: Clone, const DIM: usize> {
    v0: Vector<T, DIM>,
    v1: Vector<T, DIM>,
}


impl LineSegment<i64, 2> {

    pub fn across(&self, rhs: &Self) -> bool {
        let v0 = rhs.v1.clone() - rhs.v0.clone();
        let v1 = self.v0.clone() - rhs.v0.clone();
        let v2 = self.v1.clone() - rhs.v0.clone();
        v0.cross_prod(&v1) * v0.cross_prod(&v2) <= 0
    }


    pub fn intersect(lhs: &Self, rhs: &Self) -> bool {
        lhs.across(rhs) && rhs.across(lhs)
    }
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
