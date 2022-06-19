pub mod io {

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

    #[derive(Debug, Clone, Copy, PartialEq, Eq)]
    pub struct GroupApprox<S, I>(std::marker::PhantomData<(S, I)>);

    /// ((usize, usize), min)
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

    /// (u64, min)
    impl BinaryOp for GroupApprox<u64, Min> {
        type S = u64;

        fn op(lhs: Self::S, rhs: Self::S) -> Self::S { lhs.min(rhs) }
    }

    impl Idempotence for GroupApprox<u64, Min> {}

    impl Commutative for GroupApprox<u64, Min> {}

    impl Associative for GroupApprox<u64, Min> {}

    impl Identity for GroupApprox<u64, Min> {
        fn e() -> Self::S { std::u64::MAX }
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

    /// latin square property
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

        pub trait Commutative<I: Id> {}

        pub trait Associative<I: Id> {}

        pub trait Idempotence<I: Id> {}

        pub trait Identity<I: Id> {
            fn e() -> Self;
        }

        pub trait Inverse<I: Id> {
            fn inv(_: Self) -> Self;
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

        pub trait Semigroup<I: Id>: Magma<I> + Associative<I> {}

        impl<I, T> Semigroup<I> for T
        where
            T: Magma<I> + Associative<I>,
            I: Id,
        {
        }

        pub trait Monoid<I: Id>: Semigroup<I> + Identity<I> {}

        impl<I, T> Monoid<I> for T
        where
            T: Semigroup<I> + Identity<I>,
            I: Id,
        {
        }

        pub trait Group<I: Id>: Monoid<I> + Inverse<I> {}

        impl<I, T> Group<I> for T
        where
            T: Monoid<I> + Inverse<I>,
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
        const MASKS: [u64; 6] = [
            0xffffffff00000000,
            0xffff0000ffff0000,
            0xff00ff00ff00ff00,
            0xf0f0f0f0f0f0f0f0,
            0xcccccccccccccccc, // 0b1100...
            0xaaaaaaaaaaaaaaaa, // 0b1010...
        ];
        // TODO: change later. not compile on AtCoder.
        // for m in MASKS {
        for m in MASKS.iter() {
            if n & m > 0 {
                n &= m;
            }
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

pub mod range_get_query {
    pub trait RangeGetQuery<I> {
        type T;
        fn get_range(&mut self, l: usize, r: usize) -> Self::T;
    }
}

pub mod segtree {
    use std::iter::FromIterator;

    use crate::algebraic_structure::*;

    /// Segment Tree
    pub struct Segtree<M: Monoid> {
        pub(crate) size: usize,
        pub(crate) data: Vec<M::S>,
    }

    impl<M> std::iter::FromIterator<M::S> for Segtree<M>
    where
        M: Monoid,
        M::S: Clone,
    {
        fn from_iter<T: IntoIterator<Item = M::S>>(iter: T) -> Self {
            let mut data = iter.into_iter().collect::<Vec<_>>();
            let size = data.len();
            let n = size.next_power_of_two();
            data = (0..n)
                .map(|_| M::e())
                .chain(data.into_iter())
                .chain((0..n - size).map(|_| M::e()))
                .collect::<Vec<_>>();
            let mut seg = Self { size, data };
            (1..n).rev().for_each(|i| seg.update(i));
            seg
        }
    }

    impl<M: Monoid> Segtree<M> {
        pub fn size(&self) -> usize { self.size }

        pub(crate) fn n(&self) -> usize { self.data.len() >> 1 }
    }

    impl<M> Segtree<M>
    where
        M: Monoid,
        M::S: Clone,
    {
        pub fn new<F>(size: usize, default: F) -> Self
        where
            F: Fn() -> M::S,
        {
            Self::from_iter((0..size).map(|_| default()))
        }

        fn update(&mut self, i: usize) {
            self.data[i] = M::op(
                self.data[i << 1].clone(),
                self.data[i << 1 | 1].clone(),
            );
        }

        pub fn set(&mut self, mut i: usize, x: M::S) {
            assert!(i < self.size);
            i += self.n();
            self.data[i] = x;
            while i > 1 {
                i >>= 1;
                self.update(i);
            }
        }

        /// why `reduce` but `fold`?
        /// but initial element internally is just the identity element.
        /// it's not an arbitrary element.
        /// also, it is not necessarily used to compute _{op}\prod_l^r (l < r).
        /// we use the identity only to make it easy implementation.
        /// (requireing monoid for simplicity,
        /// however, strictly, it's enough to be only semigrouop.)
        /// so this method should be called `reduce`.
        pub fn reduce(&self, mut l: usize, mut r: usize) -> M::S {
            assert!(l < r && r <= self.size);
            let n = self.n();
            l += n;
            r += n;
            let mut vl = M::e();
            let mut vr = M::e();
            while l < r {
                if l & 1 == 1 {
                    vl = M::op(vl, self.data[l].clone());
                    l += 1;
                }
                if r & 1 == 1 {
                    r -= 1;
                    vr = M::op(self.data[r].clone(), vr);
                }
                l >>= 1;
                r >>= 1;
            }
            M::op(vl, vr)
        }
    }

    impl<M> Segtree<M>
    where
        M: Monoid,
        M::S: Clone,
    {
        pub fn reduce_recurse(&self, l: usize, r: usize) -> M::S {
            assert!(l <= r && r <= self.size);
            self._reduce_recurse(l, r, 0, self.n(), 1)
        }

        fn _reduce_recurse(
            &self,
            l: usize,
            r: usize,
            cur_l: usize,
            cur_r: usize,
            i: usize,
        ) -> M::S {
            if cur_r <= l || r <= cur_l {
                return M::e();
            }
            if l <= cur_l && cur_r <= r {
                return self.data[i].clone();
            }
            let c = (cur_l + cur_r) >> 1;
            M::op(
                self._reduce_recurse(l, r, cur_l, c, i << 1),
                self._reduce_recurse(l, r, c, cur_r, i << 1 | 1),
            )
        }
    }

    /// indexing
    impl<M> std::ops::Index<usize> for Segtree<M>
    where
        M: Monoid,
    {
        type Output = M::S;

        fn index(&self, i: usize) -> &Self::Output {
            assert!(i < self.size());
            &self.data[i + self.n()]
        }
    }

    impl<M> From<&[M::S]> for Segtree<M>
    where
        M: Monoid,
        M::S: Clone,
    {
        fn from(slice: &[M::S]) -> Self {
            Self::from_iter(slice.iter().cloned())
        }
    }

    impl<M> Segtree<M>
    where
        M: Monoid,
        M::S: Clone,
    {
        pub fn max_right<F>(&self, is_ok: &F, l: usize) -> usize
        where
            F: Fn(&M::S) -> bool,
        {
            assert!(l <= self.size);
            if l == self.size {
                return self.size;
            }
            let n = self.n();
            let mut v = M::e();
            let mut i = l + n;
            debug_assert_ne!(i, 0);
            loop {
                i >>= i.trailing_zeros(); // upstream
                let nv = M::op(v.clone(), self.data[i].clone());
                if !is_ok(&nv) {
                    break;
                }
                // otherwise up one stair to right
                i += 1;
                v = nv;
                if i.count_ones() == 1 {
                    return self.size;
                }
            }
            // down stairs to right
            while i < n {
                i <<= 1;
                let nv = M::op(v.clone(), self.data[i].clone());
                if !is_ok(&nv) {
                    continue;
                }
                v = nv;
                i += 1;
            }
            i - n
        }

        pub fn min_left<F>(&self, is_ok: &F, r: usize) -> usize
        where
            F: Fn(&M::S) -> bool,
        {
            assert!(r <= self.size);
            if r == 0 {
                return 0;
            }
            let n = self.n();
            let mut v = M::e();
            let mut i = r + n;
            debug_assert_ne!(i, 0);
            loop {
                i >>= i.trailing_zeros(); // upstream
                let nv = M::op(
                    self.data[i - 1].clone(),
                    v.clone(),
                );
                if !is_ok(&nv) {
                    break;
                }
                i -= 1;
                v = nv;
                if i.count_ones() == 1 {
                    return 0;
                }
            }
            while i < n {
                i <<= 1;
                let nv = M::op(
                    self.data[i - 1].clone(),
                    v.clone(),
                );
                if !is_ok(&nv) {
                    continue;
                }
                i -= 1;
                v = nv;
            }
            i - n
        }
    }

    impl<M> Segtree<M>
    where
        M: Monoid,
        M::S: Clone,
    {
        pub fn max_right_recurse<F>(&self, is_ok: &F, l: usize) -> usize
        where
            F: Fn(&M::S) -> bool,
        {
            assert!(l <= self.size);
            self._max_right_recurse(
                is_ok,
                l,
                0,
                self.n(),
                &mut M::e(),
                1,
            )
        }

        /// find max right satisfying current_left <= right <= current_right.
        /// if current_right <= left, return left
        /// if current_left >= self.size, return self.size
        fn _max_right_recurse<F>(
            &self,
            is_ok: &F,
            l: usize,
            cur_l: usize,
            cur_r: usize,
            v: &mut M::S,
            i: usize,
        ) -> usize
        where
            F: Fn(&M::S) -> bool,
        {
            if cur_r <= l {
                return l;
            }
            if cur_l >= self.size {
                return self.size;
            }
            let nv = M::op(v.clone(), self.data[i].clone());
            if l <= cur_l && cur_r <= self.size && is_ok(&nv) {
                *v = nv;
                return cur_r;
            }
            if cur_r - cur_l == 1 {
                return cur_l;
            }
            let c = (cur_l + cur_r) >> 1;
            let res = self._max_right_recurse(is_ok, l, cur_l, c, v, i << 1);
            if res < c || res == self.size {
                return res;
            }
            self._max_right_recurse(
                is_ok,
                l,
                c,
                cur_r,
                v,
                i << 1 | 1,
            )
        }

        pub fn min_left_recurse<F>(&self, is_ok: &F, r: usize) -> usize
        where
            F: Fn(&M::S) -> bool,
        {
            assert!(r <= self.size);
            self._min_left_recurse(
                is_ok,
                r,
                0,
                self.n(),
                &mut M::e(),
                1,
            )
        }

        fn _min_left_recurse<F>(
            &self,
            is_ok: &F,
            r: usize,
            cur_l: usize,
            cur_r: usize,
            v: &mut M::S,
            i: usize,
        ) -> usize
        where
            F: Fn(&M::S) -> bool,
        {
            if cur_l >= r {
                return r;
            }
            let nv = M::op(self.data[i].clone(), v.clone());
            if cur_r <= r && is_ok(&nv) {
                *v = nv;
                return cur_l;
            }
            if cur_r - cur_l == 1 {
                return cur_r;
            }
            let c = (cur_l + cur_r) >> 1;
            let res = self._min_left_recurse(
                is_ok,
                r,
                c,
                cur_r,
                v,
                i << 1 | 1,
            );
            if res > c {
                return res;
            }
            self._min_left_recurse(is_ok, r, cur_l, c, v, i << 1)
        }
    }

    use crate::{algebraic_structure_impl::*, range_get_query::RangeGetQuery};

    impl<S, I> RangeGetQuery<I> for Segtree<GroupApprox<S, I>>
    where
        GroupApprox<S, I>: Monoid<S = S>,
        S: Clone,
    {
        type T = S;

        fn get_range(&mut self, l: usize, r: usize) -> Self::T {
            self.reduce(l, r)
        }
    }

    #[cfg(test)]
    mod tests {
        use super::*;
        use crate::group_theory_id::Additive;
        type Seg = Segtree<GroupApprox<usize, Additive>>;

        #[test]
        fn test_basic() {
            let mut seg = Seg::new(10, || 0);
            assert_eq!(seg.reduce(0, 10), 0);
            seg.set(5, 5);
            assert_eq!(seg.reduce(0, 10), 5);
            seg.set(5, 10);
            assert_eq!(seg.reduce(0, 10), 10);
        }

        #[test]
        fn test_indexing() {
            let mut seg = Seg::new(10, || 0);
            seg.set(5, 10);
            assert_eq!(seg[5], 10);
        }

        #[test]
        fn test_reduce_recurse() {
            let mut seg = Seg::new(10, || 0);
            assert_eq!(seg.reduce_recurse(0, 10), 0);
            seg.set(5, 5);
            assert_eq!(seg.reduce_recurse(0, 10), 5);
            seg.set(5, 10);
            assert_eq!(seg.reduce_recurse(0, 10), 10);
        }

        #[test]
        fn test_binary_search() {
            // use crate::monoid::Monoid;
            let mut seg = Seg::new(10, || 0);
            assert_eq!(seg.reduce(0, 10), 0);
            seg.set(5, 10);
            let is_ok = &|sum: &usize| *sum < 10;
            assert_eq!(seg.max_right(is_ok, 0), 5);
            assert_eq!(seg.max_right(is_ok, 10), 10);
            assert_eq!(seg.max_right(is_ok, 5), 5);
            assert_eq!(seg.max_right(is_ok, 6), 10);

            assert_eq!(seg.min_left(is_ok, 10), 6);
            assert_eq!(seg.min_left(is_ok, 5), 0);
            assert_eq!(seg.min_left(is_ok, 6), 6);
        }

        #[test]
        fn test_binary_search_recurse() {
            let mut seg = Seg::new(10, || 0);
            assert_eq!(seg.reduce(0, 10), 0);
            seg.set(5, 10);
            let is_ok = &|sum: &usize| *sum < 10;
            assert_eq!(
                seg.max_right_recurse(is_ok, 0),
                5
            );
            assert_eq!(
                seg.max_right_recurse(is_ok, 10),
                10
            );
            assert_eq!(
                seg.max_right_recurse(is_ok, 5),
                5
            );
            assert_eq!(
                seg.max_right_recurse(is_ok, 6),
                10
            );

            assert_eq!(
                seg.min_left_recurse(is_ok, 10),
                6
            );
            assert_eq!(
                seg.min_left_recurse(is_ok, 5),
                0
            );
            assert_eq!(
                seg.min_left_recurse(is_ok, 6),
                6
            );
        }
    }
}

pub mod modular {
    use crate::power::pow_monoid;

    /// pow for u32
    /// why not only u64?
    /// because it's expensive to cast as u128.
    pub fn pow(m: u32, base: u64, exp: u64) -> u32 {
        let modulus = m as u64;
        pow_monoid(
            &|x, y| x * y % modulus,
            &|| 1,
            base % modulus,
            exp,
        ) as u32
    }

    pub fn pow_64(m: u64, base: u128, exp: u64) -> u64 {
        let modulus = m as u128;
        pow_monoid(
            &|x, y| x * y % modulus,
            &|| 1,
            base % modulus,
            exp,
        ) as u64
    }

    /// avoid overflow on u128.
    /// pow for addition.
    /// under u64 -> it's enough to cast as u128.
    pub fn mul_doubling(mut a: u128, mut b: u128, m: u128) -> u128 {
        let mut res = 0;
        while b > 0 {
            if b & 1 == 1 {
                res = (res + a) % m;
            }
            a = (a << 1) % m;
            b >>= 1;
        }
        res
    }

    // TODO:
    pub fn primitive_root() {}

    pub mod modulus {
        pub trait StaticGet {
            type T;
            fn get() -> Self::T;
        }

        pub trait StaticSet {
            type T;
            fn set(value: Self::T);
        }

        pub trait DynGet {
            type T;
            fn get(&self) -> Self::T;
        }

        pub trait DynSet {
            type T;
            fn set(&mut self, value: Self::T);
        }

        pub trait Id {}

        impl<T> Id for T {}

        macro_rules! define_static_mod {
            (
                $name:ident,
                $uint:ty,
                $atomic_uint:ty,
                $atomic_ordering_store:expr,
                $atomic_ordering_load:expr
            ) => {
                #[derive(
                    Debug, Copy, Clone, PartialEq, Eq, PartialOrd, Ord, Hash,
                )]
                pub struct $name<Id>(std::marker::PhantomData<Id>);

                impl<Id> $name<Id> {
                    fn cell() -> &'static $atomic_uint {
                        // VALUE type needs Sync + 'static
                        // std::cell types are not Sync
                        // std::sync::Mutex is not 'static
                        // only atomic types can be.
                        // or we can use external crate like `lazy_static`.

                        // why not defining as associated const variable?
                        // -> const variables are immutabe in any situation.
                        static CELL: $atomic_uint = <$atomic_uint>::new(0);
                        &CELL
                    }
                }

                impl<Id> StaticGet for $name<Id> {
                    type T = $uint;

                    fn get() -> Self::T {
                        Self::cell().load($atomic_ordering_load)
                    }
                }

                impl<Id> StaticSet for $name<Id> {
                    type T = $uint;

                    fn set(value: Self::T) {
                        Self::cell().store(value, $atomic_ordering_store);
                    }
                }
            };

            ($name:ident, $uint:ty, $atomic_uint:ty) => {
                define_static_mod!(
                    $name,
                    $uint,
                    $atomic_uint,
                    std::sync::atomic::Ordering::SeqCst,
                    std::sync::atomic::Ordering::SeqCst
                );
            };
        }

        use std::sync::atomic::{AtomicU32, AtomicU64};
        define_static_mod!(StaticMod32, u32, AtomicU32);
        define_static_mod!(StaticMod64, u64, AtomicU64);

        // TODO: change later. not compile on AtCoder.
        // macro_rules! define_const_mod {
        //     ($name:ident, $uint:ty) => {
        //         #[derive(
        //             Debug, Copy, Clone, PartialEq, Eq, PartialOrd, Ord, Hash,
        //         )]
        //         pub struct $name<const MOD: $uint>;

        //         impl<const MOD: $uint> StaticGet for $name<MOD> {
        //             type T = $uint;

        //             fn get() -> Self::T { MOD }
        //         }
        //     };
        // }

        // define_const_mod!(ConstMod64, u64);
        // define_const_mod!(ConstMod32, u32);

        /// old version for online judges.
        macro_rules! define_const_mod_old {
            ($name:ident, $uint:ty, $value:expr) => {
                #[derive(
                    Debug, Copy, Clone, PartialEq, Eq, PartialOrd, Ord, Hash,
                )]
                pub struct $name;

                impl StaticGet for $name {
                    type T = $uint;

                    fn get() -> Self::T { $value }
                }
            };
        }

        define_const_mod_old!(
            Mod998_244_353,
            u32,
            998_244_353
        );
        define_const_mod_old!(
            Mod1_000_000_007,
            u32,
            1_000_000_007
        );

        /// T is gonna be u64 or u32
        #[derive(Debug, Copy, Clone, PartialEq, Eq, PartialOrd, Ord, Hash)]
        pub struct DynMod<T>(T);

        impl<T> DynMod<T> {
            pub fn new(value: T) -> Self { Self(value) }
        }

        impl<T: Copy> DynGet for DynMod<T> {
            type T = T;

            fn get(&self) -> Self::T { self.0 }
        }

        impl<T> DynSet for DynMod<T> {
            type T = T;

            fn set(&mut self, value: Self::T) { self.0 = value }
        }

        #[cfg(test)]
        mod tests {
            use super::*;
            // TODO: change later. not compile on AtCoder.

            // #[test]
            // fn test_const_mod() {
            //     type Mod = ConstMod32<1_000_000_007>;
            //     assert_eq!(Mod::get(), 1_000_000_007);
            // }

            #[test]
            fn test_const_mod_old() {
                type Mod = Mod1_000_000_007;
                assert_eq!(Mod::get(), 1_000_000_007);
            }

            #[test]
            fn test_static_mod() {
                struct Id;
                type Mod = StaticMod32<Id>;
                Mod::set(1_000_000_007);
                assert_eq!(Mod::get(), 1_000_000_007);
                Mod::set(998_244_353);
                assert_eq!(Mod::get(), 998_244_353);
            }
            #[test]
            fn test_dyn_mod() {
                type Mod = DynMod<u32>;

                let mut m = Mod::new(998_244_353);
                assert_eq!(m.get(), 998_244_353);
                m.set(1_000_000_007);
                assert_eq!(m.get(), 1_000_000_007);
            }
        }
    }

    pub mod arithmetic {
        //! reference
        //! https://en.wikipedia.org/wiki/Modular_arithmetic#Properties

        pub trait Static {
            type T;

            fn modulus() -> Self::T;

            fn add(lhs: Self::T, rhs: Self::T) -> Self::T;
            fn neg(x: Self::T) -> Self::T;
            fn sub(lhs: Self::T, rhs: Self::T) -> Self::T {
                Self::add(lhs, Self::neg(rhs))
            }
            fn mul(lhs: Self::T, rhs: Self::T) -> Self::T;
            fn inv(x: Self::T) -> Self::T;
            fn div(lhs: Self::T, rhs: Self::T) -> Self::T {
                Self::mul(lhs, Self::inv(rhs))
            }
        }

        pub trait Dyn {
            type T;
            fn modulus(&self) -> Self::T;

            fn add(&self, lhs: Self::T, rhs: Self::T) -> Self::T;
            fn neg(&self, x: Self::T) -> Self::T;
            fn sub(&self, lhs: Self::T, rhs: Self::T) -> Self::T {
                self.add(lhs, self.neg(rhs))
            }
            fn mul(&self, lhs: Self::T, rhs: Self::T) -> Self::T;
            fn inv(&self, x: Self::T) -> Self::T;
            fn div(&self, lhs: Self::T, rhs: Self::T) -> Self::T {
                self.mul(lhs, self.inv(rhs))
            }
        }

        use crate::modular::{inv::extgcd as invert, modulus::StaticGet};

        /// why `default`?
        /// because there exists other modular arithmetic implementations.
        /// e.g. Montgomery Multiplication, or Burrett Reduction.
        #[derive(
            Debug, Clone, Copy, PartialEq, Eq, Hash, PartialOrd, Ord, Default,
        )]
        pub struct DefaultStatic<T, M: StaticGet<T = T>>(
            std::marker::PhantomData<(T, M)>,
        );

        macro_rules! impl_default_static {
            ($uint:ty, $mul_cast_uint:ty) => {
                impl<M: StaticGet<T = $uint>> Static
                    for DefaultStatic<$uint, M>
                {
                    type T = $uint;

                    fn modulus() -> Self::T { M::get() }

                    fn add(lhs: Self::T, rhs: Self::T) -> Self::T {
                        assert!(lhs < M::get() && rhs < M::get());
                        let mut x = lhs;
                        x += rhs;
                        if x >= M::get() {
                            x -= M::get();
                        }
                        x
                    }

                    fn neg(x: Self::T) -> Self::T {
                        assert!(x < M::get());
                        if x == 0 { 0 } else { M::get() - x }
                    }

                    fn mul(lhs: Self::T, rhs: Self::T) -> Self::T {
                        let mut x = lhs as $mul_cast_uint;
                        x *= rhs as $mul_cast_uint;
                        x %= M::get() as $mul_cast_uint;
                        x as Self::T
                    }

                    fn inv(x: $uint) -> Self::T {
                        assert!(x > 0);
                        invert(M::get() as u64, x as u64).unwrap() as Self::T
                    }
                }
            };
        }

        impl_default_static!(u32, u64);
        impl_default_static!(u64, u128);

        // TODO: change later. still not compile on AtCoder.
        // use crate::modular::modulus::ConstMod32;

        // #[allow(dead_code)]
        // pub type Modular1_000_000_007 =
        //     DefaultStatic<u32, ConstMod32<1_000_000_007>>;

        // #[allow(dead_code)]
        // pub type Modular998_244_353 =
        //     DefaultStatic<u32, ConstMod32<998_244_353>>;

        use crate::modular::modulus::{Mod1_000_000_007, Mod998_244_353};

        #[allow(dead_code)]
        pub type Modular1_000_000_007 = DefaultStatic<u32, Mod1_000_000_007>;

        #[allow(dead_code)]
        pub type Modular998_244_353 = DefaultStatic<u32, Mod998_244_353>;

        #[cfg(test)]
        mod tests {
            use super::*;
            #[test]
            fn test() {
                use crate::modular::int::Modint;

                type Mint = Modint<u32, Modular1_000_000_007>;
                let a = Mint::from(1_000_000_008);
                assert_eq!(a.value(), 1);
            }
        }
    }

    pub mod inv {
        //! well-known modular inverse algorithms.

        /// inverse by Fermat's Little Theorem.
        /// for prime modulus.
        pub fn fermat() {
            // TODO:
        }

        /// inverse by Euler's Theorem.
        pub fn euler() {
            // TODO:
            // check gcd
            // return error if gcd != 1
            // or compute inverse with totient function.
            // related: carmichael_function.rs
        }

        use crate::ext_euclid::mod_gcd_inv;

        /// inverse by Extended Euclidean Algorithm.
        pub fn extgcd(modulus: u64, element: u64) -> Result<u64, &'static str> {
            let (gcd, inv) = mod_gcd_inv(modulus, element);
            if gcd == 1 {
                Ok(inv)
            } else {
                Err("modulus and element are not coprime")
            }
        }
    }

    pub mod int {
        use crate::modular::arithmetic::Static as Arithmetic;

        /// static modular element.
        /// modular element is only static.
        /// because all instances should be in the same arithmetic context.
        /// T should be u32 or u64.
        #[derive(
            Debug, Clone, Copy, PartialEq, Eq, PartialOrd, Ord, Hash, Default,
        )]
        pub struct Modint<T, M>
        where
            M: Arithmetic<T = T>,
        {
            value: M::T,
        }

        impl<T, M> std::fmt::Display for Modint<T, M>
        where
            M: Arithmetic<T = T>,
            M::T: std::fmt::Display,
        {
            fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
                write!(f, "{}", self.value)
            }
        }

        impl<M: Arithmetic<T = u64>> Modint<u64, M> {
            pub fn new(mut v: u64) -> Self {
                if v >= M::modulus() {
                    v %= M::modulus();
                }
                Modint { value: v }
            }
        }

        impl<M: Arithmetic<T = u32>> Modint<u32, M> {
            pub fn new(mut v: u32) -> Self {
                if v >= M::modulus() {
                    v %= M::modulus();
                }
                Modint { value: v }
            }
        }

        impl<T, M> Modint<T, M>
        where
            M: Arithmetic<T = T>,
            M::T: Copy,
        {
            // TODO: make const
            pub fn value(&self) -> M::T { self.value }

            // pub fn new(value: M::T) -> Self { Self { value } }

            pub fn modulus() -> M::T { M::modulus() }
        }

        impl<T, M> std::ops::Add for Modint<T, M>
        where
            M: Arithmetic<T = T>,
            T: Copy,
        {
            type Output = Self;

            fn add(mut self, rhs: Self) -> Self::Output {
                self.value = M::add(self.value, rhs.value);
                self
            }
        }

        impl<T, M> std::ops::AddAssign for Modint<T, M>
        where
            M: Arithmetic<T = T> + Copy,
            T: Copy,
        {
            fn add_assign(&mut self, rhs: Self) { *self = *self + rhs; }
        }

        impl<T, M> std::ops::Sub for Modint<T, M>
        where
            M: Arithmetic<T = T>,
            T: Copy,
        {
            type Output = Self;

            fn sub(mut self, rhs: Self) -> Self::Output {
                self.value = M::sub(self.value, rhs.value);
                self
            }
        }

        impl<T, M> std::ops::SubAssign for Modint<T, M>
        where
            M: Arithmetic<T = T> + Copy,
            T: Copy,
        {
            fn sub_assign(&mut self, rhs: Self) { *self = *self - rhs; }
        }

        impl<T, M> std::ops::Neg for Modint<T, M>
        where
            M: Arithmetic<T = T>,
            T: Copy,
        {
            type Output = Self;

            fn neg(mut self) -> Self::Output {
                self.value = M::neg(self.value);
                self
            }
        }

        impl<T, M> std::ops::Mul for Modint<T, M>
        where
            M: Arithmetic<T = T>,
            T: Copy,
        {
            type Output = Self;

            fn mul(mut self, rhs: Self) -> Self::Output {
                self.value = M::mul(self.value, rhs.value);
                self
            }
        }

        impl<T, M> std::ops::MulAssign for Modint<T, M>
        where
            M: Arithmetic<T = T> + Copy,
            T: Copy,
        {
            fn mul_assign(&mut self, rhs: Self) { *self = *self * rhs; }
        }

        impl<T, M> std::ops::Div for Modint<T, M>
        where
            M: Arithmetic<T = T>,
            T: Copy,
        {
            type Output = Self;

            fn div(mut self, rhs: Self) -> Self::Output {
                self.value = M::div(self.value, rhs.value);
                self
            }
        }

        impl<T, M> std::ops::DivAssign for Modint<T, M>
        where
            M: Arithmetic<T = T> + Copy,
            T: Copy,
        {
            fn div_assign(&mut self, rhs: Self) { *self = *self / rhs; }
        }

        impl<T, M> Modint<T, M>
        where
            M: Arithmetic<T = T> + Copy,
            T: Copy,
        {
            pub fn inv(mut self) -> Self {
                self.value = M::inv(self.value);
                self
            }
        }

        impl<M> From<i32> for Modint<u32, M>
        where
            M: Arithmetic<T = u32>,
        {
            fn from(value: i32) -> Self { Self::from(value as i64) }
        }

        impl<M> From<i32> for Modint<u64, M>
        where
            M: Arithmetic<T = u64>,
        {
            fn from(value: i32) -> Self { Self::from(value as i64) }
        }

        impl<M> From<i64> for Modint<u32, M>
        where
            M: Arithmetic<T = u32>,
        {
            fn from(mut value: i64) -> Self {
                let m = M::modulus() as i64;
                if value < -m || value >= m {
                    value %= m;
                }
                if value < 0 {
                    value += m;
                }
                Self::new(value as u32)
            }
        }

        impl<M> From<i64> for Modint<u64, M>
        where
            M: Arithmetic<T = u64>,
        {
            fn from(mut value: i64) -> Self {
                let m = M::modulus() as i64;
                if value < -m || value >= m {
                    value %= m;
                }
                if value < 0 {
                    value += m;
                }
                Self::new(value as u64)
            }
        }
        // TODO: move out From<T> from this file.
        // because these are extensions rather than core functionality.
        impl<M> From<u64> for Modint<u64, M>
        where
            M: Arithmetic<T = u64>,
        {
            fn from(mut value: u64) -> Self {
                let m = M::modulus();
                if value >= m {
                    value %= m;
                }
                Self::new(value)
            }
        }

        impl<M> From<u64> for Modint<u32, M>
        where
            M: Arithmetic<T = u32>,
        {
            fn from(mut value: u64) -> Self {
                let m = M::modulus() as u64;
                if value >= m {
                    value %= m;
                }
                Self::new(value as u32)
            }
        }
        impl<M> From<usize> for Modint<u32, M>
        where
            M: Arithmetic<T = u32>,
        {
            fn from(value: usize) -> Self { Self::from(value as u64) }
        }

        impl<M> From<usize> for Modint<u64, M>
        where
            M: Arithmetic<T = u64>,
        {
            fn from(value: usize) -> Self { Self::from(value as u64) }
        }

        use crate::power::itself::PowMonoid;

        impl<M> Modint<u64, M>
        where
            M: Arithmetic<T = u64>,
            Self: Clone,
        {
            pub fn pow(self, exponent: u64) -> Self {
                self.pow_monoid(exponent)
            }
        }

        impl<M> Modint<u32, M>
        where
            M: Arithmetic<T = u32>,
            Self: Clone,
        {
            pub fn pow(self, exponent: u64) -> Self {
                self.pow_monoid(exponent)
            }
        }

        use crate::{
            binary_function::itself::*,
            group_theory_id::*,
            ops::MulInv,
        };

        impl<T, M> BinaryOp<Multiplicative> for Modint<T, M>
        where
            M: Arithmetic<T = T>,
            T: Copy,
        {
            fn op(lhs: Self, rhs: Self) -> Self { lhs * rhs }
        }

        impl<M> Identity<Multiplicative> for Modint<u64, M>
        where
            M: Arithmetic<T = u64>,
        {
            fn e() -> Self { 1.into() }
        }

        impl<M> Identity<Multiplicative> for Modint<u32, M>
        where
            M: Arithmetic<T = u32>,
        {
            fn e() -> Self { 1.into() }
        }

        impl<T, M> Associative<Multiplicative> for Modint<T, M> where
            M: Arithmetic<T = T>
        {
        }

        impl<M> MulInv for Modint<u64, M>
        where
            M: Arithmetic<T = u64> + Copy,
        {
            type Output = Self;

            fn mul_inv(self) -> Self::Output { self.inv() }
        }

        impl<M> MulInv for Modint<u32, M>
        where
            M: Arithmetic<T = u32> + Copy,
        {
            type Output = Self;

            fn mul_inv(self) -> Self::Output { self.inv() }
        }

        // TODO:
        #[cfg(test)]
        mod tests {
            #[test]
            fn test() {}
        }
    }

    #[cfg(test)]
    mod tests {
        use super::*;
        #[test]
        fn test_mul_doubling_128() {
            let a = 1234567890123456789u128;
            let m = 1u128 << 100;
            assert_eq!(
                mul_doubling(a, a, m),
                a * a % m,
            );
        }
    }
}

