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
pub struct ArrayCompression<T>(pub Vec<T>);
impl<T: Ord> ArrayCompression<T> {
    pub fn new(mut a: Vec<T>) -> Self {
        a.sort_unstable();
        a.dedup();
        Self(a)
    }

    pub fn encode(&self, v: &T) -> usize { self.0.binary_search(v).unwrap() }

    pub fn once(a: &[T]) -> Vec<usize>
    where
        T: Clone,
    {
        let f = Self::new(a.to_vec());
        a.iter().map(|x| f.encode(x)).collect()
    }
}
use std::ops::*;
impl<T: Ord> Index<usize> for ArrayCompression<T> {
    type Output = T;

    fn index(&self, i: usize) -> &Self::Output { &self.0[i] }
}
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

    pub fn fold_lt(&self, mut i: usize) -> T
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
pub struct Multiset(Fenwick<i32>);
impl Multiset {
    pub fn new(less_than: usize) -> Self { Self(Fenwick::new(less_than)) }

    pub fn size(&self) -> usize { self.0.fold_lt(self.0.size()) as usize }

    pub fn count(&self, x: usize) -> i32 {
        self.0.fold_lt(x + 1) - self.0.fold_lt(x)
    }

    /// positive cnt: insert.
    /// negative cnt: remove. (|cnt| <= count(x))
    pub fn add(&mut self, x: usize, delta: i32) {
        assert!(self.count(x) + delta >= 0);
        self.0.operate(x, delta);
    }

    pub fn insert(&mut self, x: usize) { self.add(x, 1); }

    pub fn remove(&mut self, x: usize) { self.add(x, -1); }

    pub fn remove_all(&mut self, x: usize) { self.add(x, -self.count(x)); }

    pub fn lower_bound(&self, x: usize) -> usize { self.0.fold_lt(x) as usize }

    pub fn upper_bound(&self, x: usize) -> usize {
        self.0.fold_lt(x + 1) as usize
    }

    pub fn get(&self, i: usize) -> Option<usize> {
        let v = self.0.max_right(|&x| x as usize <= i);
        if v == self.0.size() { None } else { Some(v) }
    }
}
impl Multiset {
    pub fn min(&self) -> Option<usize> { self.get(0) }

    pub fn max(&self) -> Option<usize> { self.get(self.size() - 1) }
}
impl Multiset {
    pub fn low_median(&self) -> Option<usize> {
        self.get((self.size() - 1) >> 1)
    }

    pub fn high_median(&self) -> Option<usize> { self.get(self.size() >> 1) }
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: usize = read();
    let a: Vec<_> = (0..n).map(|_| read::<i32>()).collect();
    let mut g = vec![vec![]; n];
    for _ in 0..n - 1 {
        let u = read::<usize>() - 1;
        let v = read::<usize>() - 1;
        g[u].push(v);
        g[v].push(u);
    }
    fn dfs(
        g: &[Vec<usize>], a: &[i32], f: &ArrayCompression<i32>,
        st: &mut Multiset, u: usize, p: usize, turn: u8,
    ) -> i32 {
        let x = f.encode(&a[u]);
        st.insert(x);
        let mut cand = vec![];
        for &v in g[u].iter() {
            if v == p {
                continue;
            }
            cand.push(dfs(g, a, f, st, v, u, turn ^ 1));
        }
        cand.sort_unstable();
        if turn == 0 {
            cand.reverse();
        }
        let res = if !cand.is_empty() {
            cand[0]
        } else {
            (f[st.low_median().unwrap()] + f[st.high_median().unwrap()]) >> 1
        };
        st.remove(x);
        res
    }
    let f = ArrayCompression::new(a.clone());
    let mut st = Multiset::new(1 << 17);
    let res = dfs(&g, &a, &f, &mut st, 0, n, 0);
    writeln!(writer, "{}", res).unwrap();
}
