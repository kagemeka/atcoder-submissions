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
#[allow(unused_macros)]
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

    let n: u64 = reader.read()?;
    writeln!(
        writer,
        "{}",
        sum_of_multiples_sum(n)
    )?;
    // writeln!(
    //     writer,
    //     "{}",
    //     sum_of_multiples_sum_range(n, 1, n)
    // )?;
    writer.flush()?;
    Ok(())
}

pub fn arithematic_series(diff: i64, a_0: i64, nth: u64) -> i64 {
    sum_arithematic_progression(
        a_0,
        a_0 + diff * nth as i64,
        nth + 1,
    )
}

pub fn sum_arithematic_progression(a: i64, b: i64, count: u64) -> i64 {
    assert!(count > 0);
    if count == 1 {
        assert!(a == b);
    } else {
        assert!((b - a) % (count as i64 - 1) == 0);
    }
    (a + b) * count as i64 / 2
}

pub fn sum_of_multiples(limit: u64, n: u64) -> u64 {
    let cnt = limit / n;
    (1 + cnt) * cnt / 2 * n
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

/// \sum_{i=lo}^{hi}{\sum_{i|j, j <= limit}{j}}
/// O(\sqrt{n})
/// sqrt split teqnique
pub fn sum_of_multiples_sum_range(limit: u64, lo: u64, hi: u64) -> u64 {
    assert!(lo <= hi && hi <= limit);
    let mut s = 0;
    let mut k: u64 = 0; // floor_sqrt(limit) + 1
    for i in lo..=hi {
        if i * i > limit {
            k = i;
            break;
        }
        s += sum_of_multiples(limit, i);
    }
    if k == 0 {
        debug_assert!(hi * hi <= limit);
        return s;
    }
    debug_assert!(lo <= k && k <= hi);
    // added for i=lo..k.
    // next, consider i=k..=hi.
    // for j=1..?, for i i * j <= limit, sum(i * j) = j * sum(i)
    // because i >= k, it's enough to consider j as at most limit / k.
    for j in 1..=limit / k {
        let mut i_max = limit / j;
        debug_assert!((i_max + 1) * j > limit);
        debug_assert!(k <= i_max);
        if i_max > hi {
            i_max = hi;
        }
        s += (k + i_max) * (i_max - k + 1) / 2 * j;
    }

    s
}

/// \sum_{i=1}^{limit}{\sum_{i|j, j <= limit}{j}}
/// smart formula transformation with symmetric property.
/// O(\sqrt{n})
pub fn sum_of_multiples_sum(limit: u64) -> u64 {
    let mut s = 0;
    for i in 1..=limit {
        if i * i > limit {
            break;
        }
        let j = limit / i;
        s += i * i + i * (i + 1 + j) * (j - i);
    }
    s
}

/// \sum_{i=1}^n{i \cdot |divisors(i)|}
/// O(\sqrt{n})
pub fn sum_of_divisors_count_times_i(limit: u64) -> u64 {
    sum_of_multiples_sum(limit)
}

// /// \sum_{i=1}^n{i \cdot |divisors(i)|}
// /// O(\sqrt{n})
// pub fn sum_of_divisors_counts_multipled_by_i_1_to_n_sqrt_split(n: u64) -> u64
// {     let mut k: u64 = 0;

//     let mut s = 0;
//     for i in 1..=n {
//         if i * i > n {
//             k = i;
//             break;
//         }
//         s += sum_of_multiple(i, n);
//     }
//     for j in 1..k {
//         let i = n / j; // max limit such that i * j <= n
//         if i < k {
//             break;
//         }
//         s += (k + i) * (i - k + 1) / 2 * j;
//     }
//     s
// }

pub fn geometric_series(a0: i64, r: i64, n: usize) -> i64 {
    if r == 0 {
        return a0 * n as i64;
    }
    (1 - pow_semigroup(&|x, y| x * y, r, n as u64)) / (1 - r)
}

pub fn pow_semigroup<F, X>(f: &F, mut x: X, mut exponent: u64) -> X
where
    F: Fn(X, X) -> X,
    X: Clone,
{
    assert!(exponent > 0);
    let mut y = x.clone();
    exponent -= 1;
    while exponent > 0 {
        if exponent & 1 == 1 {
            y = f(y, x.clone());
        }
        x = f(x.clone(), x);
        exponent >>= 1;
    }
    y
}

pub fn prime_factorize_trial_division(mut n: u64) -> Vec<(u64, usize)> {
    let mut factors = vec![];
    for i in 2..n {
        if i * i > n {
            break;
        }
        if n % i != 0 {
            continue;
        }
        let mut cnt = 0;
        while n % i == 0 {
            cnt += 1;
            n /= i;
        }
        factors.push((i, cnt));
    }
    if n != 1 {
        factors.push((n, 1));
    }
    factors
}
