pub struct ReadWrapper<R: std::io::BufRead> {
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
impl<R: std::io::BufRead> ReadWrapper<R> {
    pub fn new(reader: R) -> Self { Self { reader, tokens: vec![] } }

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

pub trait BinaryOperation<Lhs, Rhs, Codomain, Id> {
    fn operate(lhs: Lhs, rhs: Rhs) -> Codomain;
}

pub trait AssociativeProperty<S, Id>: BinaryOperation<S, S, S, Id> {
    fn assert_associative(first: S, second: S, third: S)
    where
        S: Clone + PartialEq + std::fmt::Debug,
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

pub trait Idempotence<S, Id>: BinaryOperation<S, S, S, Id> {
    fn assert_idempotent(element: S)
    where
        S: Clone + PartialEq + std::fmt::Debug,
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

pub trait CommutativeProperty<S, T, Id>: BinaryOperation<S, S, T, Id> {
    fn assert_commutative(a: S, b: S)
    where
        S: Clone,
        T: PartialEq + std::fmt::Debug,
    {
        assert_eq!(
            Self::operate(a.clone(), b.clone()),
            Self::operate(b, a)
        );
    }
}

pub trait IdentityElement<S, Id>: BinaryOperation<S, S, S, Id> {
    fn identity() -> S;
}

pub trait InverseElement<S, Id>: IdentityElement<S, Id> {
    fn invert(element: S) -> S;
}

pub trait Magma<S, Id>: BinaryOperation<S, S, S, Id> {}
impl<S, Id, T> Magma<S, Id> for T where T: BinaryOperation<S, S, S, Id> {}

pub trait Semigroup<S, Id>: Magma<S, Id> + AssociativeProperty<S, Id> {}

impl<S, Id, T> Semigroup<S, Id> for T where
    T: Magma<S, Id> + AssociativeProperty<S, Id>
{
}

pub trait Monoid<S, Id>: Semigroup<S, Id> + IdentityElement<S, Id> {}
impl<S, Id, T> Monoid<S, Id> for T where
    T: Semigroup<S, Id> + IdentityElement<S, Id>
{
}

pub trait CommutativeMonoid<S, Id>:
    Monoid<S, Id> + CommutativeProperty<S, S, Id> + Sized
{
}
impl<S, Id, T> CommutativeMonoid<S, Id> for T where
    T: Monoid<S, Id> + CommutativeProperty<S, S, Id>
{
}

pub trait Group<S, Id>: Monoid<S, Id> + InverseElement<S, Id> {}

impl<S, Id, T: Monoid<S, Id> + InverseElement<S, Id>> Group<S, Id> for T {}

pub trait AbelianGroup<S, Id>:
    Group<S, Id> + CommutativeProperty<S, S, Id>
{
}
impl<S, Id, T> AbelianGroup<S, Id> for T where
    T: Group<S, Id> + CommutativeProperty<S, S, Id>
{
}

pub trait Semiring<S, Add, Mul>:
    CommutativeMonoid<S, Add> + Monoid<S, Mul>
{
}
impl<S, Add, Mul, T> Semiring<S, Add, Mul> for T where
    T: CommutativeMonoid<S, Add> + Monoid<S, Mul>
{
}

pub trait Ring<S, Add, Mul>:
    Semiring<S, Add, Mul> + IdentityElement<S, Add>
{
}
impl<S, Add, Mul, T> Ring<S, Add, Mul> for T where
    T: Semiring<S, Add, Mul> + IdentityElement<S, Add>
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
pub fn extgcd_modinv(modulus: i64, n: i64) -> (i64, Option<i64>) {
    assert!(modulus > 1 && 0 <= n && n < modulus);
    if n == 0 {
        return (modulus, None);
    }
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
    (a, Some(x00))
}

pub trait Modulus {
    fn value() -> u32;
}

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub struct Modular<M: Modulus> {
    phantom: std::marker::PhantomData<M>,
    value: u32,
}

impl<M: Modulus> std::fmt::Display for Modular<M> {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "{}", self.value)
    }
}

impl<M: Modulus> Modular<M> {
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
    fn inverse(self) -> Option<Self> {
        let (g, inv) = extgcd_modinv(
            M::value() as i64,
            self.value() as i64,
        );
        if g != 1 || inv.is_none() {
            None
        } else {
            Some(inv.unwrap().into())
        }
    }

