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
pub struct Node {
    pivot: usize,
    pub(crate) value: usize,
    left: Option<Box<Self>>,
    right: Option<Box<Self>>,
    size: usize,
}
// fn capacity(pivot: usize) -> usize {
//     assert!(pivot > 0);
//     (1 << pivot.trailing_zeros() + 1) - 1
// }
impl Node {
    /// capacity: 1 <= value < 2^max_height
    /// 0 <= value < 2^max_height - 1 internally,
    pub fn new(max_height: usize, value: usize) -> Option<Box<Self>> {
        assert!(max_height > 0);
        // assert!(1 <= value && value < 1 << max_height);
        Some(Box::new(Self {
            pivot: 1 << (max_height - 1),
            value,
            left: None,
            right: None,
            size: 1,
        }))
    }

    fn with_pivot(pivot: usize, value: usize) -> Option<Box<Self>> {
        Some(Box::new(Self {
            pivot,
            value,
            left: None,
            right: None,
            size: 1,
        }))
    }

    // fn capacity(root: Option<&Box<Self>>) -> usize {
    //     if let Some(root) = root { capacity(root.pivot) } else { 0 }
    // }
    pub(crate) fn size(node: Option<&Box<Self>>) -> usize {
        if let Some(node) = node { node.size } else { 0 }
    }

    pub fn update(&mut self) {
        self.size = Self::size(self.left.as_ref())
            + Self::size(self.right.as_ref())
            + 1;
    }

    pub fn insert(&mut self, mut v: usize) {
        use std::mem::swap;
        assert!(v != self.value);
        let p = self.pivot;
        let d = 1 << p.trailing_zeros();
        assert!(d > 1 && p - d < v && v < p + d);
        // if self.value.max(v) <= self.pivot {
        if self.value.min(v) < self.pivot {
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
        self.update();
        // self.size += 1;
    }

    pub fn remove(mut root: Box<Self>, i: usize) -> Option<Box<Self>> {
        assert!(i < root.size);
        let lsize = Self::size(root.left.as_ref());
        if i < lsize {
            root.left = Self::remove(root.left.take().unwrap(), i);
        } else if i > lsize {
            root.right =
                Self::remove(root.right.take().unwrap(), i - lsize - 1);
        } else {
            if let Some(right) = root.right.take() {
                root.value = right.kth_node(0).value;
                root.right = Self::remove(right, 0);
            } else if let Some(left) = root.left.take() {
                root.value = left.kth_node(lsize - 1).value;
                root.left = Self::remove(left, lsize - 1);
            } else {
                return None;
            }
        }
        root.update();
        Some(root)
    }

    pub fn kth_node(&self, k: usize) -> &Self {
        // dbg!(self.size, k, self.pivot);
        assert!(k < self.size);
        let lsize = Self::size(self.left.as_ref());
        // dbg!(lsize);
        if k < lsize {
            self.left.as_ref().unwrap().kth_node(k)
        } else if k == lsize {
            self
        } else {
            self.right.as_ref().unwrap().kth_node(k - lsize - 1)
        }
    }

    pub fn binary_search<F>(f: F, root: Option<&Box<Self>>) -> usize
    where
        F: Fn(usize) -> bool,
    {
        if root.is_none() {
            return 0;
        }
        let root = root.unwrap();
        if f(root.value) {
            Self::binary_search(f, root.left.as_ref())
        } else {
            let offset = Self::size(root.left.as_ref()) + 1;
            offset + Self::binary_search(f, root.right.as_ref())
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
}
impl PivotSet {
    pub fn new(max_height: usize) -> Self { Self { root: None, max_height } }

    pub fn size(&self) -> usize { Node::size(self.root.as_ref()) }

    pub fn lower_bound(&self, x: usize) -> usize {
        Node::binary_search(|v| v >= x + 1, self.root.as_ref())
    }

    pub fn upper_bound(&self, x: usize) -> usize {
        Node::binary_search(|v| v > x + 1, self.root.as_ref())
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
        if let Some(root) = self.root.as_mut() {
            root.insert(x);
        } else {
            self.root = Node::new(self.max_height, x);
        }
    }

    pub fn remove(&mut self, x: usize) {
        if !self.contains(x) {
            return;
        }
        let i = self.lower_bound(x);
        self.root = Node::remove(self.root.take().unwrap(), i);
    }

    pub fn iter<'a>(&'a self) -> std::vec::IntoIter<&'a usize> {
        self.root.as_ref().unwrap().iter()
    }

    pub fn get(&self, i: usize) -> usize {
        self.root.as_ref().unwrap().kth_node(i).value - 1
    }
}

pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let q: usize = read();
    let mut s = PivotSet::new(30);
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
