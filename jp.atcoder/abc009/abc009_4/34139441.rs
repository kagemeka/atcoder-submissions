pub fn read<T: std::str::FromStr>() -> T {
    use std::io::Read;
    std::io::stdin()
        .lock()
        .by_ref()
        .bytes()
        .map(|c| c.unwrap() as char)
        .skip_while(|c| c.is_whitespace())
        .take_while(|c| !c.is_whitespace())
        .collect::<String>()
        .parse::<T>()
        .ok()
        .unwrap()
}
pub mod matrix_frequent {
    pub trait Shape {
        fn shape() -> (usize, usize);
    }
    pub trait Size {
        fn size() -> usize;
    }
    impl<P: Size> Shape for P {
        fn shape() -> (usize, usize) { (Self::size(), Self::size()) }
    }
    use std::{marker::PhantomData, ops::*};
    #[derive(Debug, Clone, Eq, PartialEq)]
    pub struct Matrix<T, P>(pub Vec<Vec<T>>, PhantomData<P>);
    impl<T: Clone, P: Shape> Matrix<T, P> {
        pub fn new(fill_value: T) -> Self {
            let (h, w) = P::shape();
            Self(vec![vec![fill_value; w]; h], PhantomData)
        }
    }
    impl<T: Clone + Default, P: Shape> Default for Matrix<T, P> {
        fn default() -> Self { Self::new(T::default()) }
    }
    impl<T, P> Index<usize> for Matrix<T, P> {
        type Output = [T];

        fn index(&self, i: usize) -> &Self::Output { &self.0[i] }
    }
    impl<T, P> IndexMut<usize> for Matrix<T, P> {
        fn index_mut(&mut self, i: usize) -> &mut Self::Output {
            &mut self.0[i]
        }
    }
    impl<T, P: Shape> From<Vec<Vec<T>>> for Matrix<T, P> {
        fn from(data: Vec<Vec<T>>) -> Self {
            let (h, w) = P::shape();
            assert_eq!(h, data.len());
            for i in 0..h {
                assert_eq!(data[i].len(), w);
            }
            Self(data, PhantomData)
        }
    }
    impl<T, P> Add for Matrix<T, P>
    where
        P: Shape,
        T: AddAssign + Clone + From<i32>,
    {
        type Output = Self;

        fn add(mut self, rhs: Self) -> Self::Output {
            let (h, w) = P::shape();
            for i in 0..h {
                for j in 0..w {
                    self[i][j] += rhs[i][j].clone();
                }
            }
            self
        }
    }
    impl<T, P> AddAssign for Matrix<T, P>
    where
        P: Shape + Clone,
        T: AddAssign + Clone + From<i32>,
    {
        fn add_assign(&mut self, rhs: Self) { *self = self.clone() + rhs; }
    }
    impl<T, P> From<i32> for Matrix<T, P>
    where
        P: Size,
        T: Mul<Output = T> + AddAssign + Clone + From<i32>,
    {
        fn from(x: i32) -> Self {
            assert!(x == 0 || x == 1);
            let n = P::size();
            let mut a = Self::new(0.into());
            if x == 1 {
                for i in 0..n {
                    a[i][i] = 1.into();
                }
            }
            a
        }
    }
    impl<T, P> Mul for Matrix<T, P>
    where
        P: Size,
        T: Mul<Output = T> + AddAssign + Clone + From<i32>,
    {
        type Output = Self;

        fn mul(self, rhs: Self) -> Self::Output {
            let n = P::size();
            let mut a = Self::new(0.into());
            for i in 0..n {
                for k in 0..n {
                    for j in 0..n {
                        a[i][j] += self[i][k].clone() * rhs[k][j].clone();
                    }
                }
            }
            a
        }
    }
    impl<T, P> MulAssign for Matrix<T, P>
    where
        P: Size + Clone,
        T: Mul<Output = T> + AddAssign + Clone + From<i32>,
    {
        fn mul_assign(&mut self, rhs: Self) { *self = self.clone() * rhs; }
    }
    pub fn power<T, N>(mut x: T, mut n: N) -> T
    where
        T: Clone + MulAssign + From<i32>,
        N: From<i32>
            + Ord
            + SubAssign
            + ShrAssign<usize>
            + BitAnd<Output = N>
            + Copy,
    {
        let zero = 0.into();
        let one = 1.into();
        assert!(n >= zero);
        let mut y = 1.into();
        while n > zero {
            if n & one == one {
                y *= x.clone();
            }
            x *= x.clone();
            n >>= 1;
        }
        y
    }
    #[derive(Debug, Clone)]
    pub struct Prop100;
    impl Size for Prop100 {
        fn size() -> usize { 100 }
    }
    pub type Mat100<T> = Matrix<T, Prop100>;
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    use matrix_frequent::*;
    #[derive(Debug, Clone)]
    struct R(usize);
    impl From<i32> for R {
        fn from(x: i32) -> Self {
            assert!(x == 0 || x == 1);
            Self(x as usize * std::usize::MAX)
        }
    }
    use std::ops::*;
    impl Add for R {
        type Output = Self;

        fn add(mut self, rhs: Self) -> Self::Output {
            self.0 ^= rhs.0;
            self
        }
    }
    impl AddAssign for R {
        fn add_assign(&mut self, rhs: Self) { *self = self.clone() + rhs; }
    }
    impl Mul for R {
        type Output = Self;

        fn mul(mut self, rhs: Self) -> Self::Output {
            self.0 &= rhs.0;
            self
        }
    }
    type M = Mat100<R>;
    let n: usize = read();
    let m: usize = read();
    let mut a: M = 0.into();
    for i in 0..n {
        a[n - 1 - i][0] = R(read());
    }
    let mut b: M = 0.into();
    for i in 0..n {
        b[0][i] = R(read());
    }
    for i in 0..n - 1 {
        b[i + 1][i] = R(std::usize::MAX);
    }
    b = power(b, (m - 1) as i64);
    a = b * a;
    writeln!(writer, "{}", a[n - 1][0].0).unwrap();
}
