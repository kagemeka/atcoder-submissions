pub struct ReadWrapper<R> {
    reader: R,
    tokens: Vec<String>,
}

/// Example
/// ```
/// use dsalgo::io::ReadWrapper;
/// let stdin = std::io::stdin();
/// let mut reader = ReadWrapper::new(stdin.lock());
/// // let x = reader.read::<usize>();
/// ```
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

/// Example
/// ```
/// use std::io::Write;
///
/// use dsalgo::io::locked_stdin_buf_writer;
/// let mut writer = locked_stdin_buf_writer();
/// writeln!(writer, "Hello, world!");
/// writer.flush().unwrap();
/// ```
pub fn locked_stdin_buf_writer()
-> std::io::BufWriter<std::io::StdoutLock<'static>> {
    let stdout = Box::leak(Box::new(std::io::stdout()));
    std::io::BufWriter::new(stdout.lock())
}

pub trait BinaryOperation<L, R, Codomain, Id> {
    fn operate(lhs: L, rhs: R) -> Codomain;
}

pub trait AssociativeProperty<X, Id>: BinaryOperation<X, X, X, Id> {
    fn assert_associative(first: X, second: X, third: X)
    where
        X: Clone + PartialEq + std::fmt::Debug,
    {
        assert_eq!(
            Self::operate(
                Self::operate(first.clone(), second.clone()),
                third.clone()
            ),
            Self::operate(
                first,
                Self::operate(second, third)
            ),
        );
    }
}

pub trait Idempotence<X, Id>: BinaryOperation<X, X, X, Id> {
    fn assert_idempotent(element: X)
    where
        X: Clone + PartialEq + std::fmt::Debug,
    {
        assert_eq!(
            Self::operate(
                element.clone(),
                element.clone()
            ),
            element
        );
    }
}

pub trait CommutativeProperty<X, Y, Id>: BinaryOperation<X, X, Y, Id> {
    fn assert_commutative(a: X, b: X)
    where
        X: Clone,
        Y: PartialEq + std::fmt::Debug,
    {
        assert_eq!(
            Self::operate(a.clone(), b.clone()),
            Self::operate(b, a)
        );
    }
}

pub trait IdentityElement<X, Id>: BinaryOperation<X, X, X, Id> {
    fn identity() -> X;
}

pub trait InverseElement<X, Id>: IdentityElement<X, Id> {
    fn invert(element: X) -> X;
}

pub trait Magma<S, Id>: BinaryOperation<S, S, S, Id> {}
impl<S, I, T> Magma<S, I> for T where T: BinaryOperation<S, S, S, I> {}

pub trait Semigroup<S, Id>: Magma<S, Id> + AssociativeProperty<S, Id> {}

impl<S, I, T> Semigroup<S, I> for T where
    T: Magma<S, I> + AssociativeProperty<S, I>
{
}

pub trait Monoid<S, Id>: Semigroup<S, Id> + IdentityElement<S, Id> {}
impl<S, I, T: Semigroup<S, I> + IdentityElement<S, I>> Monoid<S, I> for T {}

pub trait CommutativeMonoid<S, Id>:
    Monoid<S, Id> + CommutativeProperty<S, S, Id> + Sized
{
}
impl<S, I, T> CommutativeMonoid<S, I> for T where
    T: Monoid<S, I> + CommutativeProperty<S, S, I>
{
}

pub trait Group<S, Id>: Monoid<S, Id> + InverseElement<S, Id> {}

impl<S, I, T: Monoid<S, I> + InverseElement<S, I>> Group<S, I> for T {}

pub trait AbelianGroup<S, Id>:
    Group<S, Id> + CommutativeProperty<S, S, Id>
{
}
impl<S, I, T> AbelianGroup<S, I> for T where
    T: Group<S, I> + CommutativeProperty<S, S, I>
{
}

pub trait Semiring<S, Add, Mul>:
    CommutativeMonoid<S, Add> + Monoid<S, Mul>
{
}
impl<S, A, M, T> Semiring<S, A, M> for T where
    T: CommutativeMonoid<S, A> + Monoid<S, M>
{
}

pub trait Ring<S, Add, Mul>:
    Semiring<S, Add, Mul> + IdentityElement<S, Add>
{
}
impl<S, A, M, T> Ring<S, A, M> for T where
    T: Semiring<S, A, M> + IdentityElement<S, A>
{
}

pub struct Additive;
pub struct Multiplicative;

pub struct Xor;
pub struct GCD;
pub struct LCM;
pub struct Min;
pub struct Max;

pub trait AdditiveGroup<S>: AbelianGroup<S, Additive> {}
impl<S, T> AdditiveGroup<S> for T where T: AbelianGroup<S, Additive> {}

pub trait MulInv {
    type Output;
    fn mul_inv(self) -> Self::Output;
}

pub fn pow_semigroup_recurse<S, Id, G>(x: S, exponent: u64) -> S
where
    S: Clone,
    G: Semigroup<S, Id>,
{
    assert!(exponent > 0);
    if exponent == 1 {
        return x;
    }
    let mut y = pow_semigroup_recurse::<S, Id, G>(x.clone(), exponent >> 1);
    y = G::operate(y.clone(), y);
    if exponent & 1 == 1 {
        y = G::operate(y, x);
    }
    y
}

pub fn pow_semigroup<S, Id, G>(mut x: S, mut exponent: u64) -> S
where
    S: Clone,
    G: Semigroup<S, Id>,
{
    assert!(exponent > 0);
    let mut y = x.clone();
    exponent -= 1;
    while exponent > 0 {
        if exponent & 1 == 1 {
            y = G::operate(y, x.clone());
        }
        x = G::operate(x.clone(), x.clone());
        exponent >>= 1;
    }
    y
}

pub trait PowerSemigroup<Id>: Semigroup<Self, Id>
where
    Self: Clone,
{
    fn pow_seimigroup(self, exponent: u64) -> Self {
        pow_semigroup::<Self, Id, Self>(self, exponent)
    }
}
impl<S, Id> PowerSemigroup<Id> for S where S: Semigroup<S, Id> + Clone {}

pub fn pow_monoid<S, Id, M>(x: S, exponent: u64) -> S
where
    S: Clone,
    M: Monoid<S, Id>,
{
    if exponent == 0 {
        M::identity()
    } else {
        pow_semigroup::<S, Id, M>(x, exponent)
    }
}

pub trait PowerMonoid<Id>: Monoid<Self, Id>
where
    Self: Clone,
{
    fn pow_monoid(self, exponent: u64) -> Self {
        pow_monoid::<Self, Id, Self>(self, exponent)
    }
}
impl<S, Id> PowerMonoid<Id> for S where S: Monoid<S, Id> + Clone {}

pub fn pow_group<S, Id, G>(x: S, exponent: i64) -> S
where
    S: Clone,
    G: Group<S, Id>,
{
    if exponent >= 0 {
        pow_monoid::<S, Id, G>(x, exponent as u64)
    } else {
        pow_monoid::<S, Id, G>(G::invert(x), -exponent as u64)
    }
}

