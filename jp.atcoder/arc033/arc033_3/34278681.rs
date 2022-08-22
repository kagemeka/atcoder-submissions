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
pub struct Node<T> {
    left: Option<Box<Self>>,
    right: Option<Box<Self>>,
    size: usize,
    pub value: T,
}
impl<T> Node<T> {
    pub fn new(value: T) -> Box<Self> {
        Box::new(Self { left: None, right: None, size: 1, value })
    }

    pub(crate) fn size(root: Option<&Box<Self>>) -> usize {
        if let Some(root) = root { root.size } else { 0 }
    }

    fn left_size(&self) -> usize { Self::size(self.left.as_ref()) }

    fn update(&mut self) {
        let lsize = Self::size(self.left.as_ref());
        let rsize = Self::size(self.right.as_ref());
        self.size = lsize + rsize + 1;
    }

    // counter-clock-wise
    fn rotate_left(mut root: Box<Self>) -> Box<Self> {
        let mut new_root = root.right.take().unwrap();
        root.right = new_root.left.take();
        root.update();
        new_root.left = Some(root);
        new_root.update();
        new_root
    }

    // clock-wise
    fn rotate_right(mut root: Box<Self>) -> Box<Self> {
        let mut new_root = root.left.take().unwrap();
        root.left = new_root.right.take();
        root.update();
        new_root.right = Some(root);
        new_root.update();
        new_root
    }

    fn state(&self, k: usize) -> isize {
        let lsize = self.left_size();
        if k < lsize {
            -1
        } else if k == lsize {
            0
        } else {
            1
        }
    }

    // bring k-th node to the top
    pub fn splay(mut root: Box<Self>, mut k: usize) -> Box<Self> {
        assert!(k < root.size);
        let s = root.state(k);
        if s == 0 {
            return root;
        }
        if s == -1 {
            let mut c = root.left.take().unwrap();
            let cs = c.state(k);
            if cs == 0 {
                root.left = Some(c);
            } else if s * cs == 1 {
                c.left = Some(Self::splay(c.left.take().unwrap(), k));
                root.left = Some(c);
                root = Self::rotate_right(root);
            } else {
                k -= c.left_size() + 1;
                c.right = Some(Self::splay(c.right.take().unwrap(), k));
                c = Self::rotate_left(c);
                root.left = Some(c);
            }
            Self::rotate_right(root)
        } else {
            k -= root.left_size() + 1;
            let mut c = root.right.take().unwrap();
            let cs = c.state(k);
            if cs == 0 {
                root.right = Some(c);
            } else if s * cs == 1 {
                k -= c.left_size() + 1;
                c.right = Some(Self::splay(c.right.take().unwrap(), k));
                root.right = Some(c);
                root = Self::rotate_right(root);
            } else {
                c.left = Some(Self::splay(c.left.take().unwrap(), k));
                c = Self::rotate_right(c);
                root.right = Some(c);
            }
            Self::rotate_left(root)
        }
    }

    pub fn merge(
        l: Option<Box<Self>>, r: Option<Box<Self>>,
    ) -> Option<Box<Self>> {
        if r.is_none() {
            return l;
        }
        let mut r = r.unwrap();
        r = Self::splay(r, 0);
        r.left = l;
        r.update();
        Some(r)
    }

    pub fn split(
        root: Option<Box<Self>>, i: usize,
    ) -> (Option<Box<Self>>, Option<Box<Self>>) {
        let size = Self::size(root.as_ref());
        assert!(i <= size);
        if i == size {
            return (root, None);
        }
        let mut root = root.unwrap();
        root = Self::splay(root, i);
        let l = root.left.take();
        root.update();
        (l, Some(root))
    }

    pub fn insert(
        root: Option<Box<Self>>, i: usize, node: Option<Box<Self>>,
    ) -> Option<Box<Self>> {
        assert!(i <= Self::size(root.as_ref()));
        let (l, r) = Self::split(root, i);
        Self::merge(Self::merge(l, node), r)
    }

    pub fn pop(
        mut root: Box<Self>, i: usize,
    ) -> (Box<Self>, Option<Box<Self>>) {
        root = Self::splay(root, i);
        let new_root = Self::merge(root.left.take(), root.right.take());
        (root, new_root)
    }

    pub fn binary_search<F>(f: F, root: Option<&Box<Self>>) -> usize
    where
        F: Fn(&T) -> bool,
    {
        if root.is_none() {
            return 0;
        }
        let root = root.unwrap();
        if f(&root.value) {
            Self::binary_search(f, root.left.as_ref())
        } else {
            let offset = root.left_size() + 1;
            offset + Self::binary_search(f, root.right.as_ref())
        }
    }
}
pub struct Multiset<T>(Option<Box<Node<T>>>);
impl<T: Ord> Multiset<T> {
    pub fn new() -> Self { Self(None) }

    pub fn size(&self) -> usize { Node::size(self.0.as_ref()) }

    pub fn lower_bound(&self, v: &T) -> usize {
        Node::binary_search(|x| x >= v, self.0.as_ref())
    }

    pub fn upper_bound(&self, v: &T) -> usize {
        Node::binary_search(|x| x > v, self.0.as_ref())
    }

    pub fn count(&self, v: &T) -> usize {
        self.upper_bound(v) - self.lower_bound(v)
    }

    pub fn contains(&self, v: &T) -> bool { self.count(v) > 0 }

    pub fn insert(&mut self, v: T) {
        let i = self.lower_bound(&v);
        self.0 = Node::insert(self.0.take(), i, Some(Node::new(v)));
    }

    pub fn remove(&mut self, v: &T) {
        if !self.contains(v) {
            return;
        }
        let i = self.lower_bound(v);
        self.0 = Node::pop(self.0.take().unwrap(), i).1;
    }

    pub fn get(&mut self, i: usize) -> &T {
        self.0 = Some(Node::splay(self.0.take().unwrap(), i));
        &self.0.as_ref().unwrap().value
    }
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let q: usize = read();
    let mut s = Multiset::new();
    for _ in 0..q {
        let t: u8 = read();
        let x: usize = read();
        if t == 1 {
            s.insert(x);
        } else {
            let v = *s.get(x - 1);
            writeln!(writer, "{}", v).unwrap();
            s.remove(&v);
        }
    }
}
