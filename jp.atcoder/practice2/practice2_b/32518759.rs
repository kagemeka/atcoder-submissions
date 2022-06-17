pub struct ReadWrapper<R> {
    reader: R,
    tokens: Vec<String>,
}

impl<R> ReadWrapper<R> {
    pub fn new(reader: R) -> Self { Self { reader, tokens: vec![] } }
}

impl<R: std::io::BufRead> ReadWrapper<R> {
    pub fn read<T: std::str::FromStr>(
        &mut self,
    ) -> Result<T, <T as std::str::FromStr>::Err> {
        while self.tokens.is_empty() {
            let mut buf = String::new();
            self.reader.read_line(&mut buf).unwrap();
            self.tokens =
                buf.split_whitespace().map(str::to_string).rev().collect();
        }
        self.tokens.pop().unwrap().parse::<T>()
    }
}

pub fn locked_stdin_reader() -> ReadWrapper<std::io::StdinLock<'static>> {
    let stdin = Box::leak(Box::new(std::io::stdin()));
    ReadWrapper::new(stdin.lock())
}

pub fn locked_stdout_buf_writer()
-> std::io::BufWriter<std::io::StdoutLock<'static>> {
    let stdout = Box::leak(Box::new(std::io::stdout()));
    std::io::BufWriter::new(stdout.lock())
}

/// reference
/// https://users.rust-lang.org/t/show-value-only-in-debug-mode/43686/3
#[macro_export]
#[allow(unused_macros)]
macro_rules! debug {
    ($($x:tt)*) => {
        {
            // default in debug mode
            #[cfg(debug_assertions)]
            {
                std::dbg!($($x)*)
            }

            // default in release mode
            #[cfg(not(debug_assertions))]
            {
                ($($x)*)
            }
        }
    }
}

#[macro_export]
#[allow(unused_macros)]
macro_rules! write_vec {
    ($writer:ident, $values:expr) => {
        write_vec!($writer, $values, sep: ' ');
    };

    ($writer:ident, $values:expr,sep: $sep:expr) => {
        let n = $values.len();
        if n == 0 {
            writeln!($writer).unwrap();
        } else {
            for i in 0..n - 1 {
                write!(
                    $writer,
                    "{}{}",
                    $values[i], $sep
                )
                .unwrap();
            }
            writeln!($writer, "{}", $values[n - 1]).unwrap();
        }
    };
}

#[macro_export]
#[allow(unused_macros)]
macro_rules! write_all {
    ($writer:ident) => {
        writeln!($writer).unwrap();
    };

    ($writer:ident, $v:expr) => {
        writeln!($writer, "{}", $v).unwrap();
    };

    ($writer:ident, $v:expr, $($values:expr),+) => {
        write!($writer, "{} ", $v).unwrap();
        write_all!($writer, $($values),*);
    };
}

#[macro_export]
#[allow(unused_macros)]
macro_rules! read_vec {
    ($reader:ident, $type:ty, $n:expr) => {
        (0..$n)
            .map(|_| $reader.read::<$type>())
            .collect::<Result<Vec<_>, _>>()
            .unwrap()
    };
}

// TODO: main
// #[allow(warnings)]
fn main() -> Result<(), Box<dyn std::error::Error>> {
    use std::io::Write;
    let mut reader = locked_stdin_reader();
    let mut writer = locked_stdout_buf_writer();

    use algebraic_structure_impl::*;
    use fenwick::*;
    use group_theory_id::*;

    type Fw = Fenwick<GroupApprox<i64, Additive>>;

    let n: usize = reader.read()?;
    let q: usize = reader.read()?;

    let a = (0..n)
        .map(|_| reader.read::<i64>().unwrap())
        .collect::<Vec<_>>();

    let mut fw = Fw::new(a);

    for _ in 0..q {
        let t: usize = reader.read()?;
        let i: usize = reader.read()?;
        let j: usize = reader.read()?;

        if t == 0 {
            fw.operate(i, j as i64);
        } else {
            writeln!(writer, "{}", fw.reduce(i, j))?;
        }
    }

    writer.flush()?;
    Ok(())
}

pub mod uf {
    //! Disjoint-Set-Union (DSU) or Union-Find (UF).

    pub trait Root {
        fn root(&mut self, u: usize) -> usize;
    }

    trait Size {
        fn size(&self) -> usize;
    }

    pub trait Unite {
        fn unite(&mut self, u: usize, v: usize);
    }

    pub trait SizeOf {
        fn size_of(&mut self, u: usize) -> usize;
    }

    pub trait Same {
        fn same(&mut self, u: usize, v: usize) -> bool;
    }

    impl<U: Root> Same for U {
        fn same(&mut self, u: usize, v: usize) -> bool {
            self.root(u) == self.root(v)
        }
    }

    pub trait Labels {
        fn labels(&mut self) -> Vec<usize>;
    }

    impl<U: Root + Size> Labels for U {
        /// same label -> same component.
        fn labels(&mut self) -> Vec<usize> {
            let n = self.size();
            let mut label = vec![n; n];
            let mut l = 0;
            for i in 0..n {
                let r = self.root(i);
                if label[r] == n {
                    label[r] = l;
                    l += 1;
                }
                label[i] = label[r];
            }
            label
        }
    }