pub trait PowerGroup<Id>: Group<Self, Id>
where
    Self: Clone,
{
    fn pow_group(self, exponent: i64) -> Self {
        pow_group::<Self, Id, Self>(self, exponent)
    }
}
impl<S, Id> PowerGroup<Id> for S where S: Group<S, Id> + Clone {}

/// compute g := \gcd(modulus, n),
/// and modular inverse of n/g in Z_{modulus/g}.
/// interface is i64 but u64 because it overflows if modulus > 2^63.
/// by converting it to i64 internally.
pub fn extgcd_modinv(modulus: i64, n: i64) -> (i64, i64) {
    assert!(0 < n && n < modulus);
    // it's trivial that inverse of 0 is undefined.
    let (mut a, mut b) = (n, modulus);
    let (mut x00, mut x01) = (1, 0);
    while b != 0 {
        // this syntax is not supported on AtCoder yet.
        // (x00, x01) = (x01, x00 - a / b * x01);
        // (a, b) = (b, a % b);

        // old writing version.
        std::mem::swap(&mut x00, &mut x01);
        x01 -= a / b * x00;
        std::mem::swap(&mut a, &mut b);
        b %= a;
    }
    if x00 < 0 {
        x00 += modulus / a;
    }
    assert!(0 <= x00 && x00 < modulus / a);
    (a, x00)
}

pub trait Modulus {
    fn value() -> u32;
}

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub struct Modular<M> {
    phantom: std::marker::PhantomData<M>,
    value: u32,
}

impl<M> std::fmt::Display for Modular<M> {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "{}", self.value)
    }
}

impl<M> Modular<M> {
    // new version, cannot compile AtCoder yet.
    // pub const fn value(&self) -> u32 { self.value }

    pub fn value(&self) -> u32 { self.value }
}

impl<M: Modulus> Modular<M> {
    pub fn new(mut value: u32) -> Self {
        if value >= M::value() {
            value %= M::value();
        }
        Self {
            phantom: std::marker::PhantomData,
            value,
        }
    }

    pub fn modulus() -> u32 { M::value() }
}

impl<M: Modulus> From<u64> for Modular<M> {
    fn from(mut value: u64) -> Self {
        let m = M::value() as u64;
        if value >= m {
            value %= m;
        }
        Self::new(value as u32)
    }
}
impl<M: Modulus> From<i64> for Modular<M> {
    fn from(mut value: i64) -> Self {
        let m = M::value() as i64;
        if value < 0 || value >= m {
            value %= m;
        }
        if value < 0 {
            value += m;
        }
        Self::new(value as u32)
    }
}

impl<M: Modulus> std::ops::AddAssign<Self> for Modular<M> {
    fn add_assign(&mut self, rhs: Self) {
        let mut value = self.value as u64 + rhs.value as u64;
        let m = M::value() as u64;
        if value >= m {
            value -= m;
        }
        self.value = value as u32;
    }
}

impl<M: Modulus> std::ops::Add<Self> for Modular<M> {
    type Output = Self;

    fn add(mut self, rhs: Self) -> Self::Output {
        self += rhs;
        self
    }
}

impl<M: Modulus> std::ops::Neg for Modular<M> {
    type Output = Self;

    fn neg(mut self) -> Self::Output {
        self.value = M::value() - self.value;
        self
    }
}

impl<M: Modulus> std::ops::SubAssign<Self> for Modular<M> {
    fn sub_assign(&mut self, rhs: Self) { *self += -rhs; }
}

impl<M: Modulus> std::ops::Sub<Self> for Modular<M> {
    type Output = Self;

    fn sub(mut self, rhs: Self) -> Self {
        self -= rhs;
        self
    }
}

impl<M: Modulus> std::ops::MulAssign<Self> for Modular<M> {
    fn mul_assign(&mut self, rhs: Self) {
        let mut value = self.value as u64 * rhs.value as u64;
        let m = M::value() as u64;
        if value >= m {
            value %= m;
        }
        self.value = value as u32;
    }
}

impl<M: Modulus> std::ops::Mul<Self> for Modular<M> {
    type Output = Self;

    fn mul(mut self, rhs: Self) -> Self {
        self *= rhs;
        self
    }
}

impl<M: Modulus> std::ops::DivAssign<Self> for Modular<M> {
    fn div_assign(&mut self, rhs: Self) { *self *= rhs.invert().unwrap(); }
}
impl<M: Modulus> std::ops::Div<Self> for Modular<M> {
    type Output = Self;

    fn div(mut self, rhs: Self) -> Self::Output {
        self /= rhs;
        self
    }
}

impl<M: Modulus> Modular<M> {
    /// unlike extgcd, the caller cannot eunsure the inverse exist.
    /// with additional constant run time cost before calling this function.
    /// so if the inverse element does not exit,
    /// handle execption inside the method, and return Result<T, E>
    pub fn invert(self) -> Result<Self, &'static str> {
        if self.value() == 0 {
            return Err("0 is not invertible");
        }
        let (g, inv) = extgcd_modinv(
            M::value() as i64,
            self.value() as i64,
        );
        if g != 1 {
            Err("value and modulus are not coprime")
        } else {
            Ok(inv.into())
        }
    }
}

impl<M: Modulus> From<i32> for Modular<M> {
    fn from(value: i32) -> Self { Self::from(value as i64) }
}

impl<M: Modulus> From<usize> for Modular<M> {
    fn from(value: usize) -> Self { Self::from(value as u64) }
}

impl<M: Modulus> BinaryOperation<Self, Self, Self, Multiplicative>
    for Modular<M>
{
    fn operate(lhs: Self, rhs: Self) -> Self { lhs * rhs }
}

impl<M: Modulus> IdentityElement<Self, Multiplicative> for Modular<M> {
    fn identity() -> Self { 1.into() }
}

impl<M: Modulus> AssociativeProperty<Self, Multiplicative> for Modular<M> {}

impl<M: Modulus + Clone> Modular<M> {
    pub fn pow(self, exponent: u64) -> Self { self.pow_monoid(exponent) }
}

impl<M: Modulus> MulInv for Modular<M> {
    type Output = Self;

    fn mul_inv(self) -> Self::Output { self.invert().unwrap() }
}

// old version.
#[derive(Debug, Copy, Clone, PartialEq, Eq, PartialOrd, Ord, Hash)]
struct Mod1_000_000_007;

impl Modulus for Mod1_000_000_007 {
    fn value() -> u32 { 1_000_000_007 }
}

#[derive(Debug, Copy, Clone, PartialEq, Eq, PartialOrd, Ord, Hash)]
struct Mod998_244_353;

impl Modulus for Mod998_244_353 {
    fn value() -> u32 { 998_244_353 }
}

pub trait DynamicModId {}

impl<T> DynamicModId for T {}

