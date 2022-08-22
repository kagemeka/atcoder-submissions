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
pub struct Node {
    pivot: usize,
    value: usize,
    left: Option<Box<Self>>,
    right: Option<Box<Self>>,
}
impl Node {
    /// capacity: 2^max_height - 1
    /// 1 <= value < 2^max_height internally,
    pub fn new(value: usize, max_height: usize) -> Option<Box<Self>> {
        assert!(max_height > 0);
        assert!(1 <= value && value < 1 << max_height);
        Some(Box::new(Self {
            pivot: 1 << (max_height - 1),
            value,
            left: None,
            right: None,
        }))
    }

    fn with_pivot(pivot: usize, value: usize) -> Option<Box<Self>> {
        Some(Box::new(Self { pivot, value, left: None, right: None }))
    }

    pub fn insert(&mut self, mut v: usize) {
        use std::mem::swap;
        assert!(v != self.value);
        let p = self.pivot;
        let d = 1 << p.trailing_zeros();
        assert!(d > 1 && p - d < v && v < p + d);
        if v < self.value {}
        if self.value.max(v) <= self.pivot {
            if self.value < v {
                swap(&mut self.value, &mut v);
            }
            if let Some(l) = self.left.as_mut() {
                l.insert(v);
            } else {
                self.left = Self::with_pivot(p - (d >> 1), v);
            }
        } else {
            if self.value > v {
                swap(&mut self.value, &mut v);
            }
            if let Some(r) = self.right.as_mut() {
                r.insert(v);
            } else {
                self.right = Self::with_pivot(p + (d >> 1), v);
            }
        }
    }

    pub fn remove(root: Option<Box<Self>>, v: usize) -> Option<Box<Self>> {
        if root.is_none() {
            return None;
        }
        let mut root = root.unwrap();
        if v < root.value {
            root.left = Self::remove(root.left.take(), v);
        } else if v > root.value {
            root.right = Self::remove(root.right.take(), v);
        } else {
            if let Some(v) = Self::min(root.right.as_ref()) {
                root.value = v;
                root.right = Self::remove(root.right.take(), v);
            } else if let Some(v) = Self::max(root.left.as_ref()) {
                root.value = v;
                root.left = Self::remove(root.left.take(), v);
            } else {
                return None;
            }
        }
        Some(root)
    }

    pub fn min(root: Option<&Box<Self>>) -> Option<usize> {
        if let Some(root) = root {
            Some(if let Some(mn) = Self::min(root.left.as_ref()) {
                mn
            } else {
                root.value
            })
        } else {
            None
        }
    }

    pub fn max(root: Option<&Box<Self>>) -> Option<usize> {
        if let Some(root) = root {
            Some(if let Some(mx) = Self::max(root.right.as_ref()) {
                mx
            } else {
                root.value
            })
        } else {
            None
        }
    }

    pub fn min_ok<F>(is_ok: F, root: Option<&Box<Self>>) -> Option<usize>
    where
        F: Fn(usize) -> bool,
    {
        if root.is_none() {
            return None;
        }
        let root = root.unwrap();
        if is_ok(root.value) {
            Some(if let Some(v) = Self::min_ok(is_ok, root.left.as_ref()) {
                v
            } else {
                root.value
            })
        } else {
            Self::min_ok(is_ok, root.right.as_ref())
        }
    }

    pub fn max_ok<F>(is_ok: F, root: Option<&Box<Self>>) -> Option<usize>
    where
        F: Fn(usize) -> bool,
    {
        if root.is_none() {
            return None;
        }
        let root = root.unwrap();
        if is_ok(root.value) {
            Some(if let Some(v) = Self::max_ok(is_ok, root.right.as_ref()) {
                v
            } else {
                root.value
            })
        } else {
            Self::max_ok(is_ok, root.left.as_ref())
        }
    }

    pub fn iter<'a>(&'a self) -> std::vec::IntoIter<&'a usize> {
        let mut inorder = vec![];
        fn dfs<'b>(res: &mut Vec<&'b usize>, node: &'b Node) {
            if let Some(left) = node.left.as_ref() {
                dfs(res, left);
            }
            res.push(&node.value);
            if let Some(right) = node.right.as_ref() {
                dfs(res, right);
            }
        }
        dfs(&mut inorder, self);
        inorder.into_iter()
    }
}
pub struct PivotSet {
    root: Option<Box<Node>>,
    max_height: usize,
    size: usize,
}
impl PivotSet {
    /// deal with 0 <= x < 2^max_height - 1
    /// without duplicates.
    pub fn new(max_height: usize) -> Self {
        Self { root: None, max_height, size: 0 }
    }

    pub fn size(&self) -> usize { self.size }

    pub fn min_ge(&self, x: usize) -> Option<usize> {
        let v = Node::min_ok(|v| v >= x + 1, self.root.as_ref())?;
        Some(v - 1)
    }

    pub fn max_le(&self, x: usize) -> Option<usize> {
        let v = Node::max_ok(|v| v <= x + 1, self.root.as_ref())?;
        Some(v - 1)
    }

    pub fn contains(&self, x: usize) -> bool {
        if let Some(v) = self.min_ge(x) { v == x } else { false }
    }

    pub fn insert(&mut self, mut x: usize) {
        assert!(x < (1 << self.max_height) - 1);
        if self.contains(x) {
            return;
        }
        x += 1;
        if let Some(root) = self.root.as_mut() {
            root.insert(x);
        } else {
            self.root = Node::new(x, self.max_height)
        }
        self.size += 1;
    }

    pub fn remove(&mut self, x: usize) {
        if !self.contains(x + 1) {
            return;
        }
        self.root = Node::remove(self.root.take(), x + 1);
        self.size -= 1;
    }

    pub fn iter<'a>(&'a self) -> std::vec::IntoIter<&'a usize> {
        self.root.as_ref().unwrap().iter()
    }
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let l: usize = read();
    let q: usize = read();
    let mut s = PivotSet::new(30);
    s.insert(0);
    s.insert(l);
    for _ in 0..q {
        let t: u8 = read();
        let x: usize = read();
        if t == 1 {
            s.insert(x);
        } else {
            let hi = s.min_ge(x).unwrap();
            let lo = s.max_le(x).unwrap();
            writeln!(writer, "{}", hi - lo).unwrap();
        }
    }
}