    #[derive(Debug)]
    pub struct UF {
        a: Vec<isize>, // neg-size or parent
    }

    impl UF {
        pub fn new(size: usize) -> Self { Self { a: vec![-1; size] } }
    }

    impl Size for UF {
        fn size(&self) -> usize { self.a.len() }
    }

    impl Root for UF {
        fn root(&mut self, u: usize) -> usize {
            if self.a[u] < 0 {
                return u;
            }
            self.a[u] = self.root(self.a[u] as usize) as isize;
            self.a[u] as usize
        }
    }

    impl Unite for UF {
        fn unite(&mut self, u: usize, v: usize) {
            let mut u = self.root(u);
            let mut v = self.root(v);
            if u == v {
                return;
            }
            if self.a[u] > self.a[v] {
                std::mem::swap(&mut u, &mut v);
            }
            self.a[u] += self.a[v];
            self.a[v] = u as isize;
        }
    }

    impl SizeOf for UF {
        /// size of the component containing u
        fn size_of(&mut self, u: usize) -> usize {
            let u = self.root(u);
            -self.a[u] as usize
        }
    }

    use crate::algebraic_structure::*;
    pub struct PotentialUF<G: AbelianGroup> {
        a: Vec<isize>, // neg-size or parent
        rp: Vec<G::S>, // relative potential from parent
    }

    impl<G: AbelianGroup> Size for PotentialUF<G> {
        fn size(&self) -> usize { self.a.len() }
    }

    impl<G> PotentialUF<G>
    where
        G: AbelianGroup,
        G::S: Clone,
    {
        pub fn new(size: usize) -> Self {
            Self {
                a: vec![-1; size],
                rp: (0..size).map(|_| G::e()).collect(),
            }
        }

        /// relative potential from the root.
        fn h(&mut self, u: usize) -> G::S {
            self.root(u);
            self.rp[u].clone()
        }

        /// potential v against u.
        pub fn diff(
            &mut self,
            u: usize,
            v: usize,
        ) -> Result<G::S, &'static str> {
            if self.root(u) != self.root(v) {
                Err("different components")
            } else {
                Ok(G::op(
                    G::inv(self.h(u)),
                    self.h(v),
                ))
            }
        }

        pub fn unite(
            &mut self,
            mut u: usize,
            mut v: usize,
            d: G::S, // potential v against u
        ) where
            G::S: PartialEq,
        {
            let mut d = G::op(
                G::op(self.h(u), d),
                G::inv(self.h(v).clone()),
            );
            u = self.root(u);
            v = self.root(v);
            if u == v {
                debug_assert!(d == G::e());
                return;
            }
            if self.a[u] > self.a[v] {
                std::mem::swap(&mut u, &mut v);
                d = G::inv(d);
            }
            self.a[u] += self.a[v];
            self.a[v] = u as isize;
            self.rp[v] = d;
        }
    }

    impl<G> Root for PotentialUF<G>
    where
        G: AbelianGroup,
        G::S: Clone,
    {
        fn root(&mut self, u: usize) -> usize {
            if self.a[u] < 0 {
                return u;
            }
            let p = self.a[u] as usize;
            self.a[u] = self.root(p) as isize;
            self.rp[u] = G::op(
                self.rp[u].clone(),
                self.rp[p].clone(),
            );
            self.a[u] as usize
        }
    }

    impl<G> SizeOf for PotentialUF<G>
    where
        G: AbelianGroup,
        G::S: Clone,
    {
        fn size_of(&mut self, u: usize) -> usize
        where
            G::S: Clone,
        {
            let u = self.root(u);
            -self.a[u] as usize
        }
    }

    // TODO:
    pub struct RollbackUF {}

    // TODO:
    pub struct PersitentUF {}

    #[cfg(test)]
    mod tests {
        use super::*;
        #[test]
        fn test_uf() {
            let mut uf = UF::new(10);
            assert_eq!(uf.size_of(0), 1);
            uf.unite(3, 9);
            assert_eq!(uf.size_of(3), 2);
        }

        #[test]
        fn test_potential_uf() {
            use crate::{
                algebraic_structure_impl::*,
                group_theory_id::Additive,
            };
            let mut uf = PotentialUF::<GroupApprox<i32, Additive>>::new(6);
            assert_eq!(uf.size_of(0), 1);
            assert!(uf.diff(0, 5).is_err());
            uf.unite(0, 1, 1);
            uf.unite(5, 4, 2);
            uf.unite(1, 2, 3);
            uf.unite(4, 3, 4);
            uf.unite(2, 3, 5);
            assert_eq!(uf.size_of(4), 6);
            assert_eq!(uf.diff(0, 5), Ok(3));
        }
    }
}

pub mod group_theory_id {
    // TODO: rename group_theory_id -> binary_operation_id
    pub struct Additive;
    pub struct Multiplicative;

    pub struct Xor;
    pub struct GCD;
    pub struct LCM;
    pub struct Min;
    pub struct Max;
}

pub mod algebraic_structure_impl {
    use crate::{binary_function::*, group_theory_id::*};

    /// ((usize, usize), min)
    pub struct GroupApprox<S, I>(std::marker::PhantomData<(S, I)>);

    impl BinaryOp for GroupApprox<(usize, usize), Min> {
        type S = (usize, usize);

