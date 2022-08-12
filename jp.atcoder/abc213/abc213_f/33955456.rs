pub fn read<T: std::str::FromStr>() -> T {
    use std::io::Read;
    std::io::stdin()
        .lock()
        .by_ref()
        .bytes()
        .map(|c| c.unwrap() as char)
        .skip_while(|c| c.is_whitespace())
        .take_while(|c| !c.is_whitespace())
        .collect::<String>()
        .parse::<T>()
        .ok()
        .unwrap()
}
pub fn lcp_array(a: &[usize], sa: &[usize]) -> Vec<usize> {
    let n = a.len();
    assert!(n > 0 && sa.len() == n);
    let mut rank = vec![0; n];
    for (r, &i) in sa.iter().enumerate() {
        rank[i] = r;
    }
    let mut lcp = vec![0; n - 1];
    let mut h = 0;
    for i in 0..n {
        if h != 0 {
            h -= 1;
        }
        let r = rank[i];
        if r == n - 1 {
            continue;
        }
        let j = sa[r + 1];
        while i.max(j) + h < n && a[i + h] == a[j + h] {
            h += 1;
        }
        lcp[r] = h;
    }
    lcp
}
pub fn unique<T: Ord>(mut a: Vec<T>) -> Vec<T> {
    a.sort();
    a.dedup();
    a
}
pub struct ArrayCompression<T>(pub Vec<T>);
impl<T: Ord + Clone> ArrayCompression<T> {
    pub fn new(a: Vec<T>) -> Self { Self(unique(a)) }

    pub fn encode(&self, v: &T) -> usize { self.0.binary_search(v).unwrap() }

    pub fn inv(&self, i: usize) -> T { self.0[i].clone() }

    pub fn once(a: &[T]) -> Vec<usize> {
        let f = Self::new(a.to_vec());
        a.iter().map(|x| f.encode(x)).collect()
    }
}
pub fn suffix_array(a: &[usize]) -> Vec<usize> {
    let n = a.len();
    let mut arg = vec![0; n + 2];
    let mut counting_argsort = |a: &Vec<usize>| -> Vec<usize> {
        for &x in a.iter() {
            arg[x + 1] += 1;
        }
        let mut key = vec![0; n];
        for i in 0..n {
            arg[i + 1] += arg[i];
        }
        for (i, &x) in a.iter().enumerate() {
            key[arg[x]] = i;
            arg[x] += 1;
        }
        for c in arg.iter_mut() {
            *c = 0;
        }
        key
    };
    // let mut rank = ArrayCompression::once(a);
    // let mut v = a.clone();
    // v.dedup();
    let mut v = Vec::with_capacity(n);
    for x in a.iter() {
        v.push(x);
    }
    v.sort_unstable();
    v.dedup();
    let mut a: Vec<_> =
        a.iter().map(|x| v.binary_search(&x).unwrap()).collect();
    let mut k = 1usize;
    // let mut key = vec![0; n];
    let mut key_1 = vec![0; n];
    let mut key_10 = vec![0; n];
    let mut sa = vec![0; n];
    loop {
        for i in 0..n {
            key_1[i] = if i + k < n { 1 + a[i + k] } else { 0 };
        }
        let sa_1 = counting_argsort(&key_1);
        for i in 0..n {
            key_10[i] = a[sa_1[i]];
        }
        let sa_10 = counting_argsort(&key_10);
        for i in 0..n {
            sa[i] = sa_1[sa_10[i]];
            // key[i] = key_10[sa_10[i]] << 30 | key_1[sa[i]];
            a[sa[i]] = key_10[sa_10[i]] << 30 | key_1[sa[i]];
        }
        k <<= 1;
        if k >= n {
            return sa;
        }
        let mut rank = 0;
        let mut prev = a[sa[0]];
        for &i in sa.iter() {
            if a[i] > prev {
                rank += 1;
                prev = a[i];
            }
            a[i] = rank;
        }
        if rank == n {
            return sa;
        }
        // a[sa[0]] = 0;
        // for i in 0..n - 1 {
        //     a[sa[i + 1]] = a[sa[i]] + if key[i + 1] > key[i] { 1 } else { 0
        // }; }
    }
}
fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: usize = read();
    let s: String = read();
    let a = s.bytes().map(|x| x as usize).collect::<Vec<_>>();
    let mut sa = suffix_array(&a);
    let mut lcp = lcp_array(&a, &sa);
    let mut sim = vec![0; n];
    for i in 0..n {
        sim[i] += n - i;
    }
    for _ in 0..2 {
        let mut st = vec![(0, 0)];
        let mut s = 0;
        for i in 0..n - 1 {
            let h0 = lcp[i];
            let mut l0 = 1;
            while st.last().unwrap().0 > h0 {
                let (h, l) = st.pop().unwrap();
                l0 += l;
                s -= h * l;
            }
            s += l0 * h0;
            sim[sa[i + 1]] += s;
            st.push((h0, l0));
        }
        sa.reverse();
        lcp.reverse();
    }
    for &s in sim.iter() {
        writeln!(writer, "{}", s).unwrap();
    }
}
