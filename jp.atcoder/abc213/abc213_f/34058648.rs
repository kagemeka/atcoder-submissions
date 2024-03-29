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
pub fn sa_is(mut a: Vec<usize>) -> Vec<usize> {
    let m = *a.iter().min().unwrap();
    for x in a.iter_mut() {
        *x = *x - m + 1;
    }
    a.push(0);
    let n = a.len();
    let m = a.iter().max().unwrap() + 1;
    let mut is_s = vec![true; n];
    let mut is_lms = vec![false; n];
    let mut lms = Vec::with_capacity(n);
    for i in (1..n).rev() {
        is_s[i - 1] = if a[i - 1] == a[i] { is_s[i] } else { a[i - 1] < a[i] };
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
    let induce = |lms: &Vec<usize>| -> Vec<usize> {
        let mut sa = vec![n; n];
        let mut arg = arg_r.clone();
        for &i in lms.iter().rev() {
            arg[a[i]] -= 1;
            sa[arg[a[i]]] = i;
        }
        let mut arg = arg_l.clone();
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
        let mut arg = arg_r.clone();
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
    };
    let l = lms.len();
    let lms_idx = induce(&lms)
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
    rank = rank.into_iter().filter(|&x| x != n).collect();
    let mut lms_order: Vec<usize> = Vec::new();
    if r == l - 1 {
        lms_order.resize(l, n);
        for i in 0..l {
            lms_order[rank[i]] = i;
        }
    } else {
        lms_order = sa_is(rank);
    }
    lms = lms_order.iter().map(|&i| lms[i]).collect();
    let sa = induce(&lms);
    sa[1..].to_vec()
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
pub fn sum_of_lcp(a: &[usize]) -> Vec<usize> {
    let n = a.len();
    let mut sa = sa_is(a.to_vec());
    let mut lcp = lcp_array(&a, &sa);
    let mut similarity: Vec<_> = (1..n + 1).rev().collect();
    for _ in 0..2 {
        let mut st = vec![];
        let mut s = 0;
        for i in 0..n - 1 {
            let height = lcp[i];
            let mut len = 1;
            while let Some((h, l)) = st.last() {
                if h < &height {
                    break;
                }
                len += l;
                s -= h * l;
                st.pop();
            }
            s += height * len;
            similarity[sa[i + 1]] += s;
            st.push((height, len));
        }
        sa.reverse();
        lcp.reverse();
    }
    similarity
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let _n: usize = read();
    let s: String = read();
    let res = sum_of_lcp(&s.chars().map(|x| x as usize).collect::<Vec<_>>());
    for x in res {
        writeln!(writer, "{}", x).unwrap();
    }
}