pub mod power {
    pub fn pow_semigroup_recurse<F, X>(f: &F, x: X, exp: u64) -> X
    where
        F: Fn(X, X) -> X,
        X: Clone,
    {
        assert!(exp > 0);
        if exp == 1 {
            return x;
        }
        let mut y = pow_semigroup_recurse(f, x.clone(), exp >> 1);
        y = f(y.clone(), y);
        if exp & 1 == 1 {
            y = f(y, x);
        }
        y
    }

    pub fn pow_semigroup<F, X>(f: &F, mut x: X, mut exp: u64) -> X
    where
        F: Fn(X, X) -> X,
        X: Clone,
    {
        assert!(exp > 0);
        let mut y = x.clone();
        exp -= 1;
        while exp > 0 {
            if exp & 1 == 1 {
                y = f(y, x.clone());
            }
            x = f(x.clone(), x);
            exp >>= 1;
        }
        y
    }

    pub fn pow_monoid<F, E, X>(f: &F, e: &E, x: X, exp: u64) -> X
    where
        F: Fn(X, X) -> X,
        E: Fn() -> X,
        X: Clone,
    {
        if exp == 0 { e() } else { pow_semigroup(f, x, exp) }
    }

    pub fn pow_group<F, E, Inv, X>(f: &F, e: &E, inv: &Inv, x: X, exp: i64) -> X
    where
        F: Fn(X, X) -> X,
        E: Fn() -> X,
        Inv: Fn(X) -> X,
        X: Clone,
    {
        if exp >= 0 {
            pow_monoid(f, e, x, exp as u64)
        } else {
            pow_semigroup(f, inv(x), -exp as u64)
        }
    }

