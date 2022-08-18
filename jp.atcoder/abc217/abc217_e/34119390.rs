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
    collections::{BinaryHeap, VecDeque},
};
pub struct SortableQueue<T> {
    que: VecDeque<T>,
    hq: BinaryHeap<Reverse<T>>,
}
impl<T: Ord> SortableQueue<T> {
    pub fn new() -> Self {
        Self { que: VecDeque::new(), hq: BinaryHeap::new() }
    }

    pub fn size(&self) -> usize { self.que.len() + self.hq.len() }

    pub fn push(&mut self, x: T) { self.que.push_back(x); }

    pub fn sort(&mut self) {
        while let Some(x) = self.que.pop_front() {
            self.hq.push(Reverse(x));
        }
    }

    pub fn pop(&mut self) -> Option<T> {
        if self.size() == 0 {
            return None;
        }
        Some(if self.hq.is_empty() {
            self.que.pop_front().unwrap()
        } else {
            self.hq.pop().unwrap().0
        })
    }
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let q: usize = read();
    let mut que = SortableQueue::new();
    for _ in 0..q {
        let t: u8 = read();
        if t == 1 {
            let x: i32 = read();
            que.push(x);
        } else if t == 2 {
            writeln!(writer, "{}", que.pop().unwrap()).unwrap();
        } else {
            que.sort();
        }
    }
}
