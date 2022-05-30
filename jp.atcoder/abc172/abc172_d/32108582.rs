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
        // sum_of_divisors_counts_multipled_by_i_1_to_n(n)
        sum_of_divisors_counts_multipled_by_i_1_to_n_sqrt_split(n)
    )?;
    writer.flush()?;
    Ok(())
}

/// \sum_{i=1}^n{i \cdot |divisors(i)|}
/// O(\sqrt{n})
pub fn sum_of_divisors_counts_multipled_by_i_1_to_n_sqrt_split(n: u64) -> u64 {
    let mut k: u64 = 0;

    let mut s = 0;
    for i in 1..=n {
        if i * i > n {
            k = i;
            break;
        }
        let j = n / i;
        s += (1 + j) * j / 2 * i;
    }
    for j in 1..k {
        let i = n / j;
        if i < k {
            break;
        }
        s += (k + i) * (i - k + 1) / 2 * j;
    }
    s
}

/// \sum_{i=1}^n{i \cdot |divisors(i)|}
/// O(\sqrt{n})
pub fn sum_of_divisors_counts_multipled_by_i_1_to_n(n: u64) -> u64 {
    let mut s = 0;
    for i in 1..=n {
        if i * i > n {
            break;
        }
        let j = n / i;
        s += i * i + i * (i + 1 + j) * (j - i);
    }
    s
}
