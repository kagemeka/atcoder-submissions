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

    // let n: usize = reader.read()?;

    // let a = (0..n)
    //     .map(|_| reader.read::<u64>().unwrap())
    //     .collect::<Vec<_>>();

    // let bases = (0..5).map(|_| static_xorshift_64()).collect::<Vec<_>>();
    // let tester = FermatTestFixedBases::new(bases);
    // for x in a {
    //     writeln!(
    //         writer,
    //         "{}",
    //         if tester.is_prime(x) { "Yes" } else { "No" }
    //     )?;
    // }

    struct GCD;

    impl BinaryOperation<GCD> for u64 {
        type Codomain = Self;
        type Lhs = Self;
        type Rhs = Self;

        fn map(l: Self, r: Self) -> Self { gcd_00_is_0(l, r) }
    }
    impl AssociativeProperty<GCD> for u64 {}
    impl CommutativeProperty<GCD> for u64 {}
    impl Idempotence<GCD> for u64 {}

    let n: usize = reader.read()?;
    let q: usize = reader.read()?;
    let a = read_vec!(reader, u64, n);
    let b = read_vec!(reader, u64, n);
    let da = (0..n - 1).map(|i| {
        if a[i] >= a[i + 1] {
            a[i] - a[i + 1]
        } else {
            a[i + 1] - a[i]
        }
    });

    let db = (0..n - 1).map(|i| {
        if b[i] >= b[i + 1] {
            b[i] - b[i + 1]
        } else {
            b[i + 1] - b[i]
        }
    });

    // let sp_a = SparseTable::<u64, GCD>::from_iter(da);
    // let sp_b = SparseTable::<u64, GCD>::from_iter(db);
    let sp_a = DisjointSparseTable::<u64, GCD>::from_iter(da);
    let sp_b = DisjointSparseTable::<u64, GCD>::from_iter(db);

    for _ in 0..q {
        let mut h0: usize = reader.read()?;
        let h1: usize = reader.read()?;
        let mut w0: usize = reader.read()?;
        let w1: usize = reader.read()?;

        h0 -= 1;
        w0 -= 1;

        let mut g = a[h0] + b[w0];
        if h1 - h0 > 1 {
            g = gcd_00_is_0(g, sp_a.reduce(h0, h1 - 1));
        }
        if w1 - w0 > 1 {
            g = gcd_00_is_0(g, sp_b.reduce(w0, w1 - 1));
        }
        writeln!(writer, "{}", g)?;
    }

    writer.flush()?;
    Ok(())
}

pub fn gcd_00_is_0(a: u64, b: u64) -> u64 {
    if a == 0 && b == 0 { 0 } else { gcd(a, b) }
}

/// gcd(0, 0) is infinity -> panic.
/// user can redefine gcd(0, 0) := 0 outside of this function.
/// but strictlly, we should not return gcd(0, 0).
pub fn gcd(mut a: u64, mut b: u64) -> u64 {
    while b != 0 {
        a %= b;
        std::mem::swap(&mut a, &mut b);
    }
    assert_ne!(a, 0);
    a
}

pub trait CommutativeProperty<Id: BinaryOperationId> {}
pub trait Idempotence<Id: BinaryOperationId> {}

pub trait BinaryOperationId {}

impl<T> BinaryOperationId for T {}

pub trait Semigroup<Id: BinaryOperationId>: Magma<Id> {}

impl<Id, T> Semigroup<Id> for T
where
    T: Magma<Id> + AssociativeProperty<Id>,
    Id: BinaryOperationId,
{
}

pub trait Magma<Id: BinaryOperationId> {
    type S;
    fn operate(l: Self::S, r: Self::S) -> Self::S;
}

impl<S, Id, T> Magma<Id> for T
where
    T: BinaryOperation<Id, Lhs = S, Rhs = S, Codomain = S>,
    Id: BinaryOperationId,
{
    type S = S;

    fn operate(l: Self::S, r: Self::S) -> Self::S { T::map(l, r) }
}

pub trait BinaryOperation<Id: BinaryOperationId> {
    type Lhs;
    type Rhs;
    type Codomain;
    fn map(l: Self::Lhs, r: Self::Rhs) -> Self::Codomain;
}

pub trait AssociativeProperty<Id: BinaryOperationId> {}

pub struct SparseTable<G: Semigroup<Id>, Id> {
    data: Vec<Vec<G::S>>,
}

