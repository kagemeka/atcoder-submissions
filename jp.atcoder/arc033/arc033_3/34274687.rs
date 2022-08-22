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
pub struct PivotTreeSet {
    data: Vec<Option<usize>>,
    size: Vec<usize>,
    max_height: usize,
}
fn left(pivot: usize) -> usize { pivot - (1 << pivot.trailing_zeros() - 1) }
fn right(pivot: usize) -> usize { pivot + (1 << pivot.trailing_zeros() - 1) }
impl PivotTreeSet {
    pub fn new(max_height: usize) -> Self {
        assert!(max_height > 0);
        let n = 1 << max_height;
        Self { data: vec![None; n], size: vec![0; n], max_height }
    }

    fn root_pivot(&self) -> usize { 1 << self.max_height - 1 }

    fn left_size(&self, p: usize) -> usize {
        if p & 1 == 1 { 0 } else { self.size[left(p)] }
    }

    fn right_size(&self, p: usize) -> usize {
        if p & 1 == 1 { 0 } else { self.size[right(p)] }
    }

    pub fn size(&self) -> usize { self.size[self.root_pivot()] }

    fn update(&mut self, p: usize) {
        if self.data[p].is_none() {
            self.size[p] = 0;
            return;
        }
        self.size[p] = self.left_size(p) + self.right_size(p) + 1;
    }

    pub fn _insert(&mut self, p: usize, mut v: usize) {
        use std::mem::swap;
        let value = self.data[p];
        if value.is_none() {
            debug_assert!(self.size[p] == 0);
            self.data[p] = Some(v);
            self.size[p] = 1;
            return;
        }
        let mut value = value.unwrap();
        if v == value {
            return;
        }
        let d = 1 << p.trailing_zeros();
        assert!(p - d < v && v < p + d);
        if value.min(v) < p {
            if value < v {
                swap(&mut value, &mut v);
            }
            self.data[p] = Some(value);
            self._insert(left(p), v);
        } else {
            if value > v {
                swap(&mut value, &mut v);
            }
            self.data[p] = Some(value);
            self._insert(right(p), v);
        }
        self.update(p);
    }

    fn _remove(&mut self, p: usize, i: usize) {
        assert!(i < self.size[p]);
        let lsize = self.left_size(p);
        if i < lsize {
            self._remove(left(p), i);
        } else if i > lsize {
            self._remove(right(p), i - lsize - 1);
        } else {
            if self.right_size(p) > 0 {
                let rp = right(p);
                self.data[p] = Some(self.kth_value(rp, 0));
                self._remove(rp, 0);
            } else if lsize > 0 {
                let lp = left(p);
                self.data[p] = Some(self.kth_value(lp, lsize - 1));
                self._remove(lp, lsize - 1);
            } else {
                self.data[p] = None;
            }
        }
        self.update(p);
    }

    fn kth_value(&self, p: usize, k: usize) -> usize {
        assert!(k < self.size[p]);
        let lsize = self.left_size(p);
        if k < lsize {
            self.kth_value(left(p), k)
        } else if k == lsize {
            self.data[p].unwrap()
        } else {
            self.kth_value(right(p), k - lsize - 1)
        }
    }

    fn binary_search<F>(&self, f: F, p: usize) -> usize
    where
        F: Fn(usize) -> bool,
    {
        let v = self.data[p];
        if v.is_none() {
            return 0;
        }
        let v = v.unwrap();
        if f(v) {
            if p & 1 == 1 { 0 } else { self.binary_search(f, left(p)) }
        } else {
            let i = self.left_size(p) + 1;
            i + if p & 1 == 1 { 0 } else { self.binary_search(f, right(p)) }
        }
    }

    pub fn get(&self, i: usize) -> usize {
        self.kth_value(self.root_pivot(), i) - 1
    }

    pub fn lower_bound(&self, x: usize) -> usize {
        self.binary_search(|v| v >= x + 1, self.root_pivot())
    }

    pub fn upper_bound(&self, x: usize) -> usize {
        self.binary_search(|v| v > x + 1, self.root_pivot())
    }

    pub fn count(&self, x: usize) -> usize {
        self.upper_bound(x) - self.lower_bound(x)
    }

    pub fn contains(&self, x: usize) -> bool { self.count(x) > 0 }

    pub fn insert(&mut self, mut x: usize) {
        assert!(x < (1 << self.max_height) - 1);
        if self.contains(x) {
            return;
        }
        x += 1;
        self._insert(self.root_pivot(), x);
    }

    pub fn remove(&mut self, x: usize) {
        if !self.contains(x) {
            return;
        }
        let i = self.lower_bound(x);
        self._remove(self.root_pivot(), i);
    }
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let q: usize = read();
    let mut s = PivotTreeSet::new(18);
    for _ in 0..q {
        let t: u8 = read();
        let x: usize = read();
        if t == 1 {
            s.insert(x);
        } else {
            let v = s.get(x - 1);
            writeln!(writer, "{}", v).unwrap();
            s.remove(v);
        }
        // dbg!(&s.root);
    }
}