    pub fn invert(self) -> Result<Self, String> {
        let v = self.value;
        self.inverse().ok_or_else(|| {
            format!(
                "{} is not invertible for the modulus {}",
                v,
                M::value()
            )
        })
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

/// ```
/// use dsalgo::dynamic_modulus::DynamicMod;
/// struct Foo;
/// type Mod = DynamicMod<Foo>;
/// Mod::set(1_000_000_007);
/// assert_eq!(Mod::value(), 1_000_000_007);
/// ```
#[derive(Debug, Copy, Clone, PartialEq, Eq, PartialOrd, Ord, Hash)]
pub struct DynamicMod<Id>(std::marker::PhantomData<Id>);

impl<Id> DynamicMod<Id> {
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

impl<Id> Modulus for DynamicMod<Id> {
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
    T: std::ops::Mul<Output = T> + From<usize> + Clone,
{
    assert!(size > 0);
    let mut v = (0..size).map(|i| i.into()).collect::<Vec<T>>();
    v[0] = 1.into();
    let op = |a: T, b: T| -> T { a * b };
    accumulate(v, op)
}

pub fn factorial<T>(n: usize) -> T
where
    T: std::ops::Mul<Output = T> + From<usize>,
{
    (1..=n).fold(1.into(), |accum, x| {
        accum * x.into()
    })
}

pub fn inverse_factorial_table<T>(size: usize) -> Vec<T>
where
    T: std::ops::Mul<Output = T> + MulInv<Output = T> + From<usize> + Clone,
{
    let mut v = (0..size).map(|i| (i + 1).into()).collect::<Vec<T>>();
    v[size - 1] = factorial::<T>(size - 1).mul_inv();
    let op = |a: T, b: T| -> T { a * b };
    accumulate(
        v.into_iter().rev().collect(),
        op,
    )
    .into_iter()
    .rev()
    .collect()
}

pub struct Combination<T>
where
    T: std::ops::Mul + MulInv<Output = T> + From<usize> + Clone,
{
    fact: Vec<T>,
    inv_fact: Vec<T>,
}

impl<T> Combination<T>
where
    T: std::ops::Mul<Output = T> + MulInv<Output = T> + From<usize> + Clone,
{
    pub fn new(size: usize) -> Self {
        let fact = factorial_table::<T>(size);
        let inv_fact = inverse_factorial_table::<T>(size);
        Self { fact, inv_fact }
    }

    pub fn calc(&self, n: usize, k: usize) -> Result<T, ()> {
        if n < k {
            Ok(0.into())
        } else if n >= self.fact.len() {
            Err(())
        } else {
            Ok(self.fact[n].clone()
                * self.inv_fact[n - k].clone()
                * self.inv_fact[k].clone())
        }
    }

    pub fn inv(&self, n: usize, k: usize) -> Result<T, ()> {
        if n < k {
            Ok(0.into())
        } else if n >= self.fact.len() {
            Err(())
        } else {
            Ok(self.inv_fact[n].clone()
                * self.fact[k].clone()
                * self.fact[n - k].clone())
        }
    }
}

impl<T> Choose<T> for Combination<T>
where
    T: std::ops::Mul<Output = T> + MulInv<Output = T> + From<usize> + Clone,
{
    fn choose(&mut self, n: usize, k: usize) -> T { self.calc(n, k).unwrap() }
}

pub trait Choose<T> {
    fn choose(&mut self, n: usize, k: usize) -> T;
}

pub struct HomogeneousProduct<T>
where
    T: From<usize>,
{
    chooser: Box<dyn Choose<T>>,
}

impl<T> HomogeneousProduct<T>
where
    T: From<usize>,
{
    pub fn new(chooser: Box<dyn Choose<T>>) -> Self { Self { chooser } }

    pub fn calc(&mut self, n: usize, k: usize) -> T {
        if n == 0 {
            0.into()
        } else {
            self.chooser.choose(n + k - 1, k)
        }
    }
}

pub fn pascal_triangle<T>(size: usize) -> Vec<Vec<T>>
where
    T: std::ops::Add<Output = T> + From<usize> + Clone,
{
    let mut p: Vec<Vec<T>> = vec![vec![0.into(); size]; size];
    for i in 0..size {
        p[i][0] = 1.into();
    }
    for i in 1..size {
        for j in 1..=i {
            p[i][j] = p[i - 1][j - 1].clone() + p[i - 1][j].clone();
        }
    }
    p
}

pub struct PascalRule<T>
where
    T: std::ops::Add<Output = T> + From<usize> + Clone,
{
    cache: std::collections::HashMap<usize, T>,
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

    pub fn calc(&mut self, n: usize, k: usize) -> Result<T, ()> {
        if n < k {
            return Ok(0.into());
        }
        if k == 0 {
            return Ok(1.into());
        }
        if n >= 1 << 32 {
            return Err(());
        }
        let key = n << 32 | k;
        if !self.cache.contains_key(&key) {
            let mut v = self.calc(n - 1, k - 1)?;
            v = v + self.calc(n - 1, k)?;
            self.cache.insert(key, v);
        }
        Ok(*self.cache.get(&key).unwrap())
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

pub fn solve_ghost_leg(
    n: usize,
    edges: Vec<usize>,
) -> Result<Vec<usize>, String> {
    assert!(n > 0);
    let mut res = (0..n).collect::<Vec<_>>();
    for &i in edges.iter().rev() {
        if i >= n - 1 {
            return Err(format!(
                "invalid edge index: {}",
                i
            ));
        }
        res.swap(i, i + 1);
    }
    Ok(res)
}

pub fn bit_length(n: u64) -> u8 {
    (0u64.leading_zeros() - n.leading_zeros()) as u8
}

pub fn msb(n: u64) -> Option<usize> {
    let length = bit_length(n) as usize;
    if length == 0 { None } else { Some(length - 1) }
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
    assert_eq!(default_data.len(), n);
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

    pub fn find_root(&mut self, node: usize) -> usize {
        assert!(node < self.size());
        if self.data[node] < 0 {
            return node;
        }
        self.data[node] = self.find_root(self.data[node] as usize) as isize;
        self.data[node] as usize
    }

    pub fn unite(&mut self, u: usize, v: usize) {
        assert!(u < self.size() && v < self.size());
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
    fn query(&mut self, left: usize, right: usize) -> T;
}

pub struct LCAEulerTourRMQ<Q>
where
    Q: RangeMinimumQuery<(usize, usize)>
        + std::iter::FromIterator<(usize, usize)>,
{
    first_pos: Vec<usize>,
    rmq: Q,
}

impl<Q> LCAEulerTourRMQ<Q>
where
    Q: RangeMinimumQuery<(usize, usize)>
        + std::iter::FromIterator<(usize, usize)>,
{
    pub fn new(tree_edges: &[(usize, usize)], root: usize) -> Self {
        let tour_nodes = euler_tour_nodes(tree_edges, root);
        let depth = tree_depths(tree_edges, root);
        let first_pos = first_positions(&tour_nodes);
        let depth = tour_nodes.iter().map(|&u| depth[u]).collect::<Vec<_>>();
        let rmq = Q::from_iter(depth.into_iter().zip(tour_nodes.into_iter()));
        Self { first_pos, rmq }
    }

    pub fn get(&mut self, u: usize, v: usize) -> usize {
        let mut left = self.first_pos[u];
        let mut right = self.first_pos[v];
        if left > right {
            std::mem::swap(&mut left, &mut right);
        }
        self.rmq.query(left, right + 1).1
    }
}

impl BinaryOperation<(usize, usize), (usize, usize), (usize, usize), Min>
    for (usize, usize)
{
    fn operate(lhs: (usize, usize), rhs: (usize, usize)) -> (usize, usize) {
        std::cmp::min(lhs, rhs)
    }
}

impl AssociativeProperty<(usize, usize), Min> for (usize, usize) {}

impl IdentityElement<(usize, usize), Min> for (usize, usize) {
    fn identity() -> (usize, usize) {
        (
            std::usize::MAX,
            std::usize::MAX,
        )
    }
}

impl CommutativeProperty<(usize, usize), (usize, usize), Min>
    for (usize, usize)
{
}

impl Idempotence<(usize, usize), Min> for (usize, usize) {}

pub fn least_significant_bit(n: u64) -> Option<usize> {
    if n == 0 { None } else { Some(n.trailing_zeros() as usize) }
}

use std::iter::FromIterator;

pub struct SegmentTree<S, Id, M>
where
    M: Monoid<S, Id>,
{
    phantom_id: std::marker::PhantomData<Id>,
    phantom_m: std::marker::PhantomData<M>,
    size: usize,
    data: Vec<S>,
}

impl<S, Id, M> std::iter::FromIterator<S> for SegmentTree<S, Id, M>
where
    S: Clone,
    M: Monoid<S, Id>,
{
    fn from_iter<T: IntoIterator<Item = S>>(iter: T) -> Self {
        let mut data = iter.into_iter().collect::<Vec<_>>();
        let size = data.len();
        let n = size.next_power_of_two();
        data = (0..n)
            .map(|_| M::identity())
            .chain(data.into_iter())
            .chain((0..n - size).map(|_| M::identity()))
            .collect::<Vec<_>>();
        let mut seg = Self {
            phantom_id: std::marker::PhantomData,
            phantom_m: std::marker::PhantomData,
            size,
            data,
        };
        (1..n).rev().for_each(|i| seg.update(i));
        seg
    }
}

impl<S, Id, M> From<&[S]> for SegmentTree<S, Id, M>
where
    Self: std::iter::FromIterator<S>,
    S: Clone,
    M: Monoid<S, Id>,
{
    fn from(slice: &[S]) -> Self { Self::from_iter(slice.iter().cloned()) }
}

impl<S, Id, M> SegmentTree<S, Id, M>
where
    M: Monoid<S, Id>,
{
    pub fn size(&self) -> usize { self.size }

    fn n(&self) -> usize { self.data.len() >> 1 }
}

impl<S, Id, M> SegmentTree<S, Id, M>
where
    S: Clone,
    M: Monoid<S, Id>,
{
    pub fn new<F>(size: usize, default: F) -> Self
    where
        F: Fn() -> S,
    {
        Self::from_iter((0..size).map(|_| default()))
    }

    fn update(&mut self, i: usize) {
        self.data[i] = M::operate(
            self.data[i << 1].clone(),
            self.data[i << 1 | 1].clone(),
        );
    }

    pub fn set(&mut self, mut i: usize, x: S) {
        assert!(i < self.size);
        i += self.n();
        self.data[i] = x;
        while i > 1 {
            i >>= 1;
            self.update(i);
        }
    }

    pub fn fold(&self, mut l: usize, mut r: usize) -> S {
        assert!(l <= r && r <= self.size);
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

impl<S, Id, M> SegmentTree<S, Id, M>
where
    S: Clone,
    M: Monoid<S, Id>,
{
    pub fn max_right<F>(&self, is_ok: &F, l: usize) -> usize
    where
        F: Fn(&S) -> bool,
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
        F: Fn(&S) -> bool,
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

impl<S, Id, M> std::ops::Index<usize> for SegmentTree<S, Id, M>
where
    M: Monoid<S, Id>,
{
    type Output = S;

    fn index(&self, i: usize) -> &Self::Output {
        assert!(i < self.size);
        &self.data[i + self.n()]
    }
}

impl<S, Id, M> SegmentTree<S, Id, M>
where
    S: Clone,
    M: Monoid<S, Id>,
{
    pub fn fold_recurse(&self, l: usize, r: usize) -> S {
        assert!(l <= r && r <= self.size);
        self._fold_recurse(l, r, 0, self.n(), 1)
    }

    fn _fold_recurse(
        &self,
        l: usize,
        r: usize,
        cur_l: usize,
        cur_r: usize,
        i: usize,
    ) -> S {
        if cur_r <= l || r <= cur_l {
            return M::identity();
        }
        if l <= cur_l && cur_r <= r {
            return self.data[i].clone();
        }
        let c = (cur_l + cur_r) >> 1;
        M::operate(
            self._fold_recurse(l, r, cur_l, c, i << 1),
            self._fold_recurse(l, r, c, cur_r, i << 1 | 1),
        )
    }
}

impl<S, Id, M> SegmentTree<S, Id, M>
where
    S: Clone,
    M: Monoid<S, Id>,
{
    pub fn max_right_recurse<F>(&self, is_ok: &F, l: usize) -> usize
    where
        F: Fn(&S) -> bool,
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
        v: &mut S,
        i: usize,
    ) -> usize
    where
        F: Fn(&S) -> bool,
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
        F: Fn(&S) -> bool,
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
        v: &mut S,
        i: usize,
    ) -> usize
    where
        F: Fn(&S) -> bool,
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

impl RangeMinimumQuery<(usize, usize)>
    for SegmentTree<(usize, usize), Min, (usize, usize)>
{
    fn query(&mut self, l: usize, r: usize) -> (usize, usize) {
        self.fold(l, r)
    }
}

#[allow(dead_code)]
type LCAEulerTourRMQSegTree =
    LCAEulerTourRMQ<SegmentTree<(usize, usize), Min, (usize, usize)>>;

pub struct SparseTable<S, Id, G>
where
    G: Semigroup<S, Id> + Idempotence<S, Id> + CommutativeProperty<S, S, Id>,
{
    phantom_id: std::marker::PhantomData<Id>,
    phandom_g: std::marker::PhantomData<G>,
    data: Vec<Vec<S>>,
}

impl<S, Id, G> std::iter::FromIterator<S> for SparseTable<S, Id, G>
where
    G: Semigroup<S, Id> + Idempotence<S, Id> + CommutativeProperty<S, S, Id>,
    S: Clone,
{
    fn from_iter<T: IntoIterator<Item = S>>(iter: T) -> Self {
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
        Self {
            phantom_id: std::marker::PhantomData,
            phandom_g: std::marker::PhantomData,
            data,
        }
    }
}

impl<S, Id, G> SparseTable<S, Id, G>
where
    G: Semigroup<S, Id> + Idempotence<S, Id> + CommutativeProperty<S, S, Id>,
    S: Clone,
{
    pub fn new(slice: &[S]) -> Self { Self::from_iter(slice.iter().cloned()) }

    pub fn fold(&self, l: usize, r: usize) -> S {
        assert!(l < r && r <= self.data[0].len());
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

impl RangeMinimumQuery<(usize, usize)>
    for SparseTable<(usize, usize), Min, (usize, usize)>
{
    fn query(&mut self, l: usize, r: usize) -> (usize, usize) {
        self.fold(l, r)
    }
}

#[allow(dead_code)]
type LCAEulerTourRMQSparseTable =
    LCAEulerTourRMQ<SparseTable<(usize, usize), Min, (usize, usize)>>;

pub struct DisjointSparseTable<S, Id, G>
where
    G: Semigroup<S, Id> + CommutativeProperty<S, S, Id>,
{
    phantom_id: std::marker::PhantomData<Id>,
    phandom_g: std::marker::PhantomData<G>,
    data: Vec<Vec<S>>,
}

impl<S, Id, G> std::iter::FromIterator<S> for DisjointSparseTable<S, Id, G>
where
    G: Semigroup<S, Id> + CommutativeProperty<S, S, Id>,
    S: Clone,
{
    fn from_iter<T: IntoIterator<Item = S>>(iter: T) -> Self {
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
        Self {
            phantom_id: std::marker::PhantomData,
            phandom_g: std::marker::PhantomData,
            data,
        }
    }
}

impl<S, Id, G> DisjointSparseTable<S, Id, G>
where
    G: Semigroup<S, Id> + CommutativeProperty<S, S, Id>,
    S: Clone,
{
    pub fn new(slice: &[S]) -> Self { Self::from_iter(slice.iter().cloned()) }

    /// [l, r)
    pub fn fold(&self, l: usize, mut r: usize) -> S {
        assert!(l < r && r <= self.data[0].len());
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
    for DisjointSparseTable<(usize, usize), Min, (usize, usize)>
{
    fn query(&mut self, l: usize, r: usize) -> (usize, usize) {
        self.fold(l, r)
    }
}

#[allow(dead_code)]
type LCAEulerTourRMQDisjointSparseTable =
    LCAEulerTourRMQ<DisjointSparseTable<(usize, usize), Min, (usize, usize)>>;

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

pub struct SqrtDecomposition<S, Id, G> {
    phantom: std::marker::PhantomData<(Id, G)>,
    pub(crate) data: Vec<S>,
    pub(crate) buckets: Vec<S>,
}

impl<S, Id, G> SqrtDecomposition<S, Id, G> {
    pub fn size(&self) -> usize { self.data.len() }

    pub(crate) fn sqrt(&self) -> usize {
        let n = self.buckets.len();
        (self.size() + n - 1) / n
    }
}

impl<S, Id, G> std::iter::FromIterator<S> for SqrtDecomposition<S, Id, G>
where
    G: Semigroup<S, Id>,
    S: Clone,
{
    fn from_iter<T: IntoIterator<Item = S>>(iter: T) -> Self {
        let data = iter.into_iter().collect::<Vec<_>>();
        let size = data.len();
        let n = floor_sqrt(size as u64) as usize;
        let buckets = (0..(size + n - 1) / n)
            .map(|j| {
                (0..std::cmp::min(n, size - j * n))
                    .map(|k| data[k].clone())
                    .reduce(|l, r| G::operate(l, r))
                    .unwrap()
            })
            .collect();
        Self {
            phantom: std::marker::PhantomData,
            data,
            buckets,
        }
    }
}

impl<S, Id, G> SqrtDecomposition<S, Id, G>
where
    G: Semigroup<S, Id>,
    S: Clone,
{
    pub fn set(&mut self, i: usize, x: S) {
        assert!(i < self.size());
        let n = self.sqrt();
        self.data[i] = x;
        let j = i / n;
        let size = self.size();
        self.buckets[j] = (0..std::cmp::min(n, size - j * n))
            .map(|k| self.data[j * n + k].clone())
            .reduce(|l, r| G::operate(l, r))
            .unwrap();
    }

    pub fn reduce(&self, l: usize, mut r: usize) -> Option<S> {
        r = std::cmp::min(r, self.size());
        // if l >= r {
        //     return None;
        // }
        let n = self.sqrt();
        // let mut v = M::identity();
        (0..self.buckets.len())
            .filter(|&j| l < n * (j + 1) && n * j < r)
            .map(|j| {
                if l <= n * j && n * (j + 1) <= r {
                    return self.buckets[j].clone();
                }
                (0..n)
                    .filter_map(|k| {
                        let i = j * n + k;
                        if l <= i && i < r {
                            Some(self.data[i].clone())
                        } else {
                            None
                        }
                    })
                    .reduce(|l, r| G::operate(l, r))
                    .unwrap()
            })
            .reduce(|l, r| G::operate(l, r))
    }
}

impl<S, Id, M> SqrtDecomposition<S, Id, M>
where
    M: Monoid<S, Id>,
    S: Clone,
{
    /// faster than normal fold by constant time optimization.
    pub fn fast_reduce(&self, l: usize, r: usize) -> S {
        assert!(l <= r && r <= self.size());
        let n = self.sqrt();
        let mut v = M::identity();
        let lj = (l + n - 1) / n;
        let rj = r / n;
        if rj < lj {
            (l..r).for_each(|i| {
                v = M::operate(v.clone(), self.data[i].clone());
            });
            return v;
        }
        (l..lj * n).for_each(|i| {
            v = M::operate(v.clone(), self.data[i].clone());
        });
        (lj..rj).for_each(|j| {
            v = M::operate(
                v.clone(),
                self.buckets[j].clone(),
            );
        });
        (rj * n..r).for_each(|i| {
            v = M::operate(v.clone(), self.data[i].clone());
        });
        v
    }
}

// TODO: set_range (lazy sqrt decomp)

impl RangeMinimumQuery<(usize, usize)>
    for SqrtDecomposition<(usize, usize), Min, (usize, usize)>
{
    fn query(&mut self, l: usize, r: usize) -> (usize, usize) {
        self.reduce(l, r).unwrap()
    }
}

#[allow(dead_code)]
type LCAEulerTourRMQSqrtDecomposition =
    LCAEulerTourRMQ<SqrtDecomposition<(usize, usize), Min, (usize, usize)>>;

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

    // TODO: add Generic Type F to segmen tree for applying.
    // replace set(i, x) -> apply(i, x) and apply function of type F
    // and set(i, x) is gonnabe an extension for segment tree but primitime core
    // API. consider dual segment tree and lazy segment tree similarly.
    // TODO: use semigroup instead of monoid as default.
    // new(size) is not gonna be core API but extensional API for the case only
    // the given semigroup is also monoid.

    // TODO: merge phantom datas as tuple.
}