    use crate::algebraic_structure::*;
    pub trait PowSemigroup: Semigroup
    where
        Self::S: Clone,
    {
        fn pow_seimigroup(x: Self::S, exp: u64) -> Self::S {
            pow_semigroup(&Self::op, x, exp)
        }
    }

    impl<T: Semigroup> PowSemigroup for T where T::S: Clone {}

    pub trait PowMonoid: Monoid
    where
        Self::S: Clone,
    {
        fn pow_monoid(x: Self::S, exp: u64) -> Self::S {
            pow_monoid(&Self::op, &Self::e, x, exp)
        }
    }
    impl<T: Monoid> PowMonoid for T where T::S: Clone {}

    pub trait PowGroup: Group
    where
        Self::S: Clone,
    {
        fn pow_group(x: Self::S, exp: i64) -> Self::S {
            pow_group(
                &Self::op,
                &Self::e,
                &Self::inv,
                x,
                exp,
            )
        }
    }
    impl<T: Group> PowGroup for T where T::S: Clone {}

    pub mod itself {
        use crate::algebraic_structure::itself::*;
        pub trait PowSemigroup<I>: Semigroup<I>
        where
            Self: Clone,
        {
            fn pow_seimigroup(self, exp: u64) -> Self {
                super::pow_semigroup(&Self::op, self, exp)
            }
        }