impl<G, Id> std::iter::FromIterator<G::S> for SparseTable<G, Id>
where
    G: Semigroup<Id> + Idempotence<Id> + CommutativeProperty<Id>,
    G::S: Clone,
{
    fn from_iter<T: IntoIterator<Item = G::S>>(iter: T) -> Self {
        let mut data = vec![iter.into_iter().collect::<Vec<_>>()];
        let max_width = data[0].len();
        let height = if max_width <= 1 {
            1
        } else {
            max_width.next_power_of_two().trailing_zeros() as usize
        };
        for i in 1..height {
            let row_size = max_width - (1 << i) + 1;
            // last is max_width - (1 << i) covering (1 << i)
            // including the position.
            data.push(
                (0..row_size)
                    .map(|j| {
                        G::operate(
                            data[i - 1][j].clone(),
                            data[i - 1][j + (1 << (i - 1))].clone(),
                        )
                    })
                    .collect(),
            );
        }
        Self { data }
    }
}

use std::iter::FromIterator;
impl<G, Id> SparseTable<G, Id>
where
    G: Semigroup<Id> + Idempotence<Id> + CommutativeProperty<Id>,
    G::S: Clone,
{
    pub fn new(slice: &[G::S]) -> Self {
        Self::from_iter(slice.iter().cloned())
    }

    pub fn size(&self) -> usize { self.data[0].len() }

    pub fn reduce(&self, l: usize, r: usize) -> G::S {
        assert!(l < r && r <= self.size());
        if r - l == 1 {
            return self.data[0][l].clone();
        }
        let i = (r - l).next_power_of_two().trailing_zeros() as usize - 1;
        G::operate(
            self.data[i][l].clone(),
            self.data[i][r - (1 << i)].clone(),
        )
    }
}

pub struct DisjointSparseTable<G: Semigroup<Id>, Id> {
    data: Vec<Vec<G::S>>,
}

impl<G, Id> std::iter::FromIterator<G::S> for DisjointSparseTable<G, Id>
where
    G: Semigroup<Id> + CommutativeProperty<Id>,
    G::S: Clone,
{
    fn from_iter<T: IntoIterator<Item = G::S>>(iter: T) -> Self {
        let mut data = vec![iter.into_iter().collect::<Vec<_>>()];
        let size = data[0].len();
        let height = if size <= 1 {
            1
        } else {
            size.next_power_of_two().trailing_zeros() as usize
        };
        for i in 1..height {
            let mut row = data[0].clone();
            for p in (1 << i..=size).step_by(2 << i) {
                for d in 1..(1 << i) {
                    let j = p - d;
                    row[j - 1] = G::operate(
                        row[j - 1].clone(),
                        row[j].clone(),
                    );
                }
                for d in 0..(1 << i) - 1 {
                    let j = p + d;
                    if j + 1 >= size {
                        break;
                    }
                    row[j + 1] = G::operate(
                        row[j].clone(),
                        row[j + 1].clone(),
                    );
                }
            }
            data.push(row);
        }
        Self { data }
    }
}

impl<G, Id> DisjointSparseTable<G, Id>
where
    G: Semigroup<Id> + CommutativeProperty<Id>,
    G::S: Clone,
{
    pub fn new(slice: &[G::S]) -> Self {
        Self::from_iter(slice.iter().cloned())
    }

    pub fn size(&self) -> usize { self.data[0].len() }

    /// [l, r)
    pub fn reduce(&self, l: usize, mut r: usize) -> G::S {
        assert!(l < r && r <= self.size());
        r -= 1; // internally, consider [l, r]
        if l == r {
            return self.data[0][l].clone();
        }
        let i = bit_length((l ^ r) as u64) as usize - 1;
        // if i = 0, then use 0-th row.
        // if i = 3, then use 3-th row.
        // what does this mean?
        // only msb of l \xor r is important.
        // because,
        // for each bit j (checking in descending order from top bit),
        // if for any k in 2^j..=|data| (step 2^{j + 1}), l < k <= r,
        // then j-th bit of l \xor r is gonna be 1.
        // so the query can be dealed with j-th row.
        // <->
        // if j-th bit of l \xor r is 0,
        // then for all k in 2^j..=|data| (step 2^{j + 1}),
        // k <= l < r or l < r < k.
        // so the query cannot be dealed with j-th row.
        // then, check {j-1}-th bit next...
        G::operate(
            self.data[i][l].clone(),
            self.data[i][r].clone(),
        )
    }
}

/// O(1)
pub fn bit_length(n: u64) -> u8 {
    (0u64.leading_zeros() - n.leading_zeros()) as u8
}
