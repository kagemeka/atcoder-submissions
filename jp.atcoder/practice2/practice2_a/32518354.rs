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

    use uf::*;
    let n: usize = reader.read()?;
    let q: usize = reader.read()?;

    let mut g = UF::new(n);
    for _ in 0..q {
        let t: usize = reader.read()?;
        let u: usize = reader.read()?;
        let v: usize = reader.read()?;

        if t == 0 {
            g.unite(u, v);
        } else {
            writeln!(
                writer,
                "{}",
                if g.same(u, v) { 1 } else { 0 }
            )?;
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