        fn op(lhs: Self::S, rhs: Self::S) -> Self::S { lhs.min(rhs) }
    }

    impl Idempotence for GroupApprox<(usize, usize), Min> {}

    impl Commutative for GroupApprox<(usize, usize), Min> {}

    impl Associative for GroupApprox<(usize, usize), Min> {}

    impl Identity for GroupApprox<(usize, usize), Min> {
        fn e() -> Self::S {
            (
                std::usize::MAX,
                std::usize::MAX,
            )
        }
    }

    /// (usize, min)
    impl BinaryOp for GroupApprox<usize, Min> {
        type S = usize;

        fn op(lhs: usize, rhs: usize) -> usize { lhs.min(rhs) }
    }

    impl Idempotence for GroupApprox<usize, Min> {}

    impl Commutative for GroupApprox<usize, Min> {}

    impl Associative for GroupApprox<usize, Min> {}

    impl Identity for GroupApprox<usize, Min> {
        fn e() -> Self::S { std::usize::MAX }
    }

    /// (usize, +)
    impl BinaryOp for GroupApprox<usize, Additive> {
        type S = usize;

        fn op(lhs: usize, rhs: usize) -> usize { lhs + rhs }
    }

    impl Associative for GroupApprox<usize, Additive> {}

    impl Commutative for GroupApprox<usize, Additive> {}

    impl Identity for GroupApprox<usize, Additive> {
        fn e() -> Self::S { 0 }
    }

    /// (i32, +)
    impl BinaryOp for GroupApprox<i32, Additive> {
        type S = i32;

        fn op(lhs: i32, rhs: i32) -> i32 { lhs + rhs }
    }

    impl Associative for GroupApprox<i32, Additive> {}

    impl Commutative for GroupApprox<i32, Additive> {}

    impl Identity for GroupApprox<i32, Additive> {
        fn e() -> Self::S { 0 }
    }

    impl Inverse for GroupApprox<i32, Additive> {
        fn inv(x: i32) -> i32 { -x }
    }

    /// (u64, +)
    impl BinaryOp for GroupApprox<u64, Additive> {
        type S = u64;

        fn op(lhs: Self::S, rhs: Self::S) -> Self::S { lhs + rhs }
    }

    impl Commutative for GroupApprox<u64, Additive> {}

    impl Associative for GroupApprox<u64, Additive> {}

    impl Identity for GroupApprox<u64, Additive> {
        fn e() -> Self::S { 0 }
    }

    /// (i64, +)
    impl BinaryOp for GroupApprox<i64, Additive> {
        type S = i64;

        fn op(lhs: Self::S, rhs: Self::S) -> Self::S { lhs + rhs }
    }

    impl Commutative for GroupApprox<i64, Additive> {}

    impl Associative for GroupApprox<i64, Additive> {}

    impl Identity for GroupApprox<i64, Additive> {
        fn e() -> Self::S { 0 }
    }

    impl Inverse for GroupApprox<i64, Additive> {
        fn inv(x: i64) -> i64 { -x }
    }
}

pub mod binary_function {
    //! binary function
    pub trait BinaryFunc {
        type L;
        type R;
        type Cod;
        fn f(_: Self::L, _: Self::R) -> Self::Cod;
    }

    /// external binary operation
    pub trait ExtBinaryOp: BinaryFunc {}
    impl<T: BinaryFunc> ExtBinaryOp for T {}

    /// binary operation on a set.
    pub trait BinaryOp {
        type S;
        fn op(_: Self::S, _: Self::S) -> Self::S;
    }

    fn is_left_identity<S, F>(f: &F, e: S, x: S) -> bool
    where
        F: Fn(S, S) -> S,
        S: Clone + PartialEq,
    {
        f(e, x.clone()) == x
    }

    fn is_right_identity<S, F>(f: &F, e: S, x: S) -> bool
    where
        F: Fn(S, S) -> S,
        S: Clone + PartialEq,
    {
        f(x.clone(), e) == x
    }

    fn is_identity<S, F>(f: &F, e: S, x: S) -> bool
    where
        F: Fn(S, S) -> S,
        S: Clone + PartialEq,
    {
        is_left_identity(f, e.clone(), x.clone()) && is_right_identity(f, e, x)
    }

    /// identity element
    pub trait Identity: BinaryOp {
        fn e() -> Self::S;

        fn assert(x: Self::S)
        where
            Self::S: Clone + PartialEq,
        {
            assert!(is_identity(
                &Self::op,
                Self::e(),
                x
            ));
        }
    }

    fn is_invertible<F, G, X>(op: &F, inv: &G, e: X, x: X) -> bool
    where
        F: Fn(X, X) -> X,
        G: Fn(X) -> X,
        X: Clone + PartialEq,
    {
        op(x.clone(), inv(x.clone())) == e.clone()
            && op(inv(x.clone()), x.clone()) == e
    }

    /// inverse element
    pub trait Inverse: Identity {
        fn inv(_: Self::S) -> Self::S;

        fn assert(x: Self::S)
        where
            Self::S: Clone + PartialEq,
        {
            assert!(is_invertible(
                &Self::op,
                &Self::inv,
                Self::e(),
                x
            ));
        }
    }

