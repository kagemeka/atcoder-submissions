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
use std::{
    cmp::Reverse,
    collections::{BinaryHeap, HashMap},
};
pub struct LazyBinaryHeap<T> {
    que: BinaryHeap<T>,
    cnt: HashMap<T, isize>,
    size: usize,
}
impl<T: Ord + std::hash::Hash + Clone> LazyBinaryHeap<T> {
    pub fn new() -> Self {
        Self { que: BinaryHeap::new(), cnt: HashMap::new(), size: 0 }
    }

    pub fn size(&self) -> usize { self.size }

    pub fn count(&self, x: &T) -> isize {
        *self.cnt.get(&x).or_else(|| Some(&0)).unwrap()
    }

    pub fn contains(&self, x: &T) -> bool { self.count(x) > 0 }

    /// if count become negative,
    /// size are not changed as it as negative.
    /// if cnt = -5, heap size would't be changed until inserting at least 6.
    pub fn add(&mut self, x: T, delta: isize) {
        let c = self.cnt.entry(x.clone()).or_insert(0);
        let nc = *c + delta;
        if *c <= 0 && nc > 0 {
            self.que.push(x);
        }
        if delta >= 0 {
            self.size += nc.max(0).min(delta) as usize;
        } else {
            self.size -= (*c).max(0).min(-delta) as usize;
        }
        *c = nc;
    }

    pub fn insert(&mut self, x: T) { self.add(x, 1); }

    pub fn remove(&mut self, x: T) { self.add(x, -1); }

    fn lazy_discard_false_peek(&mut self) {
        while let Some(x) = self.que.peek() {
            if self.count(x) <= 0 {
                self.que.pop();
                continue;
            }
            break;
        }
    }

    pub fn peek(&mut self) -> Option<&T> {
        self.lazy_discard_false_peek();
        self.que.peek()
    }
}
pub struct MedianQueue<T> {
    lo: LazyBinaryHeap<T>,
    hi: LazyBinaryHeap<Reverse<T>>,
}
impl<T: Ord + Clone + std::hash::Hash> MedianQueue<T> {
    pub fn new() -> Self {
        Self { lo: LazyBinaryHeap::new(), hi: LazyBinaryHeap::new() }
    }

    fn balance(&self) -> isize {
        self.lo.size() as isize - self.hi.size() as isize
    }

    fn rebalance(&mut self) {
        let b = self.balance();
        if b == 2 {
            let x = self.lo.peek().unwrap().clone();
            self.lo.remove(x.clone());
            self.hi.insert(Reverse(x));
        } else if b == -1 {
            let x = self.hi.peek().unwrap().clone();
            self.hi.remove(x.clone());
            self.lo.insert(x.0);
        }
    }

    pub fn size(&self) -> usize { self.lo.size() + self.hi.size() }

    pub fn count(&self, x: &T) -> usize {
        self.lo.count(x) as usize + self.hi.count(&Reverse(x.clone())) as usize
    }

    pub fn insert(&mut self, x: T) {
        if self.balance() == 1 {
            self.lo.insert(x);
        } else {
            self.hi.insert(Reverse(x));
        }
        self.rebalance();
    }

    pub fn low(&mut self) -> Option<&T> { self.lo.peek() }

    pub fn high(&mut self) -> Option<&T> {
        if self.balance() == 1 {
            self.low()
        } else {
            if let Some(Reverse(x)) = self.hi.peek() {
                Some(x)
            } else {
                None
            }
        }
    }

    pub fn remove(&mut self, x: &T) {
        assert!(self.count(x) > 0);
        if self.lo.count(x) > 0 {
            self.lo.remove(x.clone());
        } else {
            self.hi.remove(Reverse(x.clone()));
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
            let lo = *que.low().unwrap();
            let hi = *que.high().unwrap();
            (lo + hi) >> 1
        };
        que.remove(&x);
        res
    }
    let mut que = MedianQueue::new();
    let res = dfs(&g, &a, &mut que, 0, n, 0);
    writeln!(writer, "{}", res).unwrap();
}
