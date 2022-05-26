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

pub fn locked_stdin_buf_writer()
-> std::io::BufWriter<std::io::StdoutLock<'static>> {
    let stdout = Box::leak(Box::new(std::io::stdout()));
    std::io::BufWriter::new(stdout.lock())
}

// #[allow(warnings)]
fn main() -> Result<(), Box<dyn std::error::Error>> {
    use std::io::Write;
    let mut reader = locked_stdin_reader();
    let mut writer = locked_stdin_buf_writer();

    let w: usize = reader.read()?;
    let n: usize = reader.read()?;
    let k: usize = reader.read()?;

    let wv = (0..n)
        .map(|_| {
            let w: u64 = reader.read().unwrap();
            let v: u64 = reader.read().unwrap();
            (v, w)
        })
        .collect::<Vec<_>>();
    let res = knapsack_01_at_most_k(&wv, k as u64, w as u64);
    writeln!(writer, "{}", res)?;

    writer.flush()?;
    Ok(())
}

/// return max sum of values of at most k items
/// whose sum of weights is at most w.
pub fn knapsack_01_at_most_k(
    value_weight_pairs: &[(u64, u64)],
    k: u64,
    capacity: u64,
) -> u64 {
    let n = value_weight_pairs.len();
    let k = k as usize;
    let c = capacity as usize;
    assert!(k <= n);
    let mut max_value = vec![vec![0; c + 1]; k + 1];
    for &(v, w) in value_weight_pairs {
        let w = w as usize;
        for i in (0..k).rev() {
            for j in w..=c {
                max_value[i + 1][j] = std::cmp::max(
                    max_value[i + 1][j],
                    max_value[i][j - w] + v,
                );
            }
        }
    }
    max_value[k][c]
}
