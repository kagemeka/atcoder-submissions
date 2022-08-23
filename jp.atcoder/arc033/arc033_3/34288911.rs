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
pub struct Node<T> {
    c: [*mut Self; 2],
    size: usize,
    pub v: T,
}
use std::ptr::null_mut;
impl<T> Node<T> {
    pub fn new(v: T) -> Self { Self { c: [null_mut(); 2], size: 1, v } }

    pub(crate) fn size(root: *const Self) -> usize {
        unsafe { root.as_ref() }.map_or(0, |root| root.size)
    }

    fn c_size(&self, i: usize) -> usize { Self::size(self.c[i]) }

    fn update(&mut self) {
        self.size = 1;
        for &c in self.c.iter() {
            self.size += Self::size(c);
        }
    }

    fn rotate_up(&mut self, i: usize) -> &mut Self {
        debug_assert!(i < 2);
        let mut c = unsafe { self.c[i].as_mut().unwrap() };
        self.c[i] = c.c[i ^ 1];
        self.update();
        c.c[i ^ 1] = self;
        c.update();
        c
    }

    fn state(&self, k: usize) -> usize {
        let lsize = self.c_size(0);
        if k < lsize {
            0
        } else if k > lsize {
            1
        } else {
            2 // itself
        }
    }

    pub fn splay(&mut self, mut k: usize) -> &mut Self {
        let mut node = self;
        assert!(k < node.size);
        let s = node.state(k);
        if s == 2 {
            return node;
        }
        let mut c = unsafe { node.c[s].as_mut().unwrap() };
        k -= (node.c_size(0) + 1) * s;
        let cs = c.state(k);
        if cs == 2 {
            node.c[s] = c;
        } else {
            k -= (c.c_size(0) + 1) * cs;
            c.c[cs] = unsafe { c.c[cs].as_mut().unwrap() }.splay(k);
            if s ^ cs == 0 {
                node.c[s] = c;
                node = node.rotate_up(s);
            } else {
                node.c[s] = c.rotate_up(cs);
            }
        }
        node.rotate_up(s)
    }

    pub fn merge(l: *mut Self, r: *mut Self) -> *mut Self {
        if r.is_null() {
            return l;
        }
        let mut r = unsafe { r.as_mut().unwrap() }.splay(0);
        r.c[0] = l;
        r.update();
        r
    }

    pub fn split(root: *mut Self, i: usize) -> (*mut Self, *mut Self) {
        let size = Self::size(root);
        assert!(i <= size);
        if i == size {
            return (root, null_mut());
        }
        let mut root = unsafe { root.as_mut().unwrap() }.splay(i);
        let l = root.c[0];
        root.c[0] = null_mut();
        root.update();
        (l, root)
    }

    pub fn insert(root: *mut Self, i: usize, node: *mut Self) -> *mut Self {
        assert!(i <= Self::size(root));
        let (l, r) = Self::split(root, i);
        Self::merge(Self::merge(l, node), r)
    }

    pub fn pop(&mut self, i: usize) -> (&mut Self, *mut Self) {
        let mut node = self;
        node = Self::splay(node, i);
        let c = Self::merge(node.c[0], node.c[1]);
        node.c[0] = null_mut();
        node.c[1] = null_mut();
        (node, c)
    }

    pub fn binary_search<F>(f: F, root: *const Self) -> usize
    where
        F: Fn(&T) -> bool,
    {
        if root.is_null() {
            return 0;
        }
        let root = unsafe { root.as_ref().unwrap() };
        if f(&root.v) {
            Self::binary_search(f, root.c[0])
        } else {
            root.c_size(0) + 1 + Self::binary_search(f, root.c[1])
        }
    }
}
#[derive(Debug)]
pub struct Multiset<T>(*mut Node<T>);
impl<T: Ord> Multiset<T> {
    pub fn new() -> Self { Self(null_mut()) }

    #[allow(dead_code)]
    pub(crate) fn dbg(&self)
    where
        T: std::fmt::Debug,
    {
        if let Some(root) = unsafe { self.0.as_ref() } {
            dbg!(&root);
        } else {
            dbg!(self.0);
        }
    }

    pub fn size(&self) -> usize { Node::size(self.0) }

    pub fn lower_bound(&self, v: &T) -> usize {
        Node::binary_search(|x| x >= v, self.0)
    }

    pub fn upper_bound(&self, v: &T) -> usize {
        Node::binary_search(|x| x > v, self.0)
    }

    pub fn count(&self, v: &T) -> usize {
        self.upper_bound(v) - self.lower_bound(v)
    }

    pub fn contains(&self, v: &T) -> bool { self.count(v) > 0 }

    pub fn insert(&mut self, v: T) {
        let i = self.lower_bound(&v);
        self.0 = Node::insert(self.0, i, Box::leak(Box::new(Node::new(v))));
    }

    pub fn remove(&mut self, v: &T) {
        if !self.contains(v) {
            return;
        }
        let i = self.lower_bound(v);
        self.0 = unsafe { self.0.as_mut().unwrap() }.pop(i).1;
    }

    pub fn get(&mut self, i: usize) -> T
    where
        T: Clone,
    {
        let root = unsafe { self.0.as_mut().unwrap() }.splay(i);
        let v = root.v.clone();
        self.0 = root;
        v
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
            let v = s.get(x - 1);
            writeln!(writer, "{}", v).unwrap();
            s.remove(&v);
        }
    }
}