/// ```
/// use dsalgo::dynamic_modulus::DynamicMod;
/// struct Foo;
/// type Mod = DynamicMod<Foo>;
/// Mod::set(1_000_000_007);
/// assert_eq!(Mod::value(), 1_000_000_007);
/// ```
#[derive(Debug, Copy, Clone, PartialEq, Eq, PartialOrd, Ord, Hash)]
pub struct DynamicMod<Id: DynamicModId>(std::marker::PhantomData<Id>);

impl<I: DynamicModId> DynamicMod<I> {
    fn core() -> &'static std::sync::atomic::AtomicU32 {
        // cannot return &'static mut VALUE because it can be changed by
        // multiple threads.
        // so we should return a reference of a type having interior mutability.
        // cannot use std::cell for static value because it is not
        // `Sync`;
        // we should use std::sync types instead.
        // atomic types are lighter than mutex.

        static VALUE: std::sync::atomic::AtomicU32 =
            std::sync::atomic::AtomicU32::new(0);
        &VALUE
    }

    pub fn set(value: u32) {
        assert!(value > 1);
        Self::core().store(
            value,
            std::sync::atomic::Ordering::SeqCst,
        );
    }
}

impl<I: DynamicModId> Modulus for DynamicMod<I> {
    fn value() -> u32 { Self::core().load(std::sync::atomic::Ordering::SeqCst) }
}

pub fn accumulate<T, F>(mut v: Vec<T>, f: F) -> Vec<T>
where
    T: Clone,
    F: Fn(T, T) -> T,
{
    for i in 0..v.len() - 1 {
        v[i + 1] = f(v[i].clone(), v[i + 1].clone());
    }
    v
}

pub fn factorial_table<T>(size: usize) -> Vec<T>
where
    T: std::ops::Mul<Output = T> + From<u64> + Clone,
{
    let mut v = (0..size as u64).map(|i| i.into()).collect::<Vec<T>>();
    v[0] = 1.into();
    let op = |a: T, b: T| -> T { a * b };
    accumulate(v, op)
}

pub fn factorial<T>(n: u64) -> T
where
    T: std::ops::Mul<Output = T> + From<u64>,
{
    (1..=n).fold(1.into(), |accum, x| {
        accum * x.into()
    })
}

pub fn inverse_factorial_table<T>(size: usize) -> Vec<T>
where
    T: std::ops::Mul<Output = T> + MulInv<Output = T> + From<u64> + Clone,
{
    let mut v = (0..size as u64).map(|i| (i + 1).into()).collect::<Vec<T>>();
    if size == 0 {
        return v;
    }
    v[size - 1] = factorial::<T>(size as u64 - 1).mul_inv();
    let op = |a: T, b: T| -> T { a * b };
    accumulate(
        v.into_iter().rev().collect(),
        op,
    )
    .into_iter()
    .rev()
    .collect()
}

pub struct Combination<T> {
    fact: Vec<T>,
    inv_fact: Vec<T>,
}

impl<T> Combination<T>
where
    T: std::ops::Mul<Output = T> + From<u64> + Clone,
{
    pub fn new(size: usize) -> Self
    where
        T: MulInv<Output = T>,
    {
        let fact = factorial_table::<T>(size);
        let inv_fact = inverse_factorial_table::<T>(size);
        Self { fact, inv_fact }
    }

    pub fn calc(&self, n: u64, k: u64) -> T {
        if k > n {
            return 0.into();
        }
        let n = n as usize;
        let k = k as usize;
        self.fact[n].clone()
            * self.inv_fact[n - k].clone()
            * self.inv_fact[k].clone()
    }

    pub fn inv(&self, n: u64, k: u64) -> T {
        assert!(k <= n); // (n, k) := 0 if k > n, so the inverse is undefined.
        let n = n as usize;
        let k = k as usize;
        self.inv_fact[n].clone()
            * self.fact[k].clone()
            * self.fact[n - k].clone()
    }
}

impl<T> Choose<T> for Combination<T>
where
    T: std::ops::Mul<Output = T> + From<u64> + Clone,
{
    fn choose(&mut self, n: u64, k: u64) -> T { self.calc(n, k) }
}

pub trait Choose<T> {
    fn choose(&mut self, n: u64, k: u64) -> T;
}

pub struct HomogeneousProduct<T> {
    chooser: Box<dyn Choose<T>>,
}

impl<T> HomogeneousProduct<T> {
    pub fn new(chooser: Box<dyn Choose<T>>) -> Self { Self { chooser } }

    pub fn calc(&mut self, n: u64, k: u64) -> T
    where
        T: From<u64>,
    {
        if n == 0 {
            0.into()
        } else {
            self.chooser.choose(n + k - 1, k)
        }
    }
}

pub fn pascal_triangle<T>(size: usize) -> Vec<Vec<T>>
where
    T: std::ops::Add<Output = T> + From<u64> + Clone,
{
    let mut p = (0..size)
        .map(|i| vec![1.into(); i + 1])
        .collect::<Vec<Vec<T>>>();
    for i in 1..size {
        for j in 1..i {
            p[i][j] = p[i - 1][j - 1].clone() + p[i - 1][j].clone();
        }
        // p[i][i] = 1 is already initialized.
    }
    p
}

pub struct PascalRule<T> {
    cache: std::collections::HashMap<u64, T>,
}

impl<T> PascalRule<T>
where
    T: std::ops::Add<Output = T> + From<usize> + Copy,
{
    pub fn new() -> Self {
        Self {
            cache: std::collections::HashMap::new(),
        }
    }

    /// interface is not u64 but u32
    /// to avoid key's overflow but memory overflow or infinite run time.
    /// memory overflow should not be handled here (low level API).
    pub fn calc(&mut self, n: u32, k: u32) -> T {
        assert!(k <= n);
        // unlike combination, (n, k) is undefined if k > n
        // on pascal's triangle.
        if k == 0 {
            return 1.into();
        }
        let key = (n as u64) << 32 | k as u64;
        if !self.cache.contains_key(&key) {
            let mut v = self.calc(n - 1, k - 1);
            if k < n {
                v = v + self.calc(n - 1, k);
            }
            self.cache.insert(key, v);
        }
        *self.cache.get(&key).unwrap()
    }
}

#[derive(Debug)]
pub struct NegativeCycleError {
    msg: &'static str,
}

impl NegativeCycleError {
    fn new() -> Self { Self { msg: "Negative Cycle Found." } }
}

impl std::fmt::Display for NegativeCycleError {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        write!(f, "{}", self.msg)
    }
}

impl std::error::Error for NegativeCycleError {
    fn description(&self) -> &str { &self.msg }
}

pub fn floyd_warshall(
    mut weight_matrix: Vec<Vec<i64>>,
) -> Result<Vec<Vec<i64>>, NegativeCycleError> {
    let n = weight_matrix.len();
    assert!((0..n).all(|i| weight_matrix[i].len() == n));
    (0..n).for_each(|i| {
        weight_matrix[i][i] = std::cmp::min(weight_matrix[i][i], 0)
    });
    (0..n).for_each(|k| {
        (0..n).for_each(|i| {
            (0..n).for_each(|j| {
                weight_matrix[i][j] = std::cmp::min(
                    weight_matrix[i][j],
                    weight_matrix[i][k] + weight_matrix[k][j],
                );
            });
        });
    });
    if (0..n).any(|i| weight_matrix[i][i] < 0) {
        Err(NegativeCycleError::new())
    } else {
        Ok(weight_matrix)
    }
}

