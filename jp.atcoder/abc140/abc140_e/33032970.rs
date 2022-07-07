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
pub mod fenwick_tree_additive {
    use std::ops::*;
    /// fenwick tree additive
    pub struct Fenwick<T>(Vec<T>);
    impl<T> Fenwick<T> {
        pub fn size(&self) -> usize { self.0.len() - 1 }

        pub fn new(size: usize) -> Self
        where
            T: From<i32>,
        {
            Self((0..size + 1).map(|_| 0.into()).collect())
        }

        pub fn operate(&mut self, mut i: usize, x: T)
        where
            T: AddAssign + Clone,
        {
            i += 1;
            while i <= self.size() {
                self.0[i] += x.clone();
                i += 1 << i.trailing_zeros();
            }
        }

        pub fn get(&self, mut i: usize) -> T
        where
            T: From<i32> + AddAssign + Clone,
        {
            let mut v = 0.into();
            while i > 0 {
                v += self.0[i].clone();
                i -= 1 << i.trailing_zeros();
            }
            v
        }

        pub fn max_right<F: Fn(&T) -> bool>(&self, f: F) -> usize
        where
            T: From<i32> + Add<Output = T> + Clone,
        {
            let n = self.size();
            let mut d = (n + 1).next_power_of_two();
            let mut v: T = 0.into();
            let mut i = 0;
            loop {
                d >>= 1;
                if d == 0 {
                    return i;
                }
                if i + d > n {
                    continue;
                }
                let nv = v.clone() + self.0[i + d].clone();
                if f(&nv) {
                    v = nv;
                    i += d;
                }
            }
        }
    }
}
pub mod fenwick_tree_multiset {
    use crate::fenwick_tree_additive::Fenwick;
    pub struct Multiset(Fenwick<i32>);
    impl Multiset {
        pub fn new(less_than: usize) -> Self { Self(Fenwick::new(less_than)) }

        pub fn size(&self) -> usize { self.0.get(self.0.size()) as usize }

        pub fn count(&self, x: usize) -> i32 {
            self.0.get(x + 1) - self.0.get(x)
        }

        pub fn add(&mut self, x: usize, cnt: i32) { self.0.operate(x, cnt); }

        pub fn lower_bound(&self, x: usize) -> usize { self.0.get(x) as usize }

        pub fn upper_bound(&self, x: usize) -> usize {
            self.0.get(x + 1) as usize
        }

        pub fn get(&self, i: usize) -> usize {
            self.0.max_right(|&x| x as usize <= i)
        }
    }
}
fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: usize = read();
    let p = (0..n).map(|_| read::<usize>() - 1).collect::<Vec<_>>();
    let mut indices = vec![0; n];
    for i in 0..n {
        indices[p[i]] = i;
    }
    let mut s = fenwick_tree_multiset::Multiset::new(n + 2);
    s.add(0, 2);
    s.add(n + 1, 2);
    let mut tot = 0usize;
    for x in (1..=n).rev() {
        let i = indices[x - 1] + 1;
        s.add(i, 1);
        let k = s.lower_bound(i);
        let (j0, j1, j2, j3) =
            (s.get(k - 2), s.get(k - 1), s.get(k + 1), s.get(k + 2));
        tot += x * ((j1 - j0) * (j2 - i) + (i - j1) * (j3 - j2));
    }
    writeln!(writer, "{}", tot).unwrap();
}
