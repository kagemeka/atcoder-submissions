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
pub fn suffix_array<T: Ord>(a: &[T]) -> Vec<usize> {
    let n = a.len();
    // let mut arg = vec![0; n + 2];
    // let mut counting_argsort = |a: &Vec<usize>| -> Vec<usize> {
    //     let mut mx = 0;
    //     for &x in a.iter() {
    //         arg[x + 1] += 1;
    //         mx = mx.max(x + 1);
    //     }
    //     let mut key = vec![0; n];
    //     for i in 0..mx - 1 {
    //         arg[i + 1] += arg[i];
    //     }
    //     for (i, &x) in a.iter().enumerate() {
    //         key[arg[x]] = i;
    //         arg[x] += 1;
    //     }
    //     for i in 0..=mx {
    //         arg[i] = 0;
    //     }
    //     key
    // };
    fn counting_argsort(a: &Vec<usize>) -> Vec<usize> {
        let n = a.len();
        let mut arg = vec![0; n + 2];
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
        key
    }
    let mut v = Vec::with_capacity(n);
    for x in a.iter() {
        v.push(x);
    }
    v.sort_unstable();
    v.dedup();
    let mut a: Vec<_> =
        a.iter().map(|x| v.binary_search(&x).unwrap() + 1).collect();
    let mut k = 1usize;
    loop {
        let key_1 =
            (0..n).map(|i| if i + k < n { a[i + k] } else { 0 }).collect();
        let sa_1 = counting_argsort(&key_1);
        let key_0 = sa_1.iter().map(|&i| a[i]).collect();
        let sa_0 = counting_argsort(&key_0);
        let sa: Vec<_> = sa_0.iter().map(|&i| sa_1[i]).collect();
        let key: Vec<_> = sa_0
            .iter()
            .zip(sa.iter())
            .map(|(&i, &j)| key_0[i] << 30 | key_1[j])
            .collect();
        k <<= 1;
        if k >= n {
            return sa;
        }
        let mut rank = 0;
        let mut prev = 0;
        for (&sa, &key) in sa.iter().zip(key.iter()) {
            if key > prev {
                rank += 1;
                prev = key;
            }
            a[sa] = rank;
        }
        if rank == n {
            return sa;
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