        impl<S: Semigroup<I> + Clone, I> PowSemigroup<I> for S {}

        pub trait PowMonoid<I>: Monoid<I>
        where
            Self: Clone,
        {
            fn pow_monoid(self, exp: u64) -> Self {
                super::pow_monoid(&Self::op, &Self::e, self, exp)
            }
        }

        impl<S: Monoid<I> + Clone, I> PowMonoid<I> for S {}

        pub trait PowGroup<I>: Group<I>
        where
            Self: Clone,
        {
            fn pow_group(self, exp: i64) -> Self {
                super::pow_group(
                    &Self::op,
                    &Self::e,
                    &Self::inv,
                    self,
                    exp,
                )
            }
        }

        impl<S: Group<I> + Clone, I> PowGroup<I> for S {}
    }

    pub mod dynamic {}
}

pub mod ops {
    pub trait MulInv {
        type Output;
        fn mul_inv(self) -> Self::Output;
    }
}
pub mod ext_euclid {
    //! extended euclidean algorithms

    pub fn extgcd_recurse(a: i64, b: i64) -> (u64, i64, i64) {
        if b == 0 {
            return if a < 0 { ((-a) as u64, -1, 0) } else { (a as u64, 1, 0) };
        }
        let (g, s, t) = extgcd_recurse(b, a % b);
        (g, t, s - a / b * t)
    }

