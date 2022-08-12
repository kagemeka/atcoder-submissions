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
    for i in 0..n {
        rank[sa[i]] = i;
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
pub fn suffix_array(mut a: Vec<usize>) -> Vec<usize> {
    let n = a.len();
    let mut d = 1;
    let mut sa: Vec<_> = (0..n).collect();
    loop {
        for i in 0..n {
            a[i] <<= 30;
            if i + d < n {
                a[i] |= 1 + a[i + d];
            }
        }
        sa.sort_unstable_by_key(|&i| a[i]);
        d <<= 1;
        if d >= n {
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
    }
}
fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: usize = read();
    let s: String = read();
    let a = s.bytes().map(|x| x as usize).collect::<Vec<_>>();
    let mut sa = suffix_array(a.clone());
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
