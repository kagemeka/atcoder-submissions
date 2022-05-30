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
macro_rules! dbg {
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

// #[allow(warnings)]
fn main() -> Result<(), Box<dyn std::error::Error>> {
    use std::io::Write;
    let mut reader = locked_stdin_reader();
    let mut writer = locked_stdout_buf_writer();

    let s: String = reader.read()?;
    let t: String = reader.read()?;
    let s = s.chars().collect::<Vec<char>>();
    let t = t.chars().collect::<Vec<char>>();

    let lcs = struct_lcs(&s, &t);
    writeln!(
        writer,
        "{}",
        lcs.iter().collect::<String>()
    )?;

    writer.flush()?;
    Ok(())
}

pub(crate) fn lcs_dp_table<T: PartialEq>(a: &[T], b: &[T]) -> Vec<Vec<usize>> {
    let n = a.len();
    let m = b.len();
    let mut length = vec![vec![0; m + 1]; n + 1];
    for i in 0..n {
        for j in 0..m {
            if a[i] == b[j] {
                length[i + 1][j + 1] = length[i][j] + 1;
                continue;
            }
            length[i + 1][j + 1] = std::cmp::max(
                length[i][j + 1],
                length[i + 1][j],
            );
        }
    }
    length
}

pub fn lcs_length(a: &[u8], b: &[u8]) -> usize {
    lcs_dp_table(a, b)[a.len()][b.len()]
}

pub(crate) fn lcs_length_low_memory<T: PartialEq>(a: &[T], b: &[T]) -> usize {
    let m = b.len();
    let mut length = vec![0; m + 1];
    for x in a {
        for j in (0..m).rev() {
            if x == &b[j] {
                length[j + 1] = length[j] + 1;
            }
        }
        for j in 0..m {
            length[j + 1] = std::cmp::max(length[j], length[j + 1]);
        }
    }
    length[m]
}

/// restore one of the transtion histories.
pub(crate) fn restore_lcs_indices(
    lcs_dp_table: &[Vec<usize>],
) -> Vec<(usize, usize)> {
    let mut indices = vec![];
    let length = lcs_dp_table;
    let mut i = length.len() - 1;
    let mut j = length[0].len() - 1;
    while i > 0 && j > 0 {
        let l = length[i][j];
        if length[i][j - 1] == l {
            j -= 1;
            continue;
        }
        if length[i - 1][j] == l {
            i -= 1;
            continue;
        }
        i -= 1;
        j -= 1;
        indices.push((i, j));
    }
    indices.reverse();
    indices
}

pub fn struct_lcs<T: PartialEq + Clone>(a: &[T], b: &[T]) -> Vec<T> {
    restore_lcs_indices(&lcs_dp_table(a, b))
        .into_iter()
        .map(|(i, _)| a[i].clone())
        .collect()
}

// TODO:
pub fn divisors_from_prime_factors(
    prime_factors: Vec<(u64, usize)>,
) -> Vec<u64> {
    vec![]
}

pub fn structive_find_divisors<F>(prime_factorize: &F, n: u64) -> Vec<u64>
where
    F: Fn(u64) -> Vec<(u64, usize)>,
{
    divisors_from_prime_factors(prime_factorize(n))
}

pub fn find_divisors_for_same_remainders(mut a: u64, mut b: u64) -> Vec<u64> {
    if a > b {
        std::mem::swap(&mut a, &mut b);
    }
    find_divisors(b - a)
}

/// 0 <= r < n
/// find all x such that n = qx + r
pub fn find_divisors_for_const_remainder(n: u64, r: u64) -> Vec<u64> {
    find_divisors(n - r).into_iter().filter(|&d| d > r).collect()
}

pub fn max_divisor_at_most_sqrt(n: u64) -> u64 {
    assert!(n > 0);
    let divs = find_divisors(n);
    divs[divs.len() >> 1]
}

/// find medians of divisors.
pub fn min_pair_sum_const_prod(prod: u64) -> u64 {
    if prod == 0 {
        return 0;
    }
    let d = max_divisor_at_most_sqrt(prod);
    d + prod / d
}

pub fn is_perfect_number(n: u64) -> bool {
    find_divisors(n).iter().sum::<u64>() == n << 1
}

pub fn count_divisors_naive(n: u64) -> u32 { find_divisors(n).len() as u32 }

pub struct SieveOfEratosthenesLowMemoryPrimeGenerator {
    iter: std::vec::IntoIter<u64>,
    range_sieve: RangeSieveOfEratosthenes,
    ranges: std::vec::IntoIter<(u64, u64)>,
}

impl SieveOfEratosthenesLowMemoryPrimeGenerator {
    /// [lo, hi)
    pub fn new(mut lo: u64, mut hi: u64) -> Self {
        if lo < 2 {
            lo = 2;
        }
        if hi < 2 {
            hi = 2;
        }
        let mut ranges = vec![];
        let range_size = floor_sqrt(hi) as usize;
        for i in (lo..hi).step_by(range_size) {
            ranges.push((
                i,
                std::cmp::min(hi, i + range_size as u64),
            ));
        }

        Self {
            iter: vec![].into_iter(),
            range_sieve: RangeSieveOfEratosthenes::new(hi as u64),
            ranges: ranges.into_iter(),
        }
    }
}

impl Iterator for SieveOfEratosthenesLowMemoryPrimeGenerator {
    type Item = u64;

    fn next(&mut self) -> Option<Self::Item> {
        if let Some(p) = self.iter.next() {
            return Some(p);
        }
        while let Some((lo, hi)) = self.ranges.next() {
            self.iter = self.range_sieve.find_prime_numbers(lo, hi).into_iter();
            if let Some(p) = self.iter.next() {
                return Some(p);
            }
        }
        None
    }
}

pub fn prime_generator(
    lo: u64,
    hi: u64,
) -> SieveOfEratosthenesLowMemoryPrimeGenerator {
    SieveOfEratosthenesLowMemoryPrimeGenerator::new(lo, hi)
}

pub struct RangeSieveOfEratosthenes {
    primes: Vec<u64>,
    less_than: u64,
}

impl RangeSieveOfEratosthenes {
    pub fn new(less_than: u64) -> Self {
        Self {
            primes: find_prime_numbers(floor_sqrt(less_than) + 1),
            less_than,
        }
    }

    /// find prime numbers in [lo, hi).
    /// time: O((hi - lo)\log{\log{less_than}})
    /// space: O(hi - lo)
    pub fn find_prime_numbers(&self, mut lo: u64, hi: u64) -> Vec<u64> {
        assert!(lo <= hi && hi <= self.less_than);
        if hi <= 2 {
            return vec![];
        }
        if lo < 2 {
            lo = 2;
        }

        let lo = lo as usize;
        let hi = hi as usize;
        let size = hi - lo;
        let mut is_prime = vec![true; size];
        for i in (lo & 1..size).step_by(2) {
            is_prime[i] = false;
        }
        if lo == 2 {
            is_prime[0] = true;
        }
        for &p in self.primes.iter().skip(1) {
            let i = p as usize;
            if i * i >= hi {
                break;
            }
            let mut from = (lo + i - 1) / i * i;
            if from & 1 == 0 {
                from += i;
            }
            for j in (std::cmp::max(from, i * i)..hi).step_by(i << 1) {
                is_prime[j - lo] = false;
            }
        }
        is_prime
            .into_iter()
            .enumerate()
            .filter_map(
                |(i, is_prime)| {
                    if is_prime { Some((i + lo) as u64) } else { None }
                },
            )
            .collect()
    }
}

pub fn floor_sqrt(n: u64) -> u64 {
    let mut lo = 0;
    let mut hi = 1 << 32;
    while hi - lo > 1 {
        let x = (lo + hi) >> 1;
        if n / x >= x {
            lo = x;
        } else {
            hi = x;
        }
    }
    lo
}

/// table[i] := largest prime number less or equal to i.
pub fn previous_prime_table(size: usize) -> Vec<Option<u64>> {
    let mut prev = is_prime_table(size)
        .into_iter()
        .enumerate()
        .map(
            |(i, is_prime)| {
                if is_prime { Some(i as u64) } else { None }
            },
        )
        .collect::<Vec<_>>();
    for i in 4..size {
        if prev[i].is_none() {
            prev[i] = prev[i - 1];
        }
    }
    prev
}

pub fn next_prime_table(size: usize) -> Vec<u64> {
    const MAX_PRIME_GAP_64: u64 = 1550;
    let mut next = is_prime_table(size + MAX_PRIME_GAP_64 as usize)
        .into_iter()
        .enumerate()
        .map(
            |(i, is_prime)| {
                if is_prime { Some(i as u64) } else { None }
            },
        )
        .collect::<Vec<_>>();
    for i in (1..size + 1550).rev() {
        if next[i - 1].is_none() {
            next[i - 1] = next[i];
        }
    }
    next.into_iter().take(size).map(|x| x.unwrap()).collect()
}

// TODO: accelerate wtih miller rabin.
/// for small n, use prime numbers list and precompute prev/next prime.
pub fn previous_prime(mut n: u64) -> u64 {
    assert!(n > 2);
    loop {
        n -= 1;
        if is_prime_naive(n) {
            break;
        }
    }
    n
}

// TODO: accelerate wtih miller rabin.
pub fn next_prime(mut n: u64) -> u64 {
    loop {
        n += 1;
        if is_prime_naive(n) {
            break;
        }
    }
    n
}

pub fn find_divisors(n: u64) -> Vec<u64> {
    let mut divisors = Vec::new();
    for d in 1..=n {
        if d * d > n {
            break;
        }
        if n % d != 0 {
            continue;
        }
        divisors.push(d);
        if d * d != n {
            divisors.push(n / d);
        }
    }
    divisors.sort();
    divisors
}

pub fn is_prime_naive(n: u64) -> bool { find_divisors(n).len() == 2 }

pub fn sieve_of_eratosthenes(sieve_size: usize) -> Vec<u64> {
    let mut primes = Vec::with_capacity(sieve_size);
    if sieve_size > 2 {
        primes.push(2);
    }
    let mut is_prime = vec![true; sieve_size];
    for i in (3..sieve_size).step_by(2) {
        if !is_prime[i] {
            continue;
        }
        primes.push(i as u64);
        for j in (i * i..sieve_size).step_by(i << 1) {
            is_prime[j] = false;
        }
    }
    primes
}

/// compute least prime factor table and prime numbers list.
pub fn linear_prime_sieve(size: usize) -> (Vec<Option<u64>>, Vec<u64>) {
    let mut lpf = vec![None; size];
    let mut prime_numbers = Vec::with_capacity(size);
    for i in 2..size {
        if lpf[i].is_none() {
            lpf[i] = Some(i as u64);
            prime_numbers.push(i as u64);
        }
        for &p in &prime_numbers {
            if p > lpf[i].unwrap() || p as usize * i >= size {
                break;
            }
            debug_assert!(lpf[p as usize * i].is_none());
            lpf[p as usize * i] = Some(p);
        }
    }
    (lpf, prime_numbers)
}

pub fn is_prime_table(size: usize) -> Vec<bool> {
    let mut is_prime = vec![false; size];
    for p in find_prime_numbers(size as u64) {
        is_prime[p as usize] = true;
    }
    is_prime
}

pub fn least_prime_factor_table(size: usize) -> Vec<Option<u64>> {
    let mut lpf = vec![None; size];
    for p in find_prime_numbers(size as u64) {
        debug_assert!(lpf[p as usize].is_none());
        lpf[p as usize] = Some(p);
    }
    for i in (4..size).step_by(2) {
        lpf[i] = Some(2);
    }
    for i in (3..size).step_by(2) {
        if i * i >= size {
            break;
        }
        debug_assert!(lpf[i].is_some());
        if lpf[i] != Some(i as u64) {
            continue;
        }
        for j in (i * i..size).step_by(i * 2) {
            if let Some(x) = lpf[j] {
                debug_assert!(x < i as u64);
            } else {
                lpf[j] = Some(i as u64);
            }
        }
    }
    lpf
}

pub fn greatest_prime_factor_table(size: usize) -> Vec<Option<u64>> {
    let lpf = least_prime_factor_table(size);
    let mut gpf = vec![None; size];
    for i in 2..size {
        gpf[i] = if lpf[i] == Some(i as u64) {
            lpf[i]
        } else {
            gpf[i / lpf[i].unwrap() as usize]
        }
    }
    gpf
}

pub fn find_prime_numbers(less_than: u64) -> Vec<u64> {
    sieve_of_eratosthenes(less_than as usize)
}

pub fn binary_search<T, F>(is_ok: &F, monotonic_sequence: &[T]) -> usize
where
    F: Fn(&T) -> bool,
{
    let mut ng = -1;
    let mut ok = monotonic_sequence.len() as isize;
    while ok - ng > 1 {
        let i = (ng + ok) >> 1;
        if is_ok(&monotonic_sequence[i as usize]) {
            ok = i;
        } else {
            ng = i;
        }
    }
    ok as usize
}

pub fn upper_bound<T: PartialOrd>(monotonic_sequence: &[T], x: &T) -> usize {
    binary_search(
        &|y: &T| y > x,
        monotonic_sequence,
    )
}