    pub fn extgcd(mut a: i64, mut b: i64) -> (u64, i64, i64) {
        let (mut x00, mut x01, mut x10, mut x11) = (1, 0, 0, 1);
        while b != 0 {
            let q = a / b;
            // (x00, x01) = (x01, x00 - q * x01);
            // (x10, x11) = (x11, x10 - q * x11);
            // (a, b) = (b, a % b);
            x00 -= q * x01;
            std::mem::swap(&mut x00, &mut x01);
            x10 -= q * x11;
            std::mem::swap(&mut x10, &mut x11);
            a %= b;
            std::mem::swap(&mut a, &mut b);
        }
        if a < 0 {
            a = -a;
            x00 = -x00;
            x10 = -x10;
        }
        (a as u64, x00, x10)
    }

    /// compute g := \gcd(modulus, n),
    /// and modular inverse of n/g in Z_{modulus/g}.
    /// we convert parameters to i64 internally.
    /// so be careful not to pass modulus > 2^63 because it overflows.
    /// it's `trivial` that inverse of 0 is undefined, so if n = 0, it panics.
    pub fn mod_gcd_inv(modulus: u64, n: u64) -> (u64, u64) {
        assert!(0 < n && n < modulus);
        let (mut a, mut b) = (n as i64, modulus as i64);
        let (mut x00, mut x01) = (1, 0);
        while b != 0 {
            // (x00, x01) = (x01, x00 - a / b * x01);
            // (a, b) = (b, a % b);

            x00 -= a / b * x01;
            std::mem::swap(&mut x00, &mut x01);
            a %= b;
            std::mem::swap(&mut a, &mut b);
        }
        let gcd = a as u64;
        let u = (modulus / gcd) as i64;
        if x00 < 0 {
            x00 += u;
        }
        debug_assert!(0 <= x00 && x00 < u);
        (gcd, x00 as u64)
    }