    fn is_commutative<F, X, Y>(f: &F, a: X, b: X) -> bool
    where
        F: Fn(X, X) -> Y,
        X: Clone,
        Y: PartialEq,
    {
        f(a.clone(), b.clone()) == f(b, a)
    }

    /// commutative property
    pub trait Commutative: BinaryOp {
        fn assert(a: Self::S, b: Self::S)
        where
            Self::S: Clone + PartialEq,
        {
            assert!(is_commutative(&Self::op, a, b));
        }
    }

    fn is_associative<F, X>(f: &F, a: X, b: X, c: X) -> bool
    where
        F: Fn(X, X) -> X,
        X: Clone + PartialEq,
    {
        f(
            f(a.clone(), b.clone()),
            c.clone(),
        ) == f(a, f(b, c))
    }
    /// associative property
    pub trait Associative: BinaryOp {
        fn assert(x: Self::S, y: Self::S, z: Self::S)
        where
            Self::S: Clone + PartialEq,
        {
            assert!(is_associative(
                &Self::op,
                x,
                y,
                z
            ));
        }
    }

    fn is_idempotent<F, X>(f: &F, x: X) -> bool
    where
        F: Fn(X, X) -> X,
        X: Clone + PartialEq,
    {
        f(x.clone(), x.clone()) == x
    }

    pub trait Idempotence: BinaryOp {
        fn assert(x: Self::S)
        where
            Self::S: Clone + PartialEq,
        {
            assert!(is_idempotent(&Self::op, x));
        }
    }

    /// latain square property
    pub trait LatinSquare: BinaryOp {}

    impl<T: Inverse> LatinSquare for T {}

    // TODO: assertion latin square

    fn is_left_absorbing<F, X>(f: &F, z: X, x: X) -> bool
    where
        F: Fn(X, X) -> X,
        X: Clone + PartialEq,
    {
        f(z.clone(), x) == z
    }

    fn is_right_absorbing<F, X>(f: &F, z: X, x: X) -> bool
    where
        F: Fn(X, X) -> X,
        X: Clone + PartialEq,
    {
        f(x, z.clone()) == z
    }

    fn is_absorbing<F, X>(f: &F, z: X, x: X) -> bool
    where
        F: Fn(X, X) -> X,
        X: Clone + PartialEq,
    {
        is_left_absorbing(f, z.clone(), x.clone())
            && is_right_absorbing(f, z, x)
    }

    /// absorbing element
    pub trait Absorbing: BinaryOp {
        fn z() -> Self::S;

        fn assert(x: Self::S)
        where
            Self::S: Clone + PartialEq,
        {
            assert!(is_absorbing(
                &Self::op,
                Self::z(),
                x
            ));
        }
    }

    pub trait Add {
        type S;
        fn add(_: Self::S, _: Self::S) -> Self::S;
    }

    pub trait Mul: Add {
        fn mul(_: Self::S, _: Self::S) -> Self::S;
    }

    fn iz_zero<F, X>(mul: &F, z: X, x: X) -> bool
    where
        F: Fn(X, X) -> X,
        X: Clone + PartialEq,
    {
        is_absorbing(mul, z, x)
    }

    pub trait Zero: Mul {
        fn zero() -> Self::S;

        fn assert(x: Self::S)
        where
            Self::S: Clone + PartialEq,
        {
            assert!(iz_zero(
                &Self::mul,
                Self::zero(),
                x
            ));
        }
    }

    pub trait One: Mul {
        fn one() -> Self::S;
    }

    pub trait AddInv: Add {
        fn add_inv(_: Self::S) -> Self::S;
    }

    pub trait MulInv: Mul {
        fn mul_inv(_: Self::S) -> Self::S;
    }

    fn is_left_distributive<Add, Mul, X>(
        add: &Add,
        mul: &Mul,
        x: X,
        y: X,
        z: X,
    ) -> bool
    where
        Add: Fn(X, X) -> X,
        Mul: Fn(X, X) -> X,
        X: Clone + PartialEq,
    {
        mul(
            x.clone(),
            add(y.clone(), z.clone()),
        ) == add(mul(x.clone(), y), mul(x, z))
    }

    fn is_right_distributive<Add, Mul, X>(
        add: &Add,
        mul: &Mul,
        y: X,
        z: X,
        x: X,
    ) -> bool
    where
        Add: Fn(X, X) -> X,
        Mul: Fn(X, X) -> X,
        X: Clone + PartialEq,
    {
        mul(
            add(y.clone(), z.clone()),
            x.clone(),
        ) == add(mul(y, x.clone()), mul(z, x))
    }

    fn is_distributive<Add, Mul, X>(
        add: &Add,
        mul: &Mul,
        x: X,
        y: X,
        z: X,
    ) -> bool
    where
        Add: Fn(X, X) -> X,
        Mul: Fn(X, X) -> X,
        X: Clone + PartialEq,
    {
        is_left_distributive(
            add,
            mul,
            x.clone(),
            y.clone(),
            z.clone(),
        ) && is_right_distributive(add, mul, y, z, x)
    }

    pub trait Distributive: Mul {
        fn assert(x: Self::S, y: Self::S, z: Self::S)
        where
            Self::S: Clone + PartialEq,
        {
            assert!(is_distributive(
                &Self::mul,
                &Self::add,
                x,
                y,
                z
            ));
        }
    }

