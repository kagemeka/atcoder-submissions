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
use std::collections::BTreeMap;
pub struct MinMaxQueue<T> {
    map: BTreeMap<T, usize>,
    size: usize,
}
impl<T: Ord> MinMaxQueue<T> {
    pub fn new() -> Self { Self { map: BTreeMap::new(), size: 0 } }

    pub fn size(&self) -> usize { self.size }

    pub fn count(&self, x: &T) -> usize {
        *self.map.get(x).or_else(|| Some(&0)).unwrap()
    }

    pub fn insert(&mut self, x: T, count: usize) {
        *self.map.entry(x).or_insert(0) += count;
        self.size += count;
    }

    pub fn remove(&mut self, x: &T, count: usize) {
        let c = self.map.get_mut(x).unwrap();
        *c -= count;
        if *c == 0 {
            self.map.remove(x);
        }
        self.size -= count;
    }

    pub fn min(&self) -> Option<&T> {
        if let Some((x, _)) = self.map.iter().next() {
            Some(x)
        } else {
            None
        }
    }

    pub fn max(&self) -> Option<&T> {
        if let Some((x, _)) = self.map.iter().next_back() {
            Some(x)
        } else {
            None
        }
    }
}
pub type Multiset<T> = MinMaxQueue<T>;
pub struct MedianQueue<T> {
    lo: Multiset<T>,
    hi: Multiset<T>,
}
impl<T: Ord + Clone> MedianQueue<T> {
    pub fn new() -> Self { Self { lo: Multiset::new(), hi: Multiset::new() } }

    fn balance(&self) -> isize {
        self.lo.size() as isize - self.hi.size() as isize
    }

    fn rebalance(&mut self) {
        let b = self.balance();
        if b == 2 {
            let x = self.lo.max().unwrap().clone();
            self.lo.remove(&x, 1);
            self.hi.insert(x, 1);
        } else if b == -1 {
            let x = self.hi.min().unwrap().clone();
            self.hi.remove(&x, 1);
            self.lo.insert(x, 1);
        }
    }

    pub fn size(&self) -> usize { self.lo.size() + self.hi.size() }

    pub fn count(&self, x: &T) -> usize { self.lo.count(x) + self.hi.count(x) }

    pub fn insert(&mut self, x: T) {
        if self.balance() == 1 {
            self.lo.insert(x, 1);
        } else {
            self.hi.insert(x, 1);
        }
        self.rebalance();
    }

    pub fn low(&self) -> Option<&T> { self.lo.max() }

    pub fn high(&self) -> Option<&T> {
        if self.balance() == 1 { self.low() } else { self.hi.min() }
    }

    pub fn remove(&mut self, x: &T) {
        assert!(self.count(x) > 0);
        if self.lo.count(x) > 0 {
            self.lo.remove(x, 1);
        } else {
            self.hi.remove(x, 1);
        }
        self.rebalance();
    }
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
        g: &[Vec<usize>], a: &[i32], que: &mut MedianQueue<i32>, u: usize,
        p: usize, turn: u8,
    ) -> i32 {
        let x = a[u];
        que.insert(x);
        let mut cand = vec![];
        for &v in g[u].iter() {
            if v == p {
                continue;
            }
            cand.push(dfs(g, a, que, v, u, turn ^ 1));
        }
        cand.sort_unstable();
        if turn == 0 {
            cand.reverse();
        }
        let res = if !cand.is_empty() {
            cand[0]
        } else {
            (que.low().unwrap() + que.high().unwrap()) >> 1
        };
        que.remove(&x);
        res
    }
    let mut que = MedianQueue::new();
    let res = dfs(&g, &a, &mut que, 0, n, 0);
    writeln!(writer, "{}", res).unwrap();
}