pub fn solve_ghost_leg(n: usize, edges: Vec<usize>) -> Vec<usize> {
    let mut res = (0..n).collect::<Vec<_>>();
    for &i in edges.iter().rev() {
        res.swap(i, i + 1);
    }
    res
}

pub fn bit_length(n: u64) -> u8 {
    (0u64.leading_zeros() - n.leading_zeros()) as u8
}

pub fn msb(n: u64) -> usize {
    assert!(n > 0);
    // it's trivial msb of 0 is undefined.
    // if n = 0, it's wrong with the caller.
    bit_length(n) as usize - 1
}

pub fn tree_edges_with_data_to_graph<T>(
    tree_edges: &[(usize, usize, T)],
) -> Vec<Vec<(usize, T)>>
where
    T: Clone,
{
    let mut graph = vec![vec![]; tree_edges.len() + 1];
    for &(u, v, ref data) in tree_edges {
        graph[u].push((v, data.clone()));
        graph[v].push((u, data.clone()));
    }
    graph
}

pub fn tree_edges_to_graph(tree_edges: &[(usize, usize)]) -> Vec<Vec<usize>> {
    tree_edges_with_data_to_graph(
        tree_edges
            .iter()
            .map(|&(u, v)| (u, v, ()))
            .collect::<Vec<_>>()
            .as_slice(),
    )
    .iter()
    .map(|edges| edges.iter().map(|&(v, _)| v).collect())
    .collect()
}

pub fn tree_bfs<T, F>(
    tree_edges: &[(usize, usize)],
    root: usize,
    default_data: Vec<T>,
    mut assign: F,
) -> Vec<T>
where
    F: FnMut(&mut Vec<T>, usize, usize),
{
    let graph = tree_edges_to_graph(tree_edges);
    let n = graph.len();
    assert!(default_data.len() == n);
    let mut que = std::collections::VecDeque::new();
    let mut parent = vec![None; n];
    let mut data = default_data;
    que.push_back(root);
    while let Some(u) = que.pop_front() {
        for &v in graph[u].iter() {
            if Some(v) == parent[u] {
                continue;
            }
            parent[v] = Some(u);
            assign(&mut data, u, v);
            que.push_back(v);
        }
    }
    data
}

pub fn tree_parents(
    tree_edges: &[(usize, usize)],
    root: usize,
) -> Vec<Option<usize>> {
    tree_bfs::<Option<usize>, _>(
        tree_edges,
        root,
        vec![None; tree_edges.len() + 1],
        |parent, u, v| {
            parent[v] = Some(u);
        },
    )
}

pub fn tree_depths(tree_edges: &[(usize, usize)], root: usize) -> Vec<usize> {
    tree_bfs::<usize, _>(
        tree_edges,
        root,
        vec![0; tree_edges.len() + 1],
        |depth, u, v| {
            depth[v] = depth[u] + 1;
        },
    )
}

/// we don't check if the given edges as a whole making a tree or not.
/// because the algorithm might be expensive even if O(N).
/// if not graph, the processes is undefined.
/// similary, we assure that the default data length
/// is equial to the number of vertices.
pub fn tree_dfs<T, F>(
    tree_edges: &[(usize, usize)],
    root: usize,
    default_data: Vec<T>,
    mut assign: F,
) -> Vec<T>
where
    F: FnMut(&mut Vec<T>, usize, usize),
{
    let graph = tree_edges_to_graph(tree_edges);
    let n = graph.len();
    assert!(default_data.len() == n);
    let mut parent = vec![None; n];
    let mut data = default_data;
    let mut stack: Vec<isize> = Vec::new();
    stack.push(root as isize);
    while let Some(u) = stack.pop() {
        if u < 0 {
            let u = !u as usize;
            if let Some(p) = parent[u] {
                assign(&mut data, p, u);
            }
            continue;
        }
        stack.push(!u);
        let u = u as usize;
        for &v in graph[u].iter() {
            if Some(v) == parent[u] {
                continue;
            }
            parent[v] = Some(u);
            stack.push(v as isize);
        }
    }
    data
}

pub fn tree_sizes(tree_edges: &[(usize, usize)], root: usize) -> Vec<usize> {
    tree_dfs::<usize, _>(
        tree_edges,
        root,
        vec![1; tree_edges.len() + 1],
        |size, u, v| {
            size[u] += size[v];
        },
    )
}

#[derive(Debug)]
pub struct UnionFind {
    data: Vec<isize>,
}

impl UnionFind {
    pub fn new(size: usize) -> Self { Self { data: vec![-1; size] } }

    pub fn size(&self) -> usize { self.data.len() }

    pub fn find_root(&mut self, u: usize) -> usize {
        if self.data[u] < 0 {
            return u;
        }
        self.data[u] = self.find_root(self.data[u] as usize) as isize;
        self.data[u] as usize
    }

    pub fn unite(&mut self, u: usize, v: usize) {
        let mut u = self.find_root(u);
        let mut v = self.find_root(v);
        if u == v {
            return;
        }
        if self.data[u] > self.data[v] {
            std::mem::swap(&mut u, &mut v);
        }
        self.data[u] += self.data[v];
        self.data[v] = u as isize;
    }

    pub fn size_of(&mut self, u: usize) -> usize {
        let u = self.find_root(u);
        -self.data[u] as usize
    }
}

pub struct LCABinaryLifting {
    ancestors: Vec<Vec<usize>>,
    depth: Vec<usize>,
}

impl LCABinaryLifting {
    pub fn new(tree_edges: &[(usize, usize)], root: usize) -> Self {
        let n = tree_edges.len() + 1;
        let depth = tree_depths(&tree_edges, root);
        let k = std::cmp::max(
            1,
            bit_length(*depth.iter().max().unwrap() as u64),
        ) as usize;
        let mut ancestors = vec![vec![n; n]; k];
        let mut parent = tree_parents(&tree_edges, root);
        parent[root] = Some(root);
        ancestors[0] = parent.iter().map(|&v| v.unwrap()).collect();
        for i in 0..k - 1 {
            for j in 0..n {
                ancestors[i + 1][j] = ancestors[i][ancestors[i][j]];
            }
        }
        Self { ancestors, depth }
    }

    pub fn get(&self, mut u: usize, mut v: usize) -> usize {
        if self.depth[u] > self.depth[v] {
            std::mem::swap(&mut u, &mut v);
        }
        let d = self.depth[v] - self.depth[u];
        for i in 0..bit_length(d as u64) as usize {
            if d >> i & 1 == 1 {
                v = self.ancestors[i][v];
            }
        }
        if v == u {
            return u;
        }
        for a in self.ancestors.iter().rev() {
            let nu = a[u];
            let nv = a[v];
            if nu != nv {
                u = nu;
                v = nv;
            }
        }
        self.ancestors[0][u]
    }
}