    pub mod dynamic {
        pub trait BinaryOp {
            type S;
            fn op(&self, _: Self::S, _: Self::S) -> Self::S;
        }
    }

    pub mod itself {
        pub trait Id {}
        impl<T> Id for T {}

        pub trait BinaryOp<I: Id> {
            fn op(_: Self, _: Self) -> Self;
        }
    }
}

pub mod algebraic_structure {
    use crate::binary_function::*;

    pub trait Magma: BinaryOp {}

    impl<T: BinaryOp> Magma for T {}

    pub trait Semigroup: Magma + Associative {}

    impl<T: Magma + Associative> Semigroup for T {}

    pub trait Monoid: Semigroup + Identity {}

    impl<T> Monoid for T where T: Semigroup + Identity {}

    pub trait UnitalMagma: Magma + Identity {}

    impl<T: Magma + Identity> UnitalMagma for T {}

    pub trait Quasigroup: Magma + LatinSquare {}

    impl<T: Magma + LatinSquare> Quasigroup for T {}

    pub trait Loop: Quasigroup + Identity {}

    impl<T: Quasigroup + Identity> Loop for T {}

    pub trait Group: Monoid + Inverse {}

    impl<T: Monoid + Inverse> Group for T {}

    pub trait AbelianGroup: Group + Commutative {}

    impl<T: Group + Commutative> AbelianGroup for T {}

    pub trait Semiring: Zero + One + Distributive {}

    impl<T: Zero + One + Distributive> Semiring for T {}

    pub trait Ring: Semiring + AddInv {}

    impl<T: Semiring + AddInv> Ring for T {}

    pub mod dynamic {
        use crate::binary_function::dynamic::*;
        pub trait Magma: BinaryOp {}

        impl<T: BinaryOp> Magma for T {}
    }

    pub mod itself {
        use crate::binary_function::itself::*;

        pub trait Magma<I: Id>: BinaryOp<I> {}

        impl<I, T> Magma<I> for T
        where
            T: BinaryOp<I>,
            I: Id,
        {
        }
    }
}

pub mod bitops {
    /// count leading zeros
    /// why L is asccociated variable rather than fixed u8?
    /// > due to big integer.
    pub trait CLZ {
        type L;

        fn clz(self) -> Self::L;
    }

    /// count trailing zeros
    pub trait CTZ {
        type L;

        fn ctz(self) -> Self::L;
    }

    /// this is not usually abbreviated as CLO unlike CLZ.
    pub trait CountLeadingOnes {
        type L;

        fn leading_ones(self) -> Self::L;
    }

    pub trait CountTrailingOnes {
        type L;

        fn trailing_ones(self) -> Self::L;
    }

    pub trait CountZeros {
        type L;

        fn count_zeros(self) -> Self::L;
    }

    pub trait CountOnes {
        type L;

        fn count_ones(self) -> Self::L;
    }

    /// bit scan reverse
    pub trait BSR {
        type L;

        fn bsr(self) -> Self::L;
    }

    /// bit scan forward
    pub trait BSF {
        type L;

        fn bsf(self) -> Self::L;
    }

    pub mod len {
        /// O(1)
        pub fn with_clz(n: u64) -> u8 {
            (0u64.leading_zeros() - n.leading_zeros()) as u8
        }

        pub fn with_clz_128(n: u128) -> u8 {
            (0u128.leading_zeros() - n.leading_zeros()) as u8
        }

        /// O(\log\log{N}})
        pub fn binary_search(mut n: u64) -> u8 {
            let mut l = 0;
            for i in (0..6).rev() {
                let d = 1 << i;
                if n >> d > 0 {
                    n >>= d;
                    l += d;
                }
            }
            if n == 1 {
                l += 1;
                n -= 1;
            }
            debug_assert_eq!(n, 0);
            l
        }

        /// O(\log{N})
        pub fn naive(mut n: u64) -> u8 {
            let mut l = 0;
            while n > 0 {
                n >>= 1;
                l += 1;
            }
            l
        }

        /// O(N)
        pub fn table(size: usize) -> Vec<u8> {
            let mut l = vec![0; size];
            for i in 1..size {
                l[i] = l[i >> 1] + 1;
            }
            l
        }
    }

    /// just alias of count_ones.
    pub trait Popcount: CountOnes {}

    impl<T: CountOnes> Popcount for T {}

    pub mod popcount {
        /// O(1)
        pub fn with_std(n: u64) -> u8 { n.count_ones() as u8 }

        /// O(\log\log{N})
        pub fn divide_conquer(mut n: u64) -> u8 {
            const M0: u64 = 0x5555555555555555; // 0b0101...
            const M1: u64 = 0x3333333333333333; // 0b0011...
            const M2: u64 = 0x0f0f0f0f0f0f0f0f; // 0b00001111...
            n -= (n >> 1) & M0;
            // = (n & M0) + ((n >> 1) & M0);
            n = (n & M1) + ((n >> 2) & M1);
            n = (n + (n >> 4)) & M2;
            // = (n & M2) + ((n >> 4) & M2)
            // k = 4, 2k < 2^k
            n += n >> 8;
            // it's only enough to mask at last.
            // popcount <= 64 = 7bits < 8.
            n += n >> 16;
            n += n >> 32;
            return (n & 0x7f) as u8;
        }

