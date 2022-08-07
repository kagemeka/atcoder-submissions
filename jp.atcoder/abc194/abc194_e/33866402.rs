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
use std::collections::{BinaryHeap, HashMap};
pub struct LazyBinaryHeap<T> {
    que: BinaryHeap<T>,
    cnt: HashMap<T, isize>,
}
impl<T: Ord + std::hash::Hash + Clone> LazyBinaryHeap<T> {
    pub fn new() -> Self {
        Self { que: BinaryHeap::new(), cnt: HashMap::new() }
    }

    pub fn count(&self, x: &T) -> isize {
        *self.cnt.get(&x).or_else(|| Some(&0)).unwrap()
    }

    pub fn contains(&self, x: &T) -> bool { self.count(x) > 0 }

    pub fn add(&mut self, x: T, delta: isize) {
        let c = self.cnt.entry(x.clone()).or_insert(0);
        if *c <= 0 && *c + delta > 0 {
            self.que.push(x);
        }
        *c += delta;
    }

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
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: usize = read();
    let m: usize = read();
    use std::cmp::Reverse;
    let a: Vec<_> = (0..n).map(|_| read::<usize>()).collect();
    let mut que = LazyBinaryHeap::new();
    for i in 0..=n + 1 {
        que.add(Reverse(i), 1);
    }
    for i in 0..m {
        que.add(Reverse(a[i]), -1);
    }
    let mut mn = que.peek().unwrap().0;
    for i in m..n {
        que.add(Reverse(a[i - m]), 1);
        que.add(Reverse(a[i]), -1);
        mn = mn.min(que.peek().unwrap().0);
    }
    writeln!(writer, "{}", mn).unwrap();
}
