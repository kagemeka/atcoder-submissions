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
    let res = if n <= 30 {
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

pub fn binary_search_sequence<T, F>(
    is_ok: &F,
    monotonic_sequence: &[T],
) -> usize
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

pub fn binary_search_sequence_another<T, F>(
    is_ok: &F,
    monotonic_sequence: &[T],
) -> usize
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

pub fn lower_bound_sequence<T: PartialOrd>(
    monotonic_sequence: &[T],
    x: &T,
) -> usize {
    binary_search_sequence(
        &|y: &T| y >= x,
        monotonic_sequence,
    )
}

pub fn upper_bound_sequence<T: PartialOrd>(
    monotonic_sequence: &[T],
    x: &T,
) -> usize {
    binary_search_sequence(
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
        let i = upper_bound_sequence(&b_weights, &(capacity - w));
        debug_assert!(i > 0);
        max_value = std::cmp::max(max_value, v + b[i - 1].0);
    }
    max_value
}

pub fn knapsack_01_small_weights_sum(
    value_weight_pairs: &[(u64, u64)],
    capacity: u64,
) -> u64 {
    knapsack_01(
        value_weight_pairs,
        std::cmp::min(
            value_weight_pairs.iter().map(|&(_, w)| w).sum::<u64>(),
            capacity,
        ),
    )
}

pub fn knapsack_01(value_weight_pairs: &[(u64, u64)], capacity: u64) -> u64 {
    let c = capacity as usize;
    let mut max_value = vec![0; c + 1];
    for &(v, w) in value_weight_pairs {
        let w = w as usize;
        for i in (w..=c).rev() {
            max_value[i] = std::cmp::max(
                max_value[i],
                max_value[i - w] + v,
            );
        }
    }
    max_value[c]
}

pub fn knapsack_01_small_values_sum(
    value_weight_pairs: &[(u64, u64)],
    capacity: u64,
) -> u64 {
    // let c = capacity as usize;
    let s = value_weight_pairs.iter().map(|&(v, _)| v).sum::<u64>() as usize;
    let mut min_weight = vec![None; s + 1];
    min_weight[0] = Some(0);
    for &(v, w) in value_weight_pairs {
        let v = v as usize;
        for i in (v..=s).rev() {
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
        .into_iter()
        .enumerate()
        .filter_map(|(i, w)| {
            if let Some(w) = w {
                if w <= capacity { Some(i as u64) } else { None }
            } else {
                None
            }
        })
        .max()
        .unwrap()
}