        /// O(\log{N})
        pub fn naive(mut n: u64) -> u8 {
            let mut c = 0;
            while n > 0 {
                c += (n & 1) as u8;
                n >>= 1
            }
            c
        }

        /// O(N)
        pub fn table(size: usize) -> Vec<u8> {
            let mut count = vec![0; size];
            for i in 1..size {
                count[i] = count[i >> 1] + (i & 1) as u8;
            }
            count
        }

        #[cfg(test)]
        mod tests {
            #[test]
            fn test() {}
        }
    }

    pub trait Inverse {
        fn invert(self) -> Self;
    }

    /// equivalent to (2^k - 1) ^ n for k bit integer.
    pub fn invert<T: std::ops::Not<Output = T>>(n: T) -> T { !n }

    pub trait Reverse {
        fn reverse(self) -> Self;
    }

    /// TODO: not implemented.
    pub fn reverse() {}

    pub trait ShrUntilOdd {
        fn shr_until_odd(self) -> Self;
    }

    /// shift right
    pub fn shr_until_odd(n: u64) -> u64 {
        assert!(n > 0);
        n >> n.trailing_zeros()
    }

    /// most significant bit
    /// O(1)
    pub fn msb(n: u64) -> usize {
        assert!(n > 0);
        crate::bitops::len::with_clz(n) as usize - 1
    }

    pub fn msb_number(n: u64) -> u64 { if n == 0 { 0 } else { 1 << msb(n) } }

    /// O(\log\log{N})
    pub fn msb_number_binary_search(mut n: u64) -> u64 {
        const M0: u64 = 0xffffffff00000000;
        const M1: u64 = 0xffff0000ffff0000;
        const M2: u64 = 0xff00ff00ff00ff00;
        const M3: u64 = 0xf0f0f0f0f0f0f0f0;
        const M4: u64 = 0xcccccccccccccccc; // 0b1100...
        const M5: u64 = 0xaaaaaaaaaaaaaaaa; // 0b1010...

        if n & M0 > 0 {
            n &= M0;
        }
        if n & M1 > 0 {
            n &= M1;
        }
        if n & M2 > 0 {
            n &= M2;
        }
        if n & M3 > 0 {
            n &= M3;
        }
        if n & M4 > 0 {
            n &= M4;
        }
        if n & M5 > 0 {
            n &= M5;
        }
        n
    }

    /// least significant bit
    pub fn lsb(n: u64) -> usize {
        assert!(n > 0);
        n.trailing_zeros() as usize
    }

    pub fn lsb_number_i64(n: i64) -> i64 { n & -n }

    pub fn lsb_number(n: u64) -> u64 {
        match n {
            0 => 0,
            n => 1 << lsb(n),
        }
    }

    /// can be called safely only in release mode.
    pub fn rotate_left(x: u64, k: u8) -> u64 { (x << k) | (x >> (64 - k)) }

    pub fn reset(n: u64, i: usize) -> u64 { n & !(1 << i) }

    pub fn reset_least_bit(n: u64) -> u64 {
        if n == 0 { 0 } else { n & (n - 1) }
    }

    pub fn flip(n: u64, i: usize) -> u64 { n ^ (1 << i) }

    #[cfg(test)]
    mod tests {
        use super::*;
        #[test]
        fn test_shr_until_odd() {
            assert_eq!(shr_until_odd(1), 1);
            assert_eq!(shr_until_odd(2), 1);
            assert_eq!(shr_until_odd(12), 3);
        }

        #[test]
        fn test_lsb() {
            assert_eq!(lsb(1), 0,);
        }

        #[test]
        fn test_lsb_number() {
            assert_eq!(lsb_number_i64(0), 0);
            assert_eq!(lsb_number_i64(1), 1);
            assert_eq!(lsb_number_i64(2), 2);
            assert_eq!(lsb_number_i64(3), 1);

            assert_eq!(lsb_number(0), 0);
            assert_eq!(lsb_number(1), 1);
            assert_eq!(lsb_number(2), 2);
            assert_eq!(lsb_number(3), 1);
        }

        #[test]
        fn test_reset_least_bit() {
            assert_eq!(reset_least_bit(0), 0);
            assert_eq!(reset_least_bit(16), 0);
            assert_eq!(reset_least_bit(3), 2);
        }
    }
}
pub mod fenwick {
    //! fenwick tree (binary indexed tree)

    use crate::{
        algebraic_structure::*,
        binary_function::*,
        bitops::{lsb_number, reset_least_bit},
    };

    /// Node Indices
    /// (case $|given array| = 8$,
    /// internally 1-indexed implemetation)
    /// |8              |
    /// |4      |       |
    /// |2  |   |6  |   |
    /// |1| |3| |5| |7| |
    pub struct Fenwick<G: Monoid> {
        data: Vec<G::S>, // data
    }