pub fn offline_lca_tarjan(
    tree_edges: &[(usize, usize)],
    queries: &[(usize, usize)],
    root: usize,
) -> Vec<usize> {
    fn dfs(
        g: &Vec<Vec<usize>>,
        q: &Vec<Vec<(usize, usize)>>,
        visited: &mut Vec<bool>,
        uf: &mut UnionFind,
        ancestor: &mut Vec<usize>,
        lca: &mut Vec<usize>,
        u: usize,
    ) {
        visited[u] = true;
        ancestor[u] = u;
        for &v in g[u].iter() {
            if visited[v] {
                continue;
            }
            dfs(
                g, q, visited, uf, ancestor, lca, v,
            );
            uf.unite(u, v);
            ancestor[uf.find_root(u)] = u;
        }
        q[u].iter().filter(|&&(v, _)| visited[v]).for_each(|&(v, i)| {
            lca[i] = ancestor[uf.find_root(v)];
        });
    }
    let n = tree_edges.len() + 1;
    let graph = tree_edges_to_graph(tree_edges);
    let mut q = vec![vec![]; n];
    for (i, &(u, v)) in queries.iter().enumerate() {
        q[u].push((v, i));
        q[v].push((u, i));
    }
    let mut visited = vec![false; n];
    let mut uf = UnionFind::new(n);
    let mut ancestor = vec![n; n];
    let mut lca = vec![n; queries.len()];
    dfs(
        &graph,
        &q,
        &mut visited,
        &mut uf,
        &mut ancestor,
        &mut lca,
        root,
    );
    lca
}

pub fn heavy_light_decompose(
    tree_edges: &[(usize, usize)],
    root: usize,
) -> Vec<usize> {
    let graph = tree_edges_to_graph(tree_edges);
    let n = graph.len();
    let mut roots = (0..n).collect::<Vec<_>>();
    let sizes = tree_sizes(tree_edges, root);
    let mut stack = vec![(root, root)];
    while let Some((u, parent)) = stack.pop() {
        let mut heavy_node = None;
        let mut max_size = 0;
        graph[u].iter().filter(|&&v| v != parent).for_each(|&v| {
            if sizes[v] > max_size {
                max_size = sizes[v];
                heavy_node = Some(v);
            }
        });
        graph[u].iter().filter(|&&v| v != parent).for_each(|&v| {
            if Some(v) == heavy_node {
                roots[v] = roots[u];
            }
            stack.push((v, u));
        });
    }
    roots
}

pub struct LCAHLD {
    parent: Vec<Option<usize>>,
    depth: Vec<usize>,
    roots: Vec<usize>,
}

impl LCAHLD {
    pub fn new(tree_edges: &[(usize, usize)], root: usize) -> Self {
        Self {
            parent: tree_parents(tree_edges, root),
            depth: tree_depths(tree_edges, root),
            roots: heavy_light_decompose(tree_edges, root),
        }
    }

    pub fn get(&self, mut u: usize, mut v: usize) -> usize {
        while self.roots[u] != self.roots[v] {
            if self.depth[self.roots[u]] > self.depth[self.roots[v]] {
                std::mem::swap(&mut u, &mut v);
            }
            v = self.parent[self.roots[v]].unwrap();
        }
        if self.depth[u] <= self.depth[v] { u } else { v }
    }
}

pub fn euler_tour_edges(
    tree_edges: &[(usize, usize)],
    root: usize,
) -> Vec<isize> {
    let graph = tree_edges_to_graph(tree_edges);
    let n = graph.len();
    let mut parent = vec![None; n];
    let mut tour = Vec::with_capacity(n << 1);
    let mut stack = vec![root as isize];
    for _ in 0..n << 1 {
        let u = stack.pop().unwrap();
        tour.push(u);
        if u < 0 {
            continue;
        }
        stack.push(!u);
        let u = u as usize;
        graph[u].iter().rev().for_each(|&v| {
            if Some(v) != parent[u] {
                parent[v] = Some(u);
                stack.push(v as isize);
            }
        });
    }
    tour
}

pub fn euler_tour_nodes(
    tree_edges: &[(usize, usize)],
    root: usize,
) -> Vec<usize> {
    let parent = tree_parents(tree_edges, root);
    euler_tour_edges(tree_edges, root)
        .iter()
        .rev()
        .skip(1)
        .rev()
        .map(
            |&u| {
                if u < 0 { parent[!u as usize].unwrap() } else { u as usize }
            },
        )
        .collect()
}

pub fn last_positions(tour_nodes: &[usize]) -> Vec<usize> {
    let n = tour_nodes.iter().max().unwrap() + 1;
    let mut pos = vec![None; n];
    tour_nodes
        .iter()
        .enumerate()
        .for_each(|(i, &u)| pos[u] = Some(i));
    pos.iter().map(|&p| p.unwrap()).collect()
}

pub fn first_positions(tour_nodes: &[usize]) -> Vec<usize> {
    let size = tour_nodes.len();
    let mut tour = tour_nodes.to_vec();
    tour.reverse();
    last_positions(&tour).iter().map(|&i| size - i - 1).collect()
}

pub trait RangeMinimumQuery<T> {
    fn query(&mut self, l: usize, r: usize) -> T;
}

pub struct LCAEulerTourRMQ<Q> {
    first_pos: Vec<usize>,
    rmq: Q,
}

impl<Q> LCAEulerTourRMQ<Q> {
    pub fn new(tree_edges: &[(usize, usize)], root: usize) -> Self
    where
        Q: std::iter::FromIterator<(usize, usize)>,
    {
        let tour_nodes = euler_tour_nodes(tree_edges, root);
        let depth = tree_depths(tree_edges, root);
        let first_pos = first_positions(&tour_nodes);
        let depth = tour_nodes.iter().map(|&u| depth[u]).collect::<Vec<_>>();
        let rmq = Q::from_iter(depth.into_iter().zip(tour_nodes.into_iter()));
        Self { first_pos, rmq }
    }

    pub fn get(&mut self, u: usize, v: usize) -> usize
    where
        Q: RangeMinimumQuery<(usize, usize)>,
    {
        let mut left = self.first_pos[u];
        let mut right = self.first_pos[v];
        if left > right {
            std::mem::swap(&mut left, &mut right);
        }
        self.rmq.query(left, right + 1).1
    }
}

impl BinaryOperations<Min> for (usize, usize) {
    type Codomain = Self;
    type Lhs = Self;
    type Rhs = Self;

    fn operate(lhs: Self::Lhs, rhs: Self::Rhs) -> Self::Codomain {
        std::cmp::min(lhs, rhs)
    }
}

impl AssociativeProperties<Min> for (usize, usize) {
    type X = Self;
}

impl IdentityElements<Min> for (usize, usize) {
    type X = Self;

