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
#[derive(Debug)]
pub struct SqrtBucket<T> {
    pub(crate) buckets: Vec<Vec<T>>,
    size: usize,
}
impl<T> SqrtBucket<T> {
    pub fn new() -> Self { Self { buckets: vec![vec![]], size: 0 } }

    pub fn size(&self) -> usize { self.size }

    fn max_interval(&self) -> usize {
        // isqrt(self.size) << 4;
        self.buckets.len() * 170
    }

    fn rebalance(&mut self) {
        use std::mem::swap;
        if self.size == 0 {
            assert!(self.buckets.len() == 1 && self.buckets[0].len() == 0);
            return;
        }
        // let s = isqrt(self.size) << 3;
        let s = isqrt(self.size) * 7;
        let m = (self.size + s - 1) / s;
        let mut b: Vec<_> = (0..m).map(|_| Vec::with_capacity(s)).collect();
        swap(&mut b, &mut self.buckets);
        for (i, x) in b.into_iter().flatten().enumerate() {
            self.buckets[i / s].push(x);
        }
    }

    /// false, false, ..., true, true
    pub(crate) fn search_bucket<F>(&self, is_ok: F) -> usize
    where
        F: Fn(&T) -> bool,
    {
        debug_assert!(self.size > 0);
        binary_search(
            |j| is_ok(self.buckets[j].last().unwrap()),
            0,
            self.buckets.len() - 1,
        )
    }

    pub(crate) fn search_on_bucket<F>(&self, j: usize, is_ok: F) -> usize
    where
        F: Fn(&T) -> bool,
    {
        let b = &self.buckets[j];
        binary_search(|i| is_ok(&b[i]), 0, b.len())
    }

    pub(crate) fn search_node<F>(&self, is_ok: F) -> (usize, usize)
    where
        F: Fn(&T) -> bool,
    {
        let j = self.search_bucket(&is_ok);
        let k = self.search_on_bucket(j, &is_ok);
        (j, k)
    }

    pub(crate) fn index_of(&self, j: usize, k: usize) -> usize {
        let mut i = 0;
        for b in self.buckets[..j].iter() {
            i += b.len();
        }
        i + k
    }

    pub(crate) fn node_of(&self, mut i: usize) -> (usize, usize) {
        assert!(i <= self.size);
        for (j, b) in self.buckets[..self.buckets.len() - 1].iter().enumerate()
        {
            if i < b.len() {
                return (j, i);
            }
            i -= b.len();
        }
        (self.buckets.len() - 1, i)
    }

    pub fn binary_search<F>(&self, is_ok: F) -> usize
    where
        F: Fn(&T) -> bool,
    {
        let (j, k) = self.search_node(is_ok);
        self.index_of(j, k)
    }

    pub(crate) fn insert_at(&mut self, j: usize, k: usize, x: T) {
        self.buckets[j].insert(k, x);
        self.size += 1;
        if self.buckets[j].len() > self.max_interval() {
            self.rebalance();
        }
    }

    pub fn insert(&mut self, i: usize, x: T) {
        let (j, k) = self.node_of(i);
        self.insert_at(j, k, x);
    }

    pub(crate) fn remove_at(&mut self, j: usize, k: usize) {
        self.buckets[j].remove(k);
        self.size -= 1;
        if self.buckets[j].len() == 0 {
            self.rebalance();
        }
    }

    pub fn remove(&mut self, i: usize) {
        assert!(i < self.size);
        let (j, k) = self.node_of(i);
        self.remove_at(j, k);
    }
}
use std::ops::*;
impl<T> Index<usize> for SqrtBucket<T> {
    type Output = T;

    fn index(&self, i: usize) -> &Self::Output {
        let (j, k) = self.node_of(i);
        &self.buckets[j][k]
    }
}
impl<T> IndexMut<usize> for SqrtBucket<T> {
    fn index_mut(&mut self, i: usize) -> &mut Self::Output {
        let (j, k) = self.node_of(i);
        &mut self.buckets[j][k]
    }
}
pub fn isqrt(n: usize) -> usize {
    if n < 2 {
        return n;
    }
    let mut ok = 0;
    let mut ng = n.min(1 << 32);
    while ng - ok > 1 {
        let x = (ok + ng) >> 1;
        if x * x <= n {
            ok = x;
        } else {
            ng = x;
        }
    }
    ok
}
pub fn binary_search<F>(is_ok: F, mut lo_ok: usize, mut hi_ok: usize) -> usize
where
    F: Fn(usize) -> bool,
{
    while lo_ok != hi_ok {
        let x = (lo_ok + hi_ok) >> 1;
        if is_ok(x) {
            hi_ok = x;
        } else {
            lo_ok = x + 1;
        }
    }
    lo_ok
}
pub struct Multiset<T>(SqrtBucket<T>);
impl<T: Ord> Multiset<T> {
    pub fn new() -> Self { Self(SqrtBucket::new()) }

    pub fn size(&self) -> usize { self.0.size() }

    pub fn lower_bound(&self, x: &T) -> usize {
        let (j, k) = self.0.search_node(|v| v >= x);
        self.0.index_of(j, k)
    }

    pub fn upper_bound(&self, x: &T) -> usize {
        let (j, k) = self.0.search_node(|v| v > x);
        self.0.index_of(j, k)
    }

    pub fn count(&self, x: &T) -> usize {
        self.upper_bound(x) - self.lower_bound(x)
    }

    pub fn insert(&mut self, x: T) {
        let i = self.lower_bound(&x);
        self.0.insert(i, x);
    }

    pub fn remove(&mut self, x: &T) {
        assert!(self.count(x) > 0);
        let i = self.lower_bound(&x);
        self.0.remove(i);
    }
}
impl<T> Index<usize> for Multiset<T> {
    type Output = T;

    fn index(&self, i: usize) -> &Self::Output { &self.0[i] }
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let l: i32 = read();
    let q: usize = read();
    let mut s = Multiset::new();
    s.insert(0);
    s.insert(l);
    for _ in 0..q {
        let t: u8 = read();
        let x: i32 = read();
        if t == 1 {
            s.insert(x);
        } else {
            let i = s.lower_bound(&x);
            writeln!(writer, "{}", s[i] - s[i - 1]).unwrap();
        }
    }
}
