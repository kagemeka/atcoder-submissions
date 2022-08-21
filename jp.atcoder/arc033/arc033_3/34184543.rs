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
pub struct SqrtDecomposition {
    data: Vec<i64>,
    buckets: Vec<i64>,
}
impl SqrtDecomposition
where
    i64: Clone,
{
    pub fn size(&self) -> usize { self.data.len() }

    pub fn interval(&self) -> usize {
        let n = self.buckets.len();
        (self.size() + n - 1) / n
    }

    pub fn new(size: usize) -> Self {
        let data = vec![0; size];
        let m = isqrt(size);
        let buckets = vec![0; (size + m - 1) / m];
        Self { data, buckets }
    }

    fn merge(&mut self, j: usize) {
        let n = self.interval();
        self.buckets[j] = self.data[j * n..self.size().min((j + 1) * n)]
            .iter()
            .cloned()
            .fold(0, |x, y| x + y)
    }

    pub fn set(&mut self, i: usize, x: i64) {
        self.data[i] = x;
        self.merge(i / self.interval());
    }

    pub fn fold(&self, l: usize, r: usize) -> i64 {
        assert!(l <= r && r <= self.size());
        let n = self.interval();
        let mut v = 0;
        let lj = (l + n - 1) / n;
        let rj = r / n;
        if rj < lj {
            for x in self.data[l..r].iter() {
                v += x;
            }
            return v;
        }
        for x in self.data[l..lj * n].iter() {
            v += x;
        }
        for x in self.buckets[lj..rj].iter() {
            v += x;
        }
        for x in self.data[rj * n..r].iter() {
            v += x;
        }
        v
    }

    pub fn max_right<F>(&self, is_ok: F, l: usize) -> usize
    where
        F: Fn(&i64) -> bool,
    {
        let m = self.interval();
        let n = self.size();
        let lj = (l + m - 1) / m;
        let mut v = 0;
        for i in l..lj * m {
            let nv = v + self.data[i];
            if !is_ok(&nv) {
                return i;
            }
            v = nv;
        }
        let mut i = n;
        for j in lj..self.buckets.len() {
            let nv = v + self.buckets[j];
            if !is_ok(&nv) {
                i = j * m;
                break;
            }
            v = nv;
        }
        while i < n {
            let nv = v + self.data[i];
            if !is_ok(&nv) {
                return i;
            }
            v = nv;
            i += 1;
        }
        i
    }

    pub fn min_left<F>(&self, is_ok: F, r: usize) -> usize
    where
        F: Fn(&i64) -> bool,
    {
        let m = self.interval();
        let rj = r / m;
        let mut v = 0;
        for i in (rj * m..r).rev() {
            let nv = self.data[i] + v;
            if !is_ok(&nv) {
                return i + 1;
            }
            v = nv;
        }
        let mut i = 0;
        for j in (0..rj).rev() {
            let nv = self.buckets[j] + v;
            if !is_ok(&nv) {
                i = (j + 1) * m;
                break;
            }
            v = nv;
        }
        while i > 0 {
            i -= 1;
            let nv = self.data[i] + v;
            if !is_ok(&nv) {
                return i + 1;
            }
            v = nv;
        }
        i
    }
}
use std::ops::*;
impl Index<usize> for SqrtDecomposition {
    type Output = i64;

    fn index(&self, i: usize) -> &Self::Output { &self.data[i] }
}
impl From<&[i64]> for SqrtDecomposition {
    fn from(data: &[i64]) -> Self {
        let mut sqd = SqrtDecomposition::new(data.len());
        sqd.data.clone_from_slice(data);
        for j in 0..sqd.buckets.len() {
            sqd.merge(j);
        }
        sqd
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
pub struct Multiset(SqrtDecomposition);
impl Multiset {
    pub fn new(less_than: usize) -> Self {
        Self(SqrtDecomposition::new(less_than))
    }

    pub fn size(&self) -> usize { self.0.fold(0, self.0.size()) as usize }

    pub fn count(&self, x: usize) -> i64 { self.0.fold(x, x + 1) }

    /// positive cnt: insert.
    /// negative cnt: remove. (|cnt| <= count(x))
    pub fn add(&mut self, x: usize, delta: i64) {
        assert!(self.count(x) + delta >= 0);
        self.0.set(x, self.0[x] + delta);
    }

    pub fn insert(&mut self, x: usize) { self.add(x, 1); }

    pub fn remove(&mut self, x: usize) { self.add(x, -1); }

    pub fn remove_all(&mut self, x: usize) { self.add(x, -self.count(x)); }

    pub fn lower_bound(&self, x: usize) -> usize { self.0.fold(0, x) as usize }

    pub fn upper_bound(&self, x: usize) -> usize {
        self.0.fold(0, x + 1) as usize
    }

    pub fn get(&self, i: usize) -> Option<usize> {
        let v = self.0.max_right(|&x| x as usize <= i, 0);
        if v == self.0.size() { None } else { Some(v) }
    }
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let q: usize = read();
    let mut s = Multiset::new(1 << 18);
    for _ in 0..q {
        let t: u8 = read();
        let x: usize = read();
        if t == 1 {
            s.insert(x);
        } else {
            let v = s.get(x - 1).unwrap();
            writeln!(writer, "{}", v).unwrap();
            s.remove(v);
        }
    }
}
