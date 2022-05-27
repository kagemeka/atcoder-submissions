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

    let n: u64 = reader.read()?;

    // subject to
    // values := 1, 6, 6^2, ..., 9, 9^2, ...
    // \forall{i} w_i := 1
    // \sum{v_j} >= n

    // minimize
    // \sum{w_j}

    // -> duality of unbounded knapsack problem.

    let mut values = vec![1];
    let mut p = 6;
    while p <= n {
        values.push(p);
        p *= 6;
    }
    p = 9;
    while p <= n {
        values.push(p);
        p *= 9;
    }
    let m = values.len();
    let vw = values.into_iter().zip(vec![1; m]).collect::<Vec<_>>();
    let n = n as usize;
    let res = dual_unbounded_knapsack_table_just(&vw, n + 1)[n].unwrap();
    writeln!(writer, "{}", res)?;

    writer.flush()?;
    Ok(())
}

/// dp[i] := min sum of weights such that their values sum is `just` i.
pub(crate) fn dual_unbounded_knapsack_table_just(
    value_weight_pairs: &[(u64, u64)],
    size: usize,
) -> Vec<Option<u64>> {
    let mut min_weight = vec![None; size];
    min_weight[0] = Some(0);
    for &(v, w) in value_weight_pairs {
        let v = v as usize;
        for i in v..size {
            if min_weight[i - v].is_none() {
                continue;
            }
            let nw = Some(min_weight[i - v].unwrap() + w);
            if min_weight[i].is_none() || nw < min_weight[i] {
                min_weight[i] = nw;
            }
        }
    }
    min_weight
}

/// dp[i] := max sum of values such that their weights sum is `at most` i.
pub(crate) fn unbounded_knapsack_table(
    value_weight_pairs: &[(u64, u64)],
    size: usize,
) -> Vec<u64> {
    let mut max_value = vec![0; size];
    for &(v, w) in value_weight_pairs {
        let w = w as usize;
        for i in w..size {
            max_value[i] = std::cmp::max(
                max_value[i],
                max_value[i - w] + v,
            );
        }
    }
    max_value
}

/// max sum of values such that their weights sum is `at most` capacity.
pub fn unbounded_knapsack(
    value_weight_pairs: &[(u64, u64)],
    capacity: u64,
) -> u64 {
    let c = capacity as usize;
    unbounded_knapsack_table(value_weight_pairs, c + 1)[c]
}
