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

    let n: usize = reader.read()?;
    let cap: usize = reader.read()?;

    let vw = (0..n)
        .map(|_| {
            let v: u64 = reader.read().unwrap();
            let w: u64 = reader.read().unwrap();
            (v, w)
        })
        .collect::<Vec<_>>();

    let n = n as u64;
    let cap = cap as u64;
    let res = if n <= 40 {
        knapsack_01_meet_in_the_middle(&vw, cap)
    } else if vw.iter().map(|&(_, w)| w).sum::<u64>() <= n * 1000 {
        knapsack_01_small_weights_sum(&vw, cap)
    } else {
        knapsack_01_small_values_sum(&vw, cap)
    };
    writeln!(writer, "{}", res)?;

    writer.flush()?;
    Ok(())
}

/// generalized bisection method in analysis.
pub fn bisect<T, B, F>(
    calc_middle: &B,
    is_ok: &F,
    trivial_ng: T,
    trivial_ok: T,
    max_epohcs: usize,
) -> T
where
    B: Fn(T, T) -> T,
    F: Fn(&T) -> bool,
    T: Clone + PartialEq,
{
    let mut ng = trivial_ng;
    let mut ok = trivial_ok;
    for _ in 0..max_epohcs {
        let middle = calc_middle(ng.clone(), ok.clone());
        if middle == ng || middle == ok {
            break;
        }
        if is_ok(&middle) {
            ok = middle;
        } else {
            ng = middle;
        }
    }
    ok
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

pub fn binary_search_another<T, F>(is_ok: &F, monotonic_sequence: &[T]) -> usize
where
    F: Fn(&T) -> bool,
{
    let mut lo_ok = 0;
    let mut hi_ok = monotonic_sequence.len();
    while lo_ok < hi_ok {
        let i = (lo_ok + hi_ok - 1) >> 1;
        if is_ok(&monotonic_sequence[i]) {
            hi_ok = i;
        } else {
            lo_ok = i + 1;
        }
    }
    hi_ok
}

pub fn lower_bound<T: PartialOrd>(monotonic_sequence: &[T], x: &T) -> usize {
    binary_search(
        &|y: &T| y >= x,
        monotonic_sequence,
    )
}

pub fn upper_bound<T: PartialOrd>(monotonic_sequence: &[T], x: &T) -> usize {
    binary_search(
        &|y: &T| y > x,
        monotonic_sequence,
    )
}

pub fn knapsack_01_meet_in_the_middle(
    value_weight_pairs: &[(u64, u64)],
    capacity: u64,
) -> u64 {
    fn enumerate_bits_brute_force(items: &[(u64, u64)]) -> Vec<(u64, u64)> {
        let n = items.len();
        let mut cand = vec![];
        for s in 0..1 << n {
            let mut value = 0;
            let mut weight = 0;
            for i in 0..n {
                if s >> i & 1 == 0 {
                    continue;
                }
                let (v, w) = items[i];
                value += v;
                weight += w;
            }
            cand.push((value, weight));
        }
        cand.sort_by_key(|&(_, w)| w);
        for i in 0..(1 << n) - 1 {
            cand[i + 1].0 = std::cmp::max(cand[i].0, cand[i + 1].0);
        }
        cand
    }
    let n = value_weight_pairs.len();
    let a = enumerate_bits_brute_force(&value_weight_pairs[..n / 2]);
    let b = enumerate_bits_brute_force(&value_weight_pairs[n / 2..]);
    let b_weights = b.iter().map(|&(_, w)| w).collect::<Vec<_>>();
    let mut max_value = 0;
    for &(v, w) in a.iter() {
        if w > capacity {
            break;
        }
        let i = upper_bound(&b_weights, &(capacity - w));
        debug_assert!(i > 0);
        max_value = std::cmp::max(max_value, v + b[i - 1].0);
    }
    max_value
}

/// dp[i] := max sum of values such that their weights sum is `just` i.
pub(crate) fn knapsack_01_table_just(
    value_weight_pairs: &[(u64, u64)],
    size: usize,
) -> Vec<Option<u64>> {
    let mut max_value = vec![None; size];
    max_value[0] = Some(0);
    for &(v, w) in value_weight_pairs {
        let w = w as usize;
        for i in (w..size).rev() {
            if max_value[i - w].is_none() {
                continue;
            }
            let nv = Some(max_value[i - w].unwrap() + v);
            if max_value[i].is_none() || nv > max_value[i] {
                max_value[i] = nv;
            }
        }
    }
    max_value
}

/// dp[i] := max sum of values such that their weights sum is `at most` i.
pub(crate) fn knapsack_01_table(
    value_weight_pairs: &[(u64, u64)],
    size: usize,
) -> Vec<u64> {
    let mut max_value = vec![0; size];
    for &(v, w) in value_weight_pairs {
        let w = w as usize;
        for i in (w..size).rev() {
            max_value[i] = std::cmp::max(
                max_value[i],
                max_value[i - w] + v,
            );
        }
    }
    max_value
}

/// max sum of values such that their weights sum is `at most` capacity.
pub fn knapsack_01(value_weight_pairs: &[(u64, u64)], capacity: u64) -> u64 {
    if value_weight_pairs.iter().map(|&(_, w)| w).sum::<u64>() <= capacity {
        value_weight_pairs.iter().map(|&(v, _)| v).sum()
    } else {
        let c = capacity as usize;
        // knapsack_01_table_just(
        //     value_weight_pairs,
        //     c + 1,
        // )
        // .iter()
        // .filter_map(|&x| x)
        // .max()
        // .unwrap()
        knapsack_01_table(value_weight_pairs, c + 1)[c]
    }
}

/// max sum of values such that their weights sum is `at most` capacity.
pub fn knapsack_01_small_weights_sum(
    value_weight_pairs: &[(u64, u64)],
    capacity: u64,
) -> u64 {
    knapsack_01(value_weight_pairs, capacity)
}

/// dp[i] := min sum of weights such that their values sum is `just` i.
pub(crate) fn dual_knapsack_01_table_just(
    value_weight_pairs: &[(u64, u64)],
    size: usize,
) -> Vec<Option<u64>> {
    let mut min_weight = vec![None; size];
    min_weight[0] = Some(0);
    for &(v, w) in value_weight_pairs {
        let v = v as usize;
        for i in (v..size).rev() {
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

/// dp[i] := min sum of weights such that their values sum is `at least` i.
pub(crate) fn dual_knapsack_01_table(
    value_weight_pairs: &[(u64, u64)],
    size: usize,
) -> Vec<Option<u64>> {
    let mut min_weight = vec![None; size];
    min_weight[0] = Some(0);
    for &(v, w) in value_weight_pairs {
        let v = v as usize;
        // for i in (v..size).rev() {
        //     if min_weight[i - v].is_none() {
        //         continue;
        //     }
        //     let nw = Some(min_weight[i - v].unwrap() + w);
        //     if min_weight[i].is_none() || nw < min_weight[i] {
        //         min_weight[i] = nw;
        //     }
        // }
        // for i in (1..size).rev() {
        //     if min_weight[i].is_none() {
        //         continue;
        //     }
        //     if min_weight[i - 1].is_none() || min_weight[i] < min_weight[i -
        // 1]     {
        //         min_weight[i - 1] = min_weight[i];
        //     }
        // }
        for i in (0..size).rev() {
            if min_weight[i].is_none() {
                continue;
            }
            let nw = Some(min_weight[i].unwrap() + w);
            let j = std::cmp::min(i + v, size - 1);
            if min_weight[j].is_none() || nw < min_weight[j] {
                min_weight[j] = nw;
            }
        }
    }
    for i in (1..size).rev() {
        if min_weight[i].is_none() {
            continue;
        }
        if min_weight[i - 1].is_none() || min_weight[i] < min_weight[i - 1] {
            min_weight[i - 1] = min_weight[i];
        }
    }

    min_weight
}

pub fn dual_knapsack_01(
    value_weight_pairs: &[(u64, u64)],
    target_value: u64,
) -> Result<u64, &'static str> {
    let s = value_weight_pairs.iter().map(|&(v, _)| v).sum::<u64>();
    let s = s as usize;
    let t = target_value as usize;
    if s < t {
        return Err("sum of values cannot achieve target value");
    }
    Ok(dual_knapsack_01_table(value_weight_pairs, t + 1)[t].unwrap())
}

/// max sum of values such that their weights sum is `at most` capacity.
pub fn knapsack_01_small_values_sum(
    value_weight_pairs: &[(u64, u64)],
    capacity: u64,
) -> u64 {
    dual_knapsack_01_table_just(
        value_weight_pairs,
        value_weight_pairs.iter().map(|&(v, _)| v).sum::<u64>() as usize + 1,
    )
    .into_iter()
    .enumerate()
    .filter_map(|(v, min_w)| {
        if let Some(w) = min_w {
            if w <= capacity { Some(v as u64) } else { None }
        } else {
            None
        }
    })
    .max()
    .unwrap()
}

// // pub fn unbounded_knapsack_01()
// // pub(crate) unbounded_knapsack_01_table()
