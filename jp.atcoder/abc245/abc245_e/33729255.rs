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
    pub left: Option<Box<Node<T>>>,
    pub right: Option<Box<Node<T>>>,
    pub height: usize,
    pub size: usize,
    pub value: T,
}
impl<T> Node<T> {
    pub fn new(value: T) -> Box<Self> {
        Box::new(Self { left: None, right: None, height: 1, size: 1, value })
    }

    pub(crate) fn height(node: Option<&Box<Self>>) -> usize {
        if let Some(node) = node { node.height } else { 0 }
    }

    pub(crate) fn size(node: Option<&Box<Self>>) -> usize {
        if let Some(node) = node { node.size } else { 0 }
    }

    pub(crate) fn balance(node: Option<&Box<Self>>) -> isize {
        if let Some(node) = node {
            Self::height(node.right.as_ref()) as isize
                - Self::height(node.left.as_ref()) as isize
        } else {
            0
        }
    }

    pub(crate) fn update(root: &mut Box<Self>) {
        let hl = Self::height(root.left.as_ref());
        let hr = Self::height(root.right.as_ref());
        root.height = hl.max(hr) + 1;
        let sl = Self::size(root.left.as_ref());
        let sr = Self::size(root.right.as_ref());
        root.size = sl + sr + 1;
    }

    pub(crate) fn rotate_left(mut root: Box<Self>) -> Box<Self> {
        let mut new_root = root.right.take().unwrap();
        root.right = new_root.left.take();
        Self::update(&mut root);
        new_root.left = Some(root);
        Self::update(&mut new_root);
        new_root
    }

    pub(crate) fn rotate_right(mut root: Box<Self>) -> Box<Self> {
        let mut new_root = root.left.take().unwrap();
        root.left = new_root.right.take();
        Self::update(&mut root);
        new_root.right = Some(root);
        Self::update(&mut new_root);
        new_root
    }

    pub(crate) fn rebalance(mut root: Box<Self>) -> Box<Self> {
        Self::update(&mut root);
        let b = Self::balance(Some(&root));
        if b < -1 {
            if Self::balance(root.left.as_ref()) > 0 {
                root.left = Some(Self::rotate_left(root.left.take().unwrap()));
            }
            return Self::rotate_right(root);
        } else if b > 1 {
            if Self::balance(root.right.as_ref()) < 0 {
                root.right =
                    Some(Self::rotate_right(root.right.take().unwrap()));
            }
            return Self::rotate_left(root);
        }
        root
    }

    pub fn insert(
        root: Option<Box<Self>>, i: usize, node: Box<Self>,
    ) -> Box<Self> {
        assert!(i <= Self::size(root.as_ref()));
        if root.is_none() {
            return node;
        }
        let mut root = root.unwrap();
        let lsize = Self::size(root.left.as_ref());
        if i <= lsize {
            root.left = Some(Self::insert(root.left.take(), i, node));
        } else {
            root.right =
                Some(Self::insert(root.right.take(), i - lsize - 1, node));
        }
        Self::rebalance(root)
    }

    pub(crate) fn pop_last(
        mut root: Box<Self>,
    ) -> (Box<Self>, Option<Box<Self>>) {
        if root.right.is_none() {
            let new_root = root.left.take();
            return (root, new_root);
        }
        let (max_node, new_right) = Self::pop_last(root.right.take().unwrap());
        root.right = new_right;
        (max_node, Some(Self::rebalance(root)))
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
            if root.left.is_none() {
                return root.right;
            }
            let (max_node, new_left) =
                Self::pop_last(root.left.take().unwrap());
            root.left = new_left;
            root.value = max_node.value;
        }
        Some(Self::rebalance(root))
    }

    pub fn kth_node(root: &Box<Self>, k: usize) -> &Box<Self> {
        assert!(k < root.size);
        let lsize = Self::size(root.left.as_ref());
        if k < lsize {
            Self::kth_node(root.left.as_ref().unwrap(), k)
        } else if k > lsize {
            Self::kth_node(root.right.as_ref().unwrap(), k - lsize - 1)
        } else {
            root
        }
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
            let offset = Self::size(root.left.as_ref()) + 1;
            offset + Self::binary_search(f, root.right.as_ref())
        }
    }

    pub fn iter<'a>(&'a self) -> std::vec::IntoIter<&'a T> {
        let mut inorder = vec![];
        fn dfs<'b, T>(res: &mut Vec<&'b T>, node: &'b Node<T>) {
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
impl<T> IntoIterator for Node<T> {
    type IntoIter = std::vec::IntoIter<Self::Item>;
    type Item = T;

    fn into_iter(self) -> Self::IntoIter {
        let mut inorder = vec![];
        fn dfs<T>(res: &mut Vec<T>, mut node: Node<T>) {
            if let Some(left) = node.left.take() {
                dfs(res, *left);
            }
            res.push(node.value);
            if let Some(right) = node.right.take() {
                dfs(res, *right);
            }
        }
        dfs(&mut inorder, self);
        inorder.into_iter()
    }
}
#[derive(Debug)]
pub struct AVLMultiset<T>(Option<Box<Node<T>>>);
impl<T: Ord> AVLMultiset<T> {
    pub fn new() -> Self { Self(None) }

    pub fn size(&self) -> usize { Node::size(self.0.as_ref()) }

    pub fn lower_bound(&self, value: &T) -> usize {
        Node::binary_search(|v| v >= &value, self.0.as_ref())
    }

    pub fn upper_bound(&self, value: &T) -> usize {
        Node::binary_search(|v| v > &value, self.0.as_ref())
    }

    pub fn count(&self, value: &T) -> usize {
        self.upper_bound(value) - self.lower_bound(value)
    }

    pub fn contains(&self, value: &T) -> bool { self.count(value) > 0 }

    pub fn insert(&mut self, value: T) {
        let i = self.lower_bound(&value);
        self.0 = Some(Node::insert(self.0.take(), i, Node::new(value)));
    }

    pub fn remove(&mut self, value: &T) {
        if !self.contains(value) {
            return;
        }
        let i = self.lower_bound(value);
        self.0 = Node::remove(self.0.take().unwrap(), i);
    }

    pub fn iter<'a>(&'a self) -> std::vec::IntoIter<&'a T> {
        self.0.as_ref().unwrap().iter()
    }
}
use std::ops::*;
impl<T> Index<usize> for AVLMultiset<T> {
    type Output = T;

    fn index(&self, i: usize) -> &Self::Output {
        &Node::kth_node(self.0.as_ref().unwrap(), i).value
    }
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: usize = read();
    let m: usize = read();
    let a: Vec<_> = (0..n).map(|_| read::<usize>()).collect();
    let b: Vec<_> = (0..n).map(|_| read::<usize>()).collect();
    let c: Vec<_> = (0..m).map(|_| read::<usize>()).collect();
    let d: Vec<_> = (0..m).map(|_| read::<usize>()).collect();
    let mut a: Vec<_> = a.into_iter().zip(b.into_iter()).collect();
    let mut b: Vec<_> = c.into_iter().zip(d.into_iter()).collect();
    a.sort();
    b.sort();
    let mut j = 0;
    let mut s = AVLMultiset::new();
    for i in 0..m {
        let (x, y) = b[i];
        while j < n && a[j].0 <= x {
            s.insert(a[j].1);
            j += 1;
        }
        let k = s.upper_bound(&y);
        if k == 0 {
            continue;
        }
        let v = s[k - 1];
        s.remove(&v);
    }
    writeln!(writer, "{}", if s.size() > 0 || j < n { "No" } else { "Yes" })
        .unwrap();
}
