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
    child: Vec<Option<Box<Self>>>,
    size: usize,
    pub value: T,
}
impl<T> Node<T> {
    pub fn new(value: T) -> Box<Self> {
        // const INIT: Option<Box<Self>> = None;
        Box::new(Self { child: vec![None, None], size: 1, value })
    }

    pub(crate) fn size(root: Option<&Box<Self>>) -> usize {
        if let Some(root) = root { root.size } else { 0 }
    }

    fn child_size(&self, i: usize) -> usize {
        Self::size(self.child[i].as_ref())
    }

    fn update(&mut self) {
        self.size = 1;
        for c in self.child.iter() {
            self.size += Self::size(c.as_ref());
        }
    }

    // i = 0 -> up left, 1 -> up right
    fn rotate_up(mut root: Box<Self>, i: usize) -> Box<Self> {
        debug_assert!(i == 0 || i == 1);
        let mut new_root = root.child[i].take().unwrap();
        root.child[i] = new_root.child[i ^ 1].take();
        root.update();
        new_root.child[i ^ 1] = Some(root);
        new_root.update();
        new_root
    }

    // which direction kth node exist?
    fn state(&self, k: usize) -> usize {
        let lsize = self.child_size(0);
        if k < lsize {
            0
        } else if k > lsize {
            1
        } else {
            2 // itself
        }
    }

    pub fn splay(mut root: Box<Self>, mut k: usize) -> Box<Self> {
        assert!(k < root.size);
        let s = root.state(k);
        if s == 2 {
            return root;
        }
        let mut c = root.child[s].take().unwrap();
        k -= (root.child_size(0) + 1) * s;
        let cs = c.state(k);
        if cs == 2 {
            root.child[s] = Some(c);
        } else {
            k -= (c.child_size(0) + 1) * cs;
            if s ^ cs == 0 {
                // zig-zig or zag-zag
                c.child[cs] = Some(Self::splay(c.child[cs].take().unwrap(), k));
                root.child[s] = Some(c);
                root = Self::rotate_up(root, s);
            } else {
                c.child[cs] = Some(Self::splay(c.child[cs].take().unwrap(), k));
                root.child[s] = Some(Self::rotate_up(c, cs));
            }
        }
        Self::rotate_up(root, s)
    }

    pub fn merge(
        l: Option<Box<Self>>, r: Option<Box<Self>>,
    ) -> Option<Box<Self>> {
        if r.is_none() {
            return l;
        }
        let mut r = r.unwrap();
        r = Self::splay(r, 0);
        r.child[0] = l;
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
        let l = root.child[0].take();
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
        let new_root = Self::merge(root.child[0].take(), root.child[1].take());
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
            Self::binary_search(f, root.child[0].as_ref())
        } else {
            let offset = root.child_size(0) + 1;
            offset + Self::binary_search(f, root.child[1].as_ref())
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