    #[cfg(test)]
    mod tests {
        use super::*;
        #[test]
        fn test_mod_gcd_inv() {
            // euclidean_mod_gcd_inv(10, 0); // runtime error.
            assert_eq!(mod_gcd_inv(5, 2), (1, 3));
            assert_eq!(mod_gcd_inv(18, 12), (6, 2));
            assert_eq!(mod_gcd_inv(111, 30), (3, 26));
            // gcd(111, 30) = 3
            // 111 / 3 = 37, 30 / 3 = 10, 10^{-1} \equiv 26 \mod 37
        }

        #[test]
        fn test_extgcd() {
            assert_eq!(
                extgcd_recurse(-30, 111),
                (3, 11, 3)
            );
            assert_eq!(extgcd_recurse(0, 0), (0, 1, 0));
            assert_eq!(extgcd(-30, 111), (3, 11, 3));
            assert_eq!(extgcd(111, 30), (3, 3, -11));
            assert_eq!(extgcd(0, 0), (0, 1, 0));
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
        d: Vec<G::S>, // data
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
            Self { d }
        }

        pub fn size(&self) -> usize { self.d.len() - 1 }

        pub fn operate(&mut self, mut i: usize, v: G::S) {
            i += 1;
            while i <= self.size() {
                self.d[i] = G::op(self.d[i].clone(), v.clone());
                i += lsb_number(i as u64) as usize;
            }
        }

