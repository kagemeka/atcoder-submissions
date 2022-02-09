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
    type Matrix = Tensor<MyInt, 2>;
    let mut a = Matrix::new([k, 1]);
    let mut c = Matrix::new([k, k]);
    for i in 0..k {
        for j in 0..k { c[[i, j]] = <MyInt as AddIdentity>::e(); }
    }
    for i in 0..k {
        a[[k - 1 - i, 0]] = MyInt(sc.scan());
    }
    for i in 0..k {
        c[[0, i]] = MyInt(sc.scan());
    }
    for i in 0..k - 1 {
        c[[i + 1, i]] = <MyInt as MulIdentity>::e();
    }
    if m <= k {
        writeln!(out, "{}", a[[k - m, 0]].0).unwrap();
        return;
    }
    c = c.pow(m - k);
    a = c * a;
    writeln!(out, "{:?}", a[[0, 0]].0).unwrap();
}




pub mod structs {
    /// Fn(&S, &S) -> S is a trait.
    /// this is a dynamic size object at compilation time.
    /// thus, it's needed to be enclosed with Box<dyn> pointer.
    pub struct Monoid<S> {
        pub op: Box<dyn Fn(&S, &S) -> S>,
        pub e: Box<dyn Fn() -> S>,
        pub commutative: bool,
    }

    pub struct Semigroup<S> {
        pub op: Box<dyn Fn(&S, &S) -> S>,
        pub commutative: bool,
        pub idempotent: bool,
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

use traits::*;




impl Semiring for MyInt {
    const MUL_COMMUTATIVE: bool = true;
    const ADD_IDEMPOTNET: bool = false;
}

#[derive(Debug, Copy, Clone, Default)]
struct MyInt(usize);


impl std::ops::Mul for MyInt {
    type Output = Self;
    fn mul(self, rhs: Self) -> Self {
        Self(self.0 & rhs.0)
    }
}


impl std::ops::Add for MyInt {
    type Output = Self;
    fn add(self, rhs: Self) -> Self {
        Self(self.0 ^ rhs.0)
    }
}


impl AddIdentity for MyInt {
    fn e() -> Self { Self(0) }
}

impl MulIdentity for MyInt {
    fn e() -> Self { Self(std::usize::MAX) }
}


/// Tensor NDIM >= 1
/// references
/// - https://github.com/okayplanet/tensor/blob/master/src/tensor/mod.rs
/// - https://github.com/ecnerwala/cp-book/blob/master/src/tensor.hpp
#[derive(Clone)]
pub struct Tensor<T, const NDIM: usize> {
    shape: [usize; NDIM],
    strides: [usize; NDIM],
    size: usize,
    data: Vec<T>,
}


impl<T: std::fmt::Debug, const NDIM: usize> std::fmt::Debug for Tensor<T, NDIM> {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        f.debug_struct("Tensor")
            .field("shape", &self.shape)
            .field("data", &self.data)
            .finish()
    }
}

impl<T: Clone + Default, const NDIM: usize> Tensor<T, NDIM> {
    pub fn new(shape: [usize; NDIM]) -> Self {
        let shape = shape.clone();
        let mut strides: [usize; NDIM] = shape;
        strides[NDIM - 1] = 1;
        for i in (1..NDIM).rev() {
            strides[i - 1] = strides[i] * shape[i];
        }
        let size: usize = strides[0] * shape[0];
        let data = vec![T::default(); size];
        Self { shape, strides, size, data }
    }
}

impl<T, const NDIM: usize> Tensor<T, NDIM> {
    fn flat_index(&self, index: [usize; NDIM]) -> usize {
        let mut idx = 0;
        for i in 0..NDIM {
            idx += index[i] * self.strides[i];
        }
        idx
    }
}

/// https://doc.rust-lang.org/std/ops/trait.Index.html
impl<T, const NDIM: usize> std::ops::Index<[usize; NDIM]> for Tensor<T, NDIM> {
    type Output = T;
    fn index(&self, index: [usize; NDIM]) -> &Self::Output {
        &self.data[self.flat_index(index)]
    }
}

/// https://doc.rust-lang.org/std/ops/trait.IndexMut.html
impl<T, const NDIM: usize> std::ops::IndexMut<[usize; NDIM]> for Tensor<T, NDIM> {
    fn index_mut(&mut self, index: [usize; NDIM]) -> &mut Self::Output {
        let idx = self.flat_index(index);
        &mut self.data[idx]
    }
}

impl<T> std::ops::Mul for Tensor<T, 2>
where
    T: Copy + Default + std::ops::Add<Output = T> + std::ops::Mul<Output = T>,
{
    type Output = Self;

    fn mul(self, rhs: Self) -> Self {
        assert_eq!(self.shape[1], rhs.shape[0]);
        let h = self.shape[0];
        let w = rhs.shape[1];
        let n = self.shape[1];
        let mut res = Self::new([h, w]);
        for i in 0..h {
            for j in 0..w {
                for k in 0..n {
                    res[[i, j]] = res[[i, j]] + self[[i, k]] * rhs[[k, j]];
                }
            }
        }
        res
    }
}

impl<T: Copy + Default + Semiring> Tensor<T, 2> {
    pub fn e(&self) -> Self {
        let (h, w) = (self.shape[0], self.shape[1]);
        let mut e = Self::new(self.shape);
        for i in 0..h {
            for j in 0..w {
                e[[i, j]] = self::AddIdentity::e();
            }
        }
        for i in 0..h { e[[i, i]] = self::MulIdentity::e(); }
        e

    }

    pub fn op(lhs: &Self, rhs: &Self) -> Self {
        assert_eq!(lhs.shape[1], rhs.shape[0]);
        let h = lhs.shape[0];
        let w = rhs.shape[1];
        let n = lhs.shape[1];
        let mut res = Self::new([h, w]);
        for i in 0..h {
            for j in 0..w {
                for k in 0..n {
                    res[[i, j]] = res[[i, j]] + lhs[[i, k]] * rhs[[k, j]];
                }
            }
        }
        res
    }

    pub fn pow(&self, n: usize) -> Self {
        assert_eq!(self.shape[0], self.shape[1]);
        if n == 0 { return self.e(); }
        let mut x = self.pow(n >> 1);
        x = Self::op(&x, &x);
        if n & 1 == 1 { x = Self::op(&x, self); }
        x
    }
}




pub fn pow<T: Monoid>(x: &T, n: usize) -> T {
    if n == 0 { return T::e(); }
    let mut y = pow(x, n >> 1);
    y = T::op(&y, &y);
    if n & 1 == 1 { y = T::op(&y, &x); }
    y
}


// use structs;
pub struct Power<T> {
    m: structs::Monoid<T>,
}

impl<T> Power<T> {
    pub fn new(m: structs::Monoid<T>) -> Self { Self { m } }

    pub fn r#do(&self, x: &T, n: usize) -> T{
        if n == 0 { return (self.m.e)(); }
        let mut y = self.r#do(x, n >> 1);
        y = (self.m.op)(&y, &y);
        if n & 1 == 1 { y = (self.m.op)(&y, &x); }
        y
    }
}