    fn identity() -> Self::X {
        (
            std::usize::MAX,
            std::usize::MAX,
        )
    }
}

impl CommutativeProperties<Min> for (usize, usize) {
    type X = Self;
}

impl Idempotences<Min> for (usize, usize) {
    type X = Self;
}

pub fn least_significant_bit(n: u64) -> Option<usize> {
    if n == 0 { None } else { Some(n.trailing_zeros() as usize) }
}

use std::iter::FromIterator;

pub struct SegmentTree<M: Monoids<Id>, Id> {
    // phantom: std::marker::PhantomData<(Id, M)>,
    size: usize,
    data: Vec<M::S>,
}

impl<M, Id> std::iter::FromIterator<M::S> for SegmentTree<M, Id>
where
    M::S: Clone,
    M: Monoids<Id>,
{
    fn from_iter<T: IntoIterator<Item = M::S>>(iter: T) -> Self {
        let mut data = iter.into_iter().collect::<Vec<_>>();
        let size = data.len();
        let n = size.next_power_of_two();
        data = (0..n)
            .map(|_| M::identity())
            .chain(data.into_iter())
            .chain((0..n - size).map(|_| M::identity()))
            .collect::<Vec<_>>();
        let mut seg = Self { size, data };
        (1..n).rev().for_each(|i| seg.update(i));
        seg
    }
}

impl<M, Id> From<&[M::S]> for SegmentTree<M, Id>
where
    Self: std::iter::FromIterator<M::S>,
    M::S: Clone,
    M: Monoids<Id>,
{
    fn from(slice: &[M::S]) -> Self { Self::from_iter(slice.iter().cloned()) }
}

impl<M, Id> SegmentTree<M, Id>
where
    M: Monoids<Id>,
{
    pub fn size(&self) -> usize { self.size }

    fn n(&self) -> usize { self.data.len() >> 1 }
}