    impl<G> Fenwick<G>
    where
        G: Monoid + Commutative,
        G::S: Clone,
    {
        /// you need to pass initial values because,
        /// it might not be identity element.
        pub fn new(a: Vec<G::S>) -> Self {
            let size = a.len();
            let mut d = vec![G::e()];
            d.append(&mut a.to_vec());
            for i in 1..size {
                let j = i + lsb_number(i as u64) as usize;
                if j <= size {
                    d[j] = G::op(d[j].clone(), d[i].clone());
                }
            }
            Self { data: d }
        }

        pub fn size(&self) -> usize { self.data.len() - 1 }

        pub fn operate(&mut self, mut i: usize, v: G::S) {
            i += 1;
            while i <= self.size() {
                self.data[i] = G::op(self.data[i].clone(), v.clone());
                i += lsb_number(i as u64) as usize;
            }
        }

        // reduce less than.
        pub fn reduce_lt(&self, mut i: usize) -> G::S {
            let mut v = G::e();
            while i > 0 {
                v = G::op(v, self.data[i].clone());
                i = reset_least_bit(i as u64) as usize;
            }
            v
        }

        pub fn max_right<F>(&self, is_ok: &F) -> usize
        where
            F: Fn(&G::S) -> bool,
        {
            let mut len = (self.size() + 1).next_power_of_two();
            let mut v = G::e();
            let mut r = 0;
            loop {
                len >>= 1;
                if len == 0 {
                    return r;
                }
                if r + len > self.size() {
                    continue;
                }
                let nv = G::op(
                    v.clone(),
                    self.data[r + len].clone(),
                );
                if is_ok(&nv) {
                    r += len;
                    v = nv;
                }
            }
        }
    }

    impl<G> Fenwick<G>
    where
        G: AbelianGroup,
        G::S: Clone,
    {
        pub fn reduce(&self, l: usize, r: usize) -> G::S {
            assert!(l <= r);
            G::op(
                G::inv(self.reduce_lt(l)),
                self.reduce_lt(r),
            )
        }

        pub fn get(&self, i: usize) -> G::S { self.reduce(i, i + 1) }

        /// find r such that \prod[l, r) = true
        pub fn max_right_from<F>(&self, is_ok: &F, l: usize) -> usize
        where
            F: Fn(&G::S) -> bool,
        {
            assert!(l <= self.size());
            let mut len = (self.size() + 1).next_power_of_two();
            let mut v = G::inv(self.reduce_lt(l));
            let mut r = 0;
            loop {
                len >>= 1;
                if len == 0 {
                    debug_assert!(l <= r);
                    return r;
                }
                if r + len > self.size() {
                    continue;
                }
                let nv = G::op(
                    v.clone(),
                    self.data[r + len].clone(),
                );
                if r + len <= l || r + len <= self.size() && is_ok(&nv) {
                    r += len;
                    v = nv;
                }
            }
        }

        /// find l such that \prod[l, r) = true, or return r
        pub fn min_left_from<F>(&self, is_ok: &F, r: usize) -> usize
        where
            F: Fn(&G::S) -> bool,
        {
            assert!(r <= self.size());
            if r == 0 {
                return 0;
            }
            let mut len = (self.size() + 1).next_power_of_two();
            let mut v = self.reduce_lt(r);
            if is_ok(&v) {
                return 0;
            }
            let mut l = 1;
            loop {
                len >>= 1;
                if len == 0 {
                    debug_assert!(l <= r);
                    return l;
                }
                if l + len > r {
                    continue;
                }
                let nv = G::op(
                    G::inv(self.data[l + len - 1].clone()),
                    v.clone(),
                );
                if !is_ok(&nv) {
                    l += len;
                    v = nv;
                }
            }
        }
    }

    pub struct FwDual<G: Monoid> {
        fw: Fenwick<G>,
    }

    impl<G> FwDual<G>
    where
        G: Monoid + Commutative,
        G::S: Clone,
    {
        pub fn new(mut a: Vec<G::S>) -> Self
        where
            G: Inverse,
            G::S: Clone,
        {
            for i in (1..a.len()).rev() {
                a[i] = G::op(
                    G::inv(a[i - 1].clone()),
                    a[i].clone(),
                );
            }
            Self { fw: Fenwick::new(a) }
        }

        pub fn size(&self) -> usize { self.fw.size() }

        /// operate on [i, size)
        pub fn operate_ge(&mut self, i: usize, v: G::S) {
            self.fw.operate(i, v)
        }

        pub fn get(&self, i: usize) -> G::S { self.fw.reduce_lt(i + 1) }

        /// find first index i satisfying
        /// `is_ok(&self.get_point(i)) == true`
        /// Constraints:
        /// `is_ok(&self.get_point(i))` must be monotonous [false,
        /// false, .., true, true] if such an i is not found,
        /// return `self.size()`
        pub fn search<F>(&self, is_ok: &F) -> usize
        where
            F: Fn(&G::S) -> bool,
        {
            self.fw.max_right(&|prod: &G::S| !is_ok(prod))
        }
    }