        // reduce less than.
        pub fn reduce_lt(&self, mut i: usize) -> G::S {
            let mut v = G::e();
            while i > 0 {
                v = G::op(v, self.d[i].clone());
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
                    self.d[r + len].clone(),
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
                    self.d[r + len].clone(),
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
                    G::inv(self.d[l + len - 1].clone()),
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

pub mod scc {
    //! strongly connected components

    /// directed sparse graph. it not necessarily be simple.
    pub type G = Vec<Vec<usize>>;

    fn trans(g: G) -> G {
        let n = g.len();
        let mut t = vec![vec![]; n];
        for i in 0..n {
            for j in g[i].clone() {
                t[j].push(i);
            }
        }
        t
    }
    pub fn kosaraju(g: G) -> Vec<usize> {
        struct D {
            g: G,
            vis: Vec<bool>,
            q: Vec<usize>,
            l: Vec<usize>,
        }
        let n = g.len();
        let mut d = D {
            g,
            vis: vec![false; n],
            q: vec![],
            l: vec![n; n],
        };
        fn dfs(d: &mut D, u: usize) {
            d.vis[u] = true;
            for v in d.g[u].clone() {
                if !d.vis[v] {
                    dfs(d, v);
                }
            }
            d.q.push(u);
        }
        fn rds(d: &mut D, u: usize, l: usize) {
            d.l[u] = l;
            for v in d.g[u].clone() {
                if d.l[v] == d.g.len() {
                    rds(d, v, l);
                }
            }
        }
        for i in 0..n {
            if !d.vis[i] {
                dfs(&mut d, i);
            }
        }
        d.g = trans(d.g);
        let mut l = 0;
        for i in d.q.clone().into_iter().rev() {
            if d.l[i] == n {
                rds(&mut d, i, l);
                l += 1;
            }
        }
        d.l
    }

    fn toposort(lb: Vec<usize>) -> Vec<usize> {
        let k = *lb.iter().max().unwrap();
        lb.into_iter().map(|l| k - l).collect::<Vec<_>>()
    }

    /// with tarjan's lowlink algorithm.
    pub fn tarjan(g: G) -> Vec<usize> {
        struct D {
            g: G,
            s: Vec<usize>,   // stack
            ord: Vec<usize>, // preorder
            o: usize,
            lo: Vec<usize>, // low preorder
            lb: Vec<usize>, // label
            l: usize,
        }
        let n = g.len();
        let mut d = D {
            g,
            s: vec![],
            ord: vec![n; n],
            o: 0,
            lo: vec![n; n],
            lb: vec![n; n],
            l: 0,
        };

        fn labeling(d: &mut D, u: usize) {
            d.ord[u] = d.o;
            d.o += 1;
            d.s.push(u);
            let n = d.g.len();
            for v in d.g[u].clone() {
                if d.ord[v] == n {
                    labeling(d, v);
                    d.lo[u] = d.lo[u].min(d.lo[v]);
                } else if d.lb[v] == n {
                    // on stack
                    d.lo[u] = d.lo[u].min(d.ord[v]);
                }
            }
            if d.lo[u] < d.ord[u] {
                return;
            }
            loop {
                let v = d.s.pop().unwrap();
                d.lb[v] = d.l;
                if v == u {
                    break;
                }
            }
            d.l += 1;
        }

        for i in 0..n {
            if d.ord[i] == n {
                labeling(&mut d, i);
            }
        }
        toposort(d.lb)
    }

    /// essentially same as Tarjan's Lowlink algorithm
    pub fn path_based(g: G) -> Vec<usize> {
        struct D {
            g: G,
            s: Vec<usize>,   // stack
            sl: Vec<usize>,  // stack for lowlink
            ord: Vec<usize>, // preorder
            o: usize,
            lb: Vec<usize>, // label
            l: usize,
        }
        let n = g.len();
        let mut d = D {
            g,
            s: vec![],
            sl: vec![],
            ord: vec![n; n],
            o: 0,
            lb: vec![n; n],
            l: 0,
        };

        fn labeling(d: &mut D, u: usize) {
            d.ord[u] = d.o;
            d.o += 1;
            d.s.push(u);
            d.sl.push(u);
            let n = d.g.len();
            for v in d.g[u].clone() {
                if d.ord[v] == n {
                    labeling(d, v);
                } else if d.lb[v] == n {
                    while d.ord[*d.sl.last().unwrap()] > d.ord[v] {
                        d.sl.pop();
                    }
                }
            }
            if d.sl.last().unwrap() != &u {
                return;
            }
            loop {
                let v = d.s.pop().unwrap();
                d.lb[v] = d.l;
                if v == u {
                    break;
                }
            }
            d.l += 1;
            d.sl.pop();
        }

        for i in 0..n {
            if d.ord[i] == n {
                labeling(&mut d, i);
            }
        }
        toposort(d.lb)
    }

    // TODO:
    /// reachability based
    pub fn reachable_based() {}

    // TODO
    #[cfg(test)]
    mod tests {
        #[test]
        fn test() {}
    }
}
// TODO: main
// #[allow(warnings)]
fn main() -> Result<(), Box<dyn std::error::Error>> {
    use std::io::Write;

    use io::*;
    let mut reader = locked_stdin_reader();
    let mut writer = locked_stdout_buf_writer();

    let n: usize = reader.read()?;
    let m: usize = reader.read()?;
    let mut g = vec![vec![]; n];
    for _ in 0..m {
        let u: usize = reader.read()?;
        let v: usize = reader.read()?;
        g[u].push(v);
    }
    // let labels = scc::kosaraju(g);
    let labels = scc::tarjan(g);
    // let labels = scc::path_based(g);
    let k = *labels.iter().max().unwrap() + 1;
    let mut comp = vec![vec![]; k];
    for i in 0..n {
        comp[labels[i]].push(i);
    }
    writeln!(writer, "{}", k)?;
    for c in comp {
        write!(writer, "{} ", c.len())?;
        write_vec!(writer, c);
    }

    writer.flush()?;
    Ok(())
}