impl<M, Id> SegmentTree<M, Id>
where
    M::S: Clone,
    M: Monoids<Id>,
{
    pub fn new<F>(size: usize, default: F) -> Self
    where
        F: Fn() -> M::S,
    {
        Self::from_iter((0..size).map(|_| default()))
    }

    fn update(&mut self, i: usize) {
        self.data[i] = M::operate(
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

    pub fn reduce(&self, mut l: usize, mut r: usize) -> M::S {
        assert!(l < r && r <= self.size);
        let n = self.n();
        l += n;
        r += n;
        let mut vl = M::identity();
        let mut vr = M::identity();
        while l < r {
            if l & 1 == 1 {
                vl = M::operate(vl, self.data[l].clone());
                l += 1;
            }
            if r & 1 == 1 {
                r -= 1;
                vr = M::operate(self.data[r].clone(), vr);
            }
            l >>= 1;
            r >>= 1;
        }
        M::operate(vl, vr)
    }
}

impl<M, Id> SegmentTree<M, Id>
where
    M::S: Clone,
    M: Monoids<Id>,
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
        let mut v = M::identity();
        let mut i = l + n;
        assert_ne!(i, 0);
        loop {
            i >>= i.trailing_zeros(); // upstream
            let nv = M::operate(v.clone(), self.data[i].clone());
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
            let nv = M::operate(v.clone(), self.data[i].clone());
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
        let mut v = M::identity();
        let mut i = r + n;
        assert_ne!(i, 0);
        loop {
            i >>= i.trailing_zeros(); // upstream
            let nv = M::operate(
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
            let nv = M::operate(
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

impl<M, Id> std::ops::Index<usize> for SegmentTree<M, Id>
where
    M: Monoids<Id>,
{
    type Output = M::S;

    fn index(&self, i: usize) -> &Self::Output {
        assert!(i < self.size);
        &self.data[i + self.n()]
    }
}

impl<M, Id> SegmentTree<M, Id>
where
    M::S: Clone,
    M: Monoids<Id>,
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
            return M::identity();
        }
        if l <= cur_l && cur_r <= r {
            return self.data[i].clone();
        }
        let c = (cur_l + cur_r) >> 1;
        M::operate(
            self._reduce_recurse(l, r, cur_l, c, i << 1),
            self._reduce_recurse(l, r, c, cur_r, i << 1 | 1),
        )
    }
}

impl<M, Id> SegmentTree<M, Id>
where
    M::S: Clone,
    M: Monoids<Id>,
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
            &mut M::identity(),
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
        let nv = M::operate(v.clone(), self.data[i].clone());
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
            &mut M::identity(),
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
        let nv = M::operate(self.data[i].clone(), v.clone());
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

impl RangeMinimumQuery<(usize, usize)> for SegmentTree<(usize, usize), Min> {
    fn query(&mut self, l: usize, r: usize) -> (usize, usize) {
        self.reduce(l, r)
    }
}

#[allow(dead_code)]
type LCAEulerTourRMQSegTree = LCAEulerTourRMQ<SegmentTree<(usize, usize), Min>>;

pub struct SparseTable<G: Semigroups<Id>, Id> {
    data: Vec<Vec<G::S>>,
}

impl<G, Id> std::iter::FromIterator<G::S> for SparseTable<G, Id>
where
    G: Semigroups<Id>
        + Idempotences<Id, X = G::S>
        + CommutativeProperties<Id, X = G::S>,
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

impl<G, Id> SparseTable<G, Id>
where
    G: Semigroups<Id>
        + Idempotences<Id, X = G::S>
        + CommutativeProperties<Id, X = G::S>,
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

impl RangeMinimumQuery<(usize, usize)> for SparseTable<(usize, usize), Min> {
    fn query(&mut self, l: usize, r: usize) -> (usize, usize) {
        self.reduce(l, r)
    }
}

#[allow(dead_code)]
type LCAEulerTourRMQSparseTable =
    LCAEulerTourRMQ<SparseTable<(usize, usize), Min>>;

pub struct DisjointSparseTable<G: Semigroups<Id>, Id> {
    data: Vec<Vec<G::S>>,
}

impl<G, Id> std::iter::FromIterator<G::S> for DisjointSparseTable<G, Id>
where
    G: Semigroups<Id> + CommutativeProperties<Id, X = G::S>,
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
    G: Semigroups<Id> + CommutativeProperties<Id, X = G::S>,
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

impl RangeMinimumQuery<(usize, usize)>
    for DisjointSparseTable<(usize, usize), Min>
{
    fn query(&mut self, l: usize, r: usize) -> (usize, usize) {
        self.reduce(l, r)
    }
}

#[allow(dead_code)]
type LCAEulerTourRMQDisjointSparseTable =
    LCAEulerTourRMQ<DisjointSparseTable<(usize, usize), Min>>;

pub fn floor_sqrt(n: u64) -> u64 {
    let mut lo = 0;
    let mut hi = 1 << 32;
    while hi - lo > 1 {
        let x = (lo + hi) / 2;
        if n / x >= x {
            lo = x;
        } else {
            hi = x;
        }
    }
    lo
}

pub struct SqrtDecomposition<G: Semigroups<Id>, Id> {
    pub(crate) data: Vec<G::S>,
    pub(crate) buckets: Vec<G::S>,
}

impl<G, Id> SqrtDecomposition<G, Id>
where
    G: Semigroups<Id>,
{
    pub fn size(&self) -> usize { self.data.len() }

    pub(crate) fn sqrt(&self) -> usize {
        let n = self.buckets.len();
        (self.size() + n - 1) / n
    }
}

impl<G, Id> std::iter::FromIterator<G::S> for SqrtDecomposition<G, Id>
where
    G: Semigroups<Id>,
    G::S: Clone,
{
    fn from_iter<T: IntoIterator<Item = G::S>>(iter: T) -> Self {
        let data = iter.into_iter().collect::<Vec<_>>();
        let size = data.len();
        let n = floor_sqrt(size as u64) as usize;
        let buckets = (0..(size + n - 1) / n)
            .map(|j| {
                // data[j * n..std::cmp::min((j + 1) * n, size)]
                //     .iter()
                //     .cloned()
                //     .reduce(|l, r| G::operate(l, r))
                //     .unwrap()
                // CHANGE LATER: reduce is not supported on atcoder yet.

                let mut iter = data[j * n..std::cmp::min((j + 1) * n, size)]
                    .iter()
                    .cloned();
                let mut v = iter.next().unwrap();
                for x in iter {
                    v = G::operate(v, x);
                }
                v
            })
            .collect();
        Self { data, buckets }
    }
}

impl<G, Id> SqrtDecomposition<G, Id>
where
    G: Semigroups<Id>,
    G::S: Clone,
{
    pub(crate) fn update(&mut self, bucket: usize) {
        let j = bucket;
        let n = self.sqrt();
        // self.buckets[j] = self.data
        //     [j * n..std::cmp::min((j + 1) * n, self.size())]
        //     .iter()
        //     .cloned()
        //     .reduce(|l, r| G::operate(l, r))
        //     .unwrap();
        // CHANGE LATER: reduce is not supported on atcoder yet.
        let mut iter = self.data
            [j * n..std::cmp::min((j + 1) * n, self.size())]
            .iter()
            .cloned();
        let mut v = iter.next().unwrap();
        for x in iter {
            v = G::operate(v, x);
        }
        self.buckets[j] = v;
    }

    // move out from core implementation later.
    pub fn apply<F>(&mut self, i: usize, f: F)
    where
        F: FnOnce(&G::S) -> G::S,
    {
        self.data[i] = f(&self.data[i]);
        self.update(i / self.sqrt());
    }

    // move out from core implementation later.
    pub fn set(&mut self, i: usize, x: G::S) {
        self.apply(i, |_| x);
        self.update(i / self.sqrt());
    }

    pub fn reduce(&self, l: usize, r: usize) -> G::S {
        assert!(l < r && r <= self.size());
        // just for early panic. it's not necessary to be checked here.
        let n = self.sqrt();
        // (0..self.buckets.len())
        //     .filter_map(|j| {
        //         if r <= n * j || n * (j + 1) <= l {
        //             return None;
        //         }
        //         if l <= n * j && n * (j + 1) <= r {
        //             return Some(self.buckets[j].clone());
        //         }
        //         (0..n)
        //             .filter_map(|k| {
        //                 let i = j * n + k;
        //                 if l <= i && i < r {
        //                     Some(self.data[i].clone())
        //                 } else {
        //                     None
        //                 }
        //             })
        //             .reduce(|l, r| G::operate(l, r))
        //     })
        //     .reduce(|l, r| G::operate(l, r))
        // CHANGE LATER: reduce is not supported on atcoder yet.

        let mut iter = (0..self.buckets.len()).filter_map(|j| {
            if r <= n * j || n * (j + 1) <= l {
                return None;
            }
            if l <= n * j && n * (j + 1) <= r {
                return Some(self.buckets[j].clone());
            }

            let mut iter = (0..n).filter_map(|k| {
                let i = j * n + k;
                if l <= i && i < r { Some(self.data[i].clone()) } else { None }
            });
            let mut v = iter.next().unwrap();
            for x in iter {
                v = G::operate(v, x);
            }
            Some(v)
        });
        let mut v = iter.next().unwrap();
        for x in iter {
            v = G::operate(v, x);
        }
        v
    }
}

impl<G, Id> SqrtDecomposition<G, Id>
where
    G: Semigroups<Id>,
    G::S: Clone,
{
    /// faster with constant time optimization.
    pub fn fast_reduce(&self, mut l: usize, r: usize) -> G::S {
        assert!(l < r && r <= self.size());
        let n = self.sqrt();
        let mut v = self.data[l].clone();
        l += 1;
        let lj = (l + n - 1) / n;
        let rj = r / n;
        if rj < lj {
            for i in l..r {
                v = G::operate(v, self.data[i].clone());
            }
            return v;
        }
        for i in l..lj * n {
            v = G::operate(v, self.data[i].clone());
        }
        for j in lj..rj {
            v = G::operate(v, self.buckets[j].clone());
        }
        for i in rj * n..r {
            v = G::operate(v, self.data[i].clone());
        }
        v
    }
}

// TODO: set_range (lazy sqrt decomp)

impl RangeMinimumQuery<(usize, usize)>
    for SqrtDecomposition<(usize, usize), Min>
{
    fn query(&mut self, l: usize, r: usize) -> (usize, usize) {
        self.fast_reduce(l, r)
    }
}

#[allow(dead_code)]
type LCAEulerTourRMQSqrtDecomposition =
    LCAEulerTourRMQ<SqrtDecomposition<(usize, usize), Min>>;

// #[allow(warnings)]
fn main() -> Result<(), Box<dyn std::error::Error>> {
    use std::io::Write;
    let mut reader = locked_stdin_reader();
    let mut writer = locked_stdin_buf_writer();

    let n: usize = reader.read()?;
    let edges = (0..n - 1)
        .map(|_| {
            let x = reader.read::<usize>().unwrap() - 1;
            let y = reader.read::<usize>().unwrap() - 1;
            (x, y)
        })
        .collect::<Vec<_>>();

    // let lca = LCABinaryLifting::new(edges.as_slice(), 0);
    // let lca = LCAHLD::new(&edges, 0);
    // let mut lca = LCAEulerTourRMQSegTree::new(&edges, 0);
    // let mut lca = LCAEulerTourRMQSparseTable::new(&edges, 0);
    // let mut lca = LCAEulerTourRMQDisjointSparseTable::new(&edges, 0);
    let mut lca = LCAEulerTourRMQSqrtDecomposition::new(&edges, 0);

    let depth = tree_depths(edges.as_slice(), 0);

    let mut dist =
        |u: usize, v: usize| depth[u] + depth[v] - depth[lca.get(u, v)] * 2;
    let q: usize = reader.read()?;
    (0..q).for_each(|_| {
        let u = reader.read::<usize>().unwrap() - 1;
        let v = reader.read::<usize>().unwrap() - 1;
        writeln!(writer, "{}", dist(u, v) + 1).unwrap();
    });

    // let queries = (0..q)
    //     .map(|_| {
    //         let u = reader.read::<usize>().unwrap() - 1;
    //         let v = reader.read::<usize>().unwrap() - 1;
    //         (u, v)
    //     })
    //     .collect::<Vec<_>>();

    // let lca = offline_lca_tarjan(&edges, &queries, 0);
    // (0..q).for_each(|i| {
    //     let (u, v) = queries[i];
    //     writeln!(writer, "{}", depth[u] + depth[v] - depth[lca[i]] * 2 +
    // 1).unwrap(); });

    writer.flush()?;
    Ok(())

    // TODO: add Generic Type F to segment tree for applying.
    // replace set(i, x) -> apply(i, x) and apply function of type F
    // and set(i, x) is gonnabe an extension for segment tree but primitime core
    // API. consider dual segment tree and lazy segment tree similarly.

    // TODO: dual segment tree
    // TODO: lazy segment tree
    // TODO: lazy sqrt decomposition
    // TODO: fenwick tree
    // TODO: dual fenwick tree
}

pub trait BinaryOperationId {}

pub trait BinaryOperations<Id>
where
    Id: BinaryOperationId,
{
    type Lhs;
    type Rhs;
    type Codomain;
    fn operate(l: Self::Lhs, r: Self::Rhs) -> Self::Codomain;
}

pub trait AssociativeProperties<Id>:
    BinaryOperations<Id, Lhs = Self::X, Rhs = Self::X, Codomain = Self::X>
where
    Id: BinaryOperationId,
{
    type X;

    /// we don't return boolean result
    /// because it's validating rather than testing.
    /// users implementing this trait must assure
    /// that the operation is associative.
    fn assert_associative(first: Self::X, second: Self::X, third: Self::X)
    where
        Self::X: Clone + PartialEq + std::fmt::Debug,
    {
        assert_eq!(
            Self::operate(
                Self::operate(first.clone(), second.clone()),
                third.clone()
            ),
            Self::operate(
                first,
                Self::operate(second, third)
            ),
        );
    }
}

pub trait Idempotences<Id>:
    BinaryOperations<Id, Lhs = Self::X, Rhs = Self::X, Codomain = Self::X>
where
    Id: BinaryOperationId,
{
    type X;
    fn assert_idempotent(element: Self::X)
    where
        Self::X: Clone + PartialEq + std::fmt::Debug,
    {
        assert_eq!(
            Self::operate(
                element.clone(),
                element.clone()
            ),
            element
        );
    }
}

pub trait CommutativeProperties<Id>:
    BinaryOperations<Id, Lhs = Self::X, Rhs = Self::X>
where
    Id: BinaryOperationId,
{
    type X;

    fn assert_commutative(l: Self::X, r: Self::X)
    where
        Self::Codomain: PartialEq + std::fmt::Debug,
        Self::X: Clone,
    {
        assert_eq!(
            Self::operate(l.clone(), r.clone()),
            Self::operate(r, l)
        );
    }
}

pub trait IdentityElements<Id>:
    BinaryOperations<Id, Lhs = Self::X, Rhs = Self::X, Codomain = Self::X>
where
    Id: BinaryOperationId,
{
    type X;
    fn identity() -> Self::X;

    fn assert_identity(element: Self::X)
    where
        Self::X: Clone + PartialEq + std::fmt::Debug,
    {
        assert_eq!(
            Self::operate(
                Self::identity(),
                element.clone(),
            ),
            element
        );
        assert_eq!(
            Self::operate(
                element.clone(),
                Self::identity()
            ),
            element
        );
    }
}

pub trait InverseElements<Id>: IdentityElements<Id>
where
    Id: BinaryOperationId,
{
    fn invert(element: Self::X) -> Self::X;
}

pub trait Magmas<Id>:
    BinaryOperations<Id, Lhs = Self::S, Rhs = Self::S, Codomain = Self::S>
where
    Id: BinaryOperationId,
{
    type S;
}

impl<S, Id, T> Magmas<Id> for T
where
    T: BinaryOperations<Id, Lhs = S, Rhs = S, Codomain = S>,
    Id: BinaryOperationId,
{
    type S = S;
}
pub trait Semigroups<Id>:
    Magmas<Id> + AssociativeProperties<Id, X = Self::S>
where
    Id: BinaryOperationId,
{
}

impl<Id, T> Semigroups<Id> for T
where
    T: Magmas<Id> + AssociativeProperties<Id, X = Self::S>,
    Id: BinaryOperationId,
{
}

pub trait Monoids<Id>:
    Semigroups<Id> + IdentityElements<Id, X = Self::S>
where
    Id: BinaryOperationId,
{
}

impl<Id, T> Monoids<Id> for T
where
    T: Semigroups<Id> + IdentityElements<Id, X = Self::S>,
    Id: BinaryOperationId,
{
}

pub trait CommutativeMonoids<Id>:
    Monoids<Id> + CommutativeProperties<Id, X = Self::S>
where
    Id: BinaryOperationId,
{
}
impl<Id, T> CommutativeMonoids<Id> for T
where
    T: Monoids<Id> + CommutativeProperties<Id, X = Self::S>,
    Id: BinaryOperationId,
{
}

pub trait Groups<Id>: Monoids<Id> + InverseElements<Id, X = Self::S>
where
    Id: BinaryOperationId,
{
}
impl<Id, T> Groups<Id> for T
where
    T: Monoids<Id> + InverseElements<Id, X = Self::S>,
    Id: BinaryOperationId,
{
}

pub trait AbelianGroups<Id>:
    Groups<Id> + CommutativeProperties<Id, X = Self::S>
where
    Id: BinaryOperationId,
{
}

impl<Id, T> AbelianGroups<Id> for T
where
    T: Groups<Id> + CommutativeProperties<Id, X = Self::S>,
    Id: BinaryOperationId,
{
}

pub trait Semirings<Add, Mul>:
    CommutativeMonoids<Add> + Monoids<Mul, S = <Self as Magmas<Add>>::S>
where
    Add: BinaryOperationId,
    Mul: BinaryOperationId,
{
}

impl<Add, Mul, T> Semirings<Add, Mul> for T
where
    T: CommutativeMonoids<Add> + Monoids<Mul, S = <Self as Magmas<Add>>::S>,
    Add: BinaryOperationId,
    Mul: BinaryOperationId,
{
}

pub trait Rings<Add, Mul>: Semirings<Add, Mul> + IdentityElements<Add>
where
    Add: BinaryOperationId,
    Mul: BinaryOperationId,
{
}

impl<Add, Mul, T> Rings<Add, Mul> for T
where
    T: Semirings<Add, Mul> + IdentityElements<Add>,
    Add: BinaryOperationId,
    Mul: BinaryOperationId,
{
}

impl<T> BinaryOperationId for T {}

pub trait AdditiveGroups: AbelianGroups<Additive> {}
impl<T> AdditiveGroups for T where T: AbelianGroups<Additive> {}