    impl<G> FwDual<G>
    where
        G: AbelianGroup,
        G::S: Clone,
    {
        pub fn operate(&mut self, l: usize, r: usize, v: G::S) {
            assert!(l < r && r <= self.size());
            self.operate_ge(l, v.clone());
            if r < self.size() {
                self.operate_ge(r, G::inv(v));
            }
        }

        /// prod[left, index) >= target_value - prod[0, left)
        /// prod[left, index) + prod[0, left) >= target_value
        /// is_ok(G::operate(prod[left, index), prod[0, left)))
        /// `is_ok`'s results must be mnotonous
        /// in the range of [left, self.size())
        /// [?, .., ?, false(left), .., false, true .., true]
        /// where first false index corresponds
        /// to the given left, it might be there exists no
        /// false.
        pub fn search_from<F>(&self, is_ok: &F, l: usize) -> usize
        where
            F: Fn(&G::S) -> bool,
        {
            assert!(l <= self.size());
            let prod_lt = if l == 0 { G::e() } else { self.get(l - 1) };
            self.fw.max_right_from(
                &|prod_ge: &G::S| {
                    !is_ok(&G::op(
                        prod_lt.clone(),
                        prod_ge.clone(),
                    ))
                },
                l,
            )
        }

        // /// [false, .. false, true, .., true, ?, .. ?]
        // /// find first true index.
        // /// no longer necessary function.
        // pub fn binary_search_from_right<F>(&self, is_ok: &F, right:
        // usize) -> usize where
        //     F: Fn(&S) -> bool,
        // {
        //     assert!(right <= self.size());
        // }
    }

    // TODO:
    /// fenwick tree lazy for addition on int
    /// TODO: generalize to semiring
    pub struct FwLazyIntAdd {}

    #[cfg(test)]
    mod tests {
        use super::*;
        #[test]
        fn test_fw() {
            use crate::{
                algebraic_structure_impl::GroupApprox,
                group_theory_id::Additive,
            };

            let arr = vec![0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

            let mut fw = Fenwick::<GroupApprox<i32, Additive>>::new(arr);

            assert_eq!(fw.reduce(0, 10), 45);
            assert_eq!(fw.reduce(6, 10), 30);
            fw.operate(5, 10);
            assert_eq!(fw.reduce(6, 10), 30);
            assert_eq!(fw.reduce_lt(5), 10);
            assert_eq!(fw.reduce_lt(6), 25);
            assert_eq!(fw.get(5), 15);
            let is_ok = |x: &i32| *x <= 25;
            assert_eq!(fw.max_right(&is_ok), 6);
            assert_eq!(fw.max_right_from(&is_ok, 0), 6);
            let is_ok = |x: &i32| *x < 25;
            assert_eq!(fw.max_right(&is_ok), 5);
            assert_eq!(fw.max_right_from(&is_ok, 0), 5);
            assert_eq!(fw.max_right_from(&is_ok, 4), 6);
            assert_eq!(fw.max_right_from(&is_ok, 5), 7);
            assert_eq!(fw.max_right_from(&is_ok, 6), 9);
            assert_eq!(
                fw.max_right_from(&is_ok, 9),
                10
            );
            assert_eq!(fw.min_left_from(&is_ok, 10), 7);
            assert_eq!(fw.min_left_from(&is_ok, 0), 0);
            assert_eq!(fw.min_left_from(&is_ok, 6), 2);
            assert_eq!(fw.min_left_from(&is_ok, 5), 0);
            let is_ok = |x: &i32| *x < 15;
            assert_eq!(fw.max_right_from(&is_ok, 5), 5);
            assert_eq!(fw.min_left_from(&is_ok, 6), 6);
            assert_eq!(fw.min_left_from(&is_ok, 10), 9);
            let is_ok = |x: &i32| *x < 9;
            assert_eq!(
                fw.min_left_from(&is_ok, 10),
                10
            );
        }

        #[test]
        fn test_dual() {
            use crate::{
                algebraic_structure_impl::GroupApprox,
                group_theory_id::Additive,
            };
            let mut a = (0..10).collect::<Vec<_>>();
            for i in 0..9 {
                a[i + 1] += a[i];
            }
            type Fw = FwDual<GroupApprox<i32, Additive>>;
            let mut fw = Fw::new(a);
            assert_eq!(fw.get(1), 1);
            assert_eq!(fw.get(5), 15);
            assert_eq!(fw.get(9), 45);
            fw.operate_ge(5, 2);
            assert_eq!(fw.get(1), 1);
            assert_eq!(fw.get(5), 17);
            assert_eq!(fw.get(9), 47);
            assert_eq!(
                fw.search(&|value: &i32| *value >= 23),
                6
            );
            assert_eq!(
                fw.search(&|value: &i32| *value >= 47),
                9
            );
            assert_eq!(
                fw.search(&|value: &i32| *value > 47),
                10
            );

            fw.operate(2, 6, 1);
            assert_eq!(fw.get(1), 1);
            assert_eq!(fw.get(5), 18);
            assert_eq!(fw.get(9), 47);
            fw.operate(2, 6, -1);
            assert_eq!(
                fw.search_from(&|value: &i32| *value >= 23, 0),
                6
            );
            assert_eq!(
                fw.search_from(&|value: &i32| *value >= 47, 0),
                9
            );
            assert_eq!(
                fw.search_from(&|value: &i32| *value > 47, 0),
                10
            );

            let b = (0..10).map(|i| fw.get(i)).collect::<Vec<_>>();
            assert_eq!(
                b,
                [
                    0, 1, 3, 6, 10, 17, 23, 30, 38, 47
                ]
            );

            assert_eq!(
                fw.search_from(&|value: &i32| *value >= 23, 7),
                7
            );
            assert_eq!(
                fw.search_from(&|value: &i32| *value >= 23, 5),
                6
            );
        }

        // TODO:
        #[test]
        fn test_lazy() {}
    }
}
