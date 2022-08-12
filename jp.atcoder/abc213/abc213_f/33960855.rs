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
pub fn sa_is(mut a: Vec<usize>) -> Vec<usize> {
    fn preprocess(
        a: &[usize],
    ) -> (Vec<bool>, Vec<bool>, Vec<usize>, Vec<usize>, Vec<usize>) {
        let n = a.len();
        let m = a.iter().max().unwrap() + 1;
        let mut is_s = vec![true; n];
        let mut is_lms = vec![false; n];
        let mut lms = Vec::with_capacity(n);
        for i in (1..n).rev() {
            is_s[i - 1] =
                if a[i - 1] == a[i] { is_s[i] } else { a[i - 1] < a[i] };
            is_lms[i] = !is_s[i - 1] && is_s[i];
            if is_lms[i] {
                lms.push(i);
            }
        }
        lms.reverse();
        let mut arg_l = vec![0; m];
        let mut arg_r = vec![0; m];
        for &x in a.iter() {
            arg_r[x] += 1;
            if x < m - 1 {
                arg_l[x + 1] += 1;
            }
        }
        for i in 0..m - 1 {
            arg_r[i + 1] += arg_r[i];
            arg_l[i + 1] += arg_l[i];
        }
        (is_s, is_lms, lms, arg_l, arg_r)
    }
    fn induced_sort(
        a: &[usize], is_s: &[bool], lms: &[usize], arg_l: &[usize],
        arg_r: &[usize],
    ) -> Vec<usize> {
        let n = a.len();
        let mut sa = vec![n; n];
        let mut arg = arg_r.to_vec();
        for &i in lms.iter().rev() {
            arg[a[i]] -= 1;
            sa[arg[a[i]]] = i;
        }
        let mut arg = arg_l.to_vec();
        for i in 0..n {
            if sa[i] == n || sa[i] == 0 {
                continue;
            }
            let i = sa[i] - 1;
            if !is_s[i] {
                sa[arg[a[i]]] = i;
                arg[a[i]] += 1;
            }
        }
        let mut arg = arg_r.to_vec();
        for i in (0..n).rev() {
            if sa[i] == n || sa[i] == 0 {
                continue;
            }
            let i = sa[i] - 1;
            if is_s[i] {
                arg[a[i]] -= 1;
                sa[arg[a[i]]] = i;
            }
        }
        sa
    }
    fn compute_lms_rank(
        a: &[usize], is_s: &[bool], is_lms: &[bool], lms: &[usize],
        arg_l: &[usize], arg_r: &[usize],
    ) -> Vec<usize> {
        let n = a.len();
        let l = lms.len();
        let lms_idx = induced_sort(a, is_s, lms, arg_l, arg_r)
            .into_iter()
            .filter(|&i| is_lms[i])
            .collect::<Vec<_>>();
        let mut rank = vec![n; n];
        let mut r = 0;
        rank[n - 1] = r;
        for i in 0..l - 1 {
            let j = lms_idx[i];
            let k = lms_idx[i + 1];
            for d in 0..n {
                if a[j + d] != a[k + d] {
                    r += 1;
                    break;
                }
                if d > 0 && is_lms[j + d] {
                    if !is_lms[k + d] {
                        r += 1;
                    }
                    break;
                }
            }
            rank[k] = r;
        }
        rank.into_iter().filter(|&x| x != n).collect()
    }
    let m = *a.iter().min().unwrap();
    for x in a.iter_mut() {
        *x = *x - m + 1;
    }
    a.push(0);
    let mut st = vec![];
    let mut lms_order;
    loop {
        let n = a.len();
        let (is_s, is_lms, lms, arg_l, arg_r) = preprocess(&a);
        let rank = compute_lms_rank(&a, &is_s, &is_lms, &lms, &arg_l, &arg_r);
        let l = lms.len();
        st.push((a, is_s, lms, arg_l, arg_r));
        a = rank;
        if *a.iter().max().unwrap() < l - 1 {
            continue;
        }
        lms_order = vec![n; l];
        for i in 0..l {
            lms_order[a[i]] = i;
        }
        break;
    }
    while let Some((a, is_s, mut lms, arg_l, arg_r)) = st.pop() {
        lms = lms_order.into_iter().map(|i| lms[i]).collect();
        lms_order = induced_sort(&a, &is_s, &lms, &arg_l, &arg_r);
    }
    lms_order[1..].to_vec()
}
fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: usize = read();
    let s: String = read();
    let a = s.bytes().map(|x| x as usize).collect::<Vec<_>>();
    let mut sa = sa_is(a.clone());
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
