use std::ops::Add;

pub struct Scanner<R: std::io::Read> {
    reader: R,
}

impl<R: std::io::Read> Scanner<R> {
    /// let stdin = std::io::stdin();
    /// let mut sc = Scanner::new(stdin.lock());
    pub fn new(reader: R) -> Self { Self { reader: reader } }

    pub fn scan<T: std::str::FromStr>(&mut self) -> T {
        use std::io::Read;
        self.reader.by_ref().bytes().map(|c| c.unwrap() as char)
        .skip_while(|c| c.is_whitespace())
        .take_while(|c| !c.is_whitespace())
        .collect::<String>().parse::<T>().ok().unwrap()
    }
}



// #[allow(warnings)]
fn main() {
    use std::io::Write;
    let stdin = std::io::stdin();
    let mut sc = Scanner::new(std::io::BufReader::new(stdin.lock()));
    let stdout = std::io::stdout();
    let out = &mut std::io::BufWriter::new(stdout.lock());

    let n: usize = sc.scan();
    let mut g: Vec<(usize, usize)> = Vec::with_capacity(n - 1);
    for _ in 0..n - 1 {
        g.push((sc.scan::<usize>() - 1, sc.scan::<usize>() - 1));
    }
    let q: usize = sc.scan();
    let mut ab: Vec<(usize, usize)> = Vec::with_capacity(q);
    for _ in 0..q {
        ab.push((sc.scan::<usize>() - 1, sc.scan::<usize>() - 1));
    }
    // let lca = BinaryLifting::new(&g, 0);
    let lca = eulertour_rmq::WithSegmentTree::new(&g, 0);
    let (_, _, depth) = euler_tour_edge(&g, 0);
    for &(a, b) in ab.iter() {
        writeln!(out, "{}", depth[a] + depth[b] - 2 * depth[lca.get(a, b)] + 1).unwrap();
    }
}



/// explicit lifetime for Monoid<S>.
/// S implements Copy trait for convenience.
pub struct SegmentTree<'a, S: Copy> {
    m: Monoid<'a, S>,
    data: Vec<S>,
    size: usize,
}


impl<'a, S: std::fmt::Debug + Copy> std::fmt::Debug for SegmentTree<'a, S> {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        f.debug_tuple("SegmentTree").field(&self.data).finish()
    }
}

impl<'a, S: Copy> SegmentTree<'a, S> {

    pub fn new(m: Monoid<'a, S>, n: usize) -> Self {
        let a = vec![(m.e)(); n];
        Self::from_vec(m, &a)
    }

    pub fn from_vec(m: Monoid<'a, S>, a: &Vec<S>) -> Self {
        let size = a.len();
        let n = size.next_power_of_two();
        let mut data = vec![(m.e)(); n << 1];
        for i in 0..size { data[n + i] = a[i]; }
        let mut seg = Self { m, data, size };
        for i in (0..n).rev() { seg.merge(i); }
        seg
    }

    fn merge(&mut self, i: usize) {
        self.data[i] = (self.m.op)(&self.data[i << 1], &self.data[i << 1 | 1]);
    }

    pub fn set(&mut self, mut i: usize, x: S) {
        assert!(i < self.size);
        i += self.data.len() >> 1;
        self.data[i] = x;
        while i > 1 { i >>= 1; self.merge(i); }
    }

    pub fn get(&self, mut l: usize, mut r: usize) -> S {
        assert!(l <= r && r <= self.size);
        let n = self.data.len() >> 1;
        l += n; r += n;
        let mut vl = (self.m.e)();
        let mut vr = (self.m.e)();
        while l < r {
            if l & 1 == 1 { vl = (self.m.op)(&vl, &self.data[l]); l += 1; }
            if r & 1 == 1 { r -= 1; vr = (self.m.op)(&self.data[r], &vr); }
            l >>= 1; r >>= 1;
        }
        (self.m.op)(&vl, &vr)
    }

    pub fn max_right(&self, is_ok: Box<dyn Fn(&S) -> bool>, l: usize) -> usize {
        assert!(l < self.size);
        let n = self.data.len() >> 1;
        let mut v = (self.m.e)();
        let mut i = (l + n) as i32;
        loop {
            i /= i & -i;
            if is_ok(&(self.m.op)(&v, &self.data[i as usize])) {
                v = (self.m.op)(&v, &self.data[i as usize]);
                i += 1;
                if i & -i == i { return self.size; }
                continue;
            }
            while i < n as i32 {
                i <<= 1;
                if is_ok(&(self.m.op)(&v, &self.data[i as usize])) {
                    v = (self.m.op)(&v, &self.data[i as usize]);
                }
            }
            return i as usize - n;
        }
    }
}


impl<'a, S: Copy> std::ops::Index<usize> for SegmentTree<'a, S> {
    type Output = S;

    fn index(&self, i: usize) -> &Self::Output {
        assert!(i < self.size);
        &self.data[i + (self.data.len() >> 1)]
    }
}

/// references
/// - https://codeforces.com/blog/entry/18369
/// - https://en.wikipedia.org/wiki/Euler_tour_technique
/// - https://cp-algorithms.com/graph/euler_path.html
/// - https://maspypy.com/euler-tour-%E3%81%AE%E3%81%8A%E5%8B%89%E5%BC%B7
pub fn euler_tour_edge(g: &Vec<(usize, usize)>, root: usize) -> (Vec<isize>, Vec<usize>, Vec<usize>) {
    let n = g.len() + 1;
    let mut t = vec![vec![]; n];
    for &(u, v) in g.iter() {
        t[u].push(v);
        t[v].push(u);
    }
    let mut parent = vec![n; n];
    let mut depth = vec![0; n];
    let mut tour = Vec::with_capacity(n << 1);
    let mut st = vec![root as isize];
    for _ in 0..n << 1 {
        let u = st.pop().unwrap();
        tour.push(u);
        if u < 0 { continue; }
        st.push(!u);
        let u = u as usize;
        for &v in t[u].iter() {
            if v == parent[u] { continue; }
            parent[v] = u;
            depth[v] = depth[u] + 1;
            st.push(v as isize);
        }
    }
    (tour, parent, depth)
}


pub fn euler_tour_node(g: &Vec<(usize, usize)>, root: usize) -> (Vec<isize>, Vec<usize>, Vec<usize>, Vec<usize>, Vec<usize>) {
    let (mut tour, parent, depth) = euler_tour_edge(g, root);
    let n = tour.len() >> 1;
    tour.pop();
    let mut first_idx = vec![n; n];
    let mut last_idx = vec![n; n];
    for i in 0..tour.len() {
        let mut u = tour[i];
        if u < 0 {
            u = parent[!u as usize] as isize;
            tour[i] = u;
        } else {
            first_idx[u as usize] = i;
        }
        last_idx[u as usize] = i;
    }
    (tour, first_idx, last_idx, parent, depth)
}




pub mod structs {
    /// Fn(&S, &S) -> S is a trait.
    /// this is a dynamic size object at compilation time.
    /// thus, it's needed to be enclosed with Box<dyn> pointer.
    pub struct Monoid<'a, S> {
        pub op: &'a dyn Fn(&S, &S) -> S,
        pub e: &'a dyn Fn() -> S,
        pub commutative: bool,
        pub idempotent: bool,
    }

    pub struct Semigroup<'a, S> {
        pub op: &'a dyn Fn(&S, &S) -> S,
        pub commutative: bool,
        pub idempotent: bool,
    }
}

use structs::*;





/// Sparse Table
/// references
/// - https://cp-algorithms.com/data_structures/sparse-table.html
pub struct SparseTable<'a, S> {
    sg: Semigroup<'a, S>,
    data: Vec<Vec<S>>,
}


impl<'a, S: Default + Clone> SparseTable<'a, S> {
    /// O(N\log{N})
    pub fn new(sg: Semigroup<'a, S>, a: &Vec<S>) -> Self {
        assert!(sg.idempotent && sg.commutative);
        let n = a.len();
        assert!(n > 0);
        let k = std::cmp::max(1, bit_length(n - 1));
        let mut data = vec![vec![S::default(); n]; k];
        data[0] = a.clone();
        for i in 0..k - 1 {
            data[i + 1] = data[i].clone();
            for j in 0..n - (1 << i) {
                data[i + 1][j] = (sg.op)(&data[i][j], &data[i][j + (1 << i)])
            }
        }
        Self { sg: sg, data: data }
    }

    /// O(1)
    pub fn get(&self, l: usize, r: usize) -> S {
        assert!(l < r && r <= self.data[0].len());
        let k = bit_length(r - l) - 1;
        (self.sg.op)(&self.data[k][l], &self.data[k][r - (1 << k)])
    }
}




/// Disjoint Sparse Table
/// references
/// - https://noshi91.hatenablog.com/entry/2018/05/08/183946
/// - https://github.com/noshi91/NoshiMochiLibrary/blob/master/SparseTable/DisjointSparseTable.noshi.cpp
pub struct DisjointSparseTable<'a, S> {
    sg: Semigroup<'a, S>,
    data: Vec<Vec<S>>,
}


impl<'a, S: Default + Clone> DisjointSparseTable<'a, S> {
    pub fn new(sg: Semigroup<'a, S>, a: &Vec<S>) -> Self {
        let n = a.len();
        assert!(n > 0);
        let k = std::cmp::max(1, bit_length(n - 1));
        let mut data = vec![vec![S::default(); n]; k];
        data[0] = a.clone();
        for i in 1..k {
            data[i] = a.clone();
            for j in (1 << i..n + 1).step_by(2 << i) {
                for k in 1..(1 << i) {
                    data[i][j - k - 1] = (sg.op)(&data[i][j - k - 1], &data[i][j - k]);
                }
                for k in 0..(1 << i) - 1 {
                    if j + k + 1 >= n { break; }
                    data[i][j + k + 1] = (sg.op)(&data[i][j + k], &data[i][j + k + 1]);
                }
            }
        }
        Self { sg: sg, data: data }
    }

    pub fn get(&self, l: usize, r: usize) -> S {
        assert!(l < r && r <= self.data[0].len());
        if r - l == 1 { return self.data[0][l].clone(); }
        let k = bit_length(l ^ r) - 1;
        (self.sg.op)(&self.data[k][l], &self.data[k][r - 1])
    }
}




pub fn bit_length(n: usize) -> usize {
    (0usize.leading_zeros() - n.leading_zeros()) as usize
}


pub fn tree_bfs(g: &Vec<(usize, usize)>, root: usize) -> (Vec<usize>, Vec<usize>) {
    let n = g.len() + 1;
    let mut t = vec![vec![]; n];
    for &(u, v) in g.iter() {
        t[u].push(v);
        t[v].push(u);
    }
    let mut parent = vec![n; n];
    let mut depth = vec![0; n];
    let mut que = std::collections::VecDeque::new();
    que.push_back(root);
    while let Some(u) = que.pop_front() {
        for &v in t[u].iter() {
            if v == parent[u] { continue; }
            parent[v] = u;
            depth[v] = depth[u] + 1;
            que.push_back(v);
        }
    }
    (parent, depth)
}


pub struct UnionFind {
    data: Vec<i32>,
}


impl UnionFind {
    pub fn new(n: usize) -> Self {
        Self { data: vec![-1; n] }
    }

    pub fn find(&mut self, u: usize) -> usize {
        if self.data[u] < 0 { return u; }
        self.data[u] = self.find(self.data[u] as usize) as i32;
        self.data[u] as usize
    }

    pub fn unite(&mut self, u: usize, v: usize) {
        let (mut u, mut v) = (self.find(u), self.find(v));
        if u == v { return; }
        if self.data[u] > self.data[v] { std::mem::swap(&mut u, &mut v); }
        self.data[u] += self.data[v];
        self.data[v] = u as i32;
    }

    pub fn size(&mut self, u: usize) -> usize {
        let u = self.find(u);
        -self.data[u] as usize
    }
}


/// Lowest Common Ancestor with Tarjan's offline algorithm.
/// O(V + Q) preprocessing, O(1) per query.
/// references
/// - https://cp-algorithms.com/graph/lca_tarjan.html
/// - https://en.wikipedia.org/wiki/Tarjan%27s_off-line_lowest_common_ancestors_algorithm
/// - https://tjkendev.github.io/procon-library/python/graph/lca-tarjan.html
pub fn tarjan_offline(g: &Vec<(usize, usize)>, uv: &Vec<(usize, usize)>, root: usize) -> Vec<usize> {
    fn dfs(
        g: &Vec<Vec<usize>>,
        q: &Vec<Vec<(usize, usize)>>,
        visited: &mut Vec<bool>,
        uf: &mut UnionFind,
        ancestor: &mut Vec<usize>,
        lca: &mut Vec<usize>,
        u: usize,
    ) {
        visited[u] = true;
        ancestor[u] = u;
        for &v in g[u].iter() {
            if visited[v] { continue; }
            dfs(g, q, visited, uf, ancestor, lca, v);
            uf.unite(u, v);
            ancestor[uf.find(u)] = u;
        }
        for &(v, i) in q[u].iter() {
            if visited[v] { lca[i] = ancestor[uf.find(v)]; }
        }
    }
    let n = g.len() + 1;
    let mut t = vec![vec![]; n];
    for &(u, v) in g.iter() {
        t[u].push(v);
        t[v].push(u);
    }
    let mut q = vec![vec![]; n];
    for (i, &(u, v)) in uv.iter().enumerate() {
        q[u].push((v, i));
        q[v].push((u, i));
    }
    let mut visited = vec![false; n];
    let mut uf = UnionFind::new(n);
    let mut ancestor = vec![n; n];
    let mut lca = vec![n; uv.len()];
    dfs(&t, &q, &mut visited, &mut uf, &mut ancestor, &mut lca, root);
    lca
}



/// Lowest Common Ancestor with Binary Lifting.
/// references
/// - https://cp-algorithms.com/graph/lca_binary_lifting.html
pub struct BinaryLifting {
    ancestor: Vec<Vec<usize>>,
    depth: Vec<usize>,
}


impl BinaryLifting {
    /// O(N\log{N})
    pub fn new(g: &Vec<(usize, usize)>, root: usize) -> Self {
        let n = g.len() + 1;
        let (parent, depth) = tree_bfs(g, root);
        let k = std::cmp::max(1, bit_length(*depth.iter().max().unwrap()));
        let mut ancestor = vec![vec![n; n]; k];
        ancestor[0] = parent;
        ancestor[0][root] = root;
        for i in 0..k - 1 {
            for j in 0..n {
                ancestor[i + 1][j] = ancestor[i][ancestor[i][j]];
            }
        }
        Self { ancestor: ancestor, depth: depth }
    }

    /// O(\log{N})
    pub fn get(&self, mut u: usize, mut v: usize) -> usize {
        if self.depth[u] > self.depth[v] { std::mem::swap(&mut u, &mut v); }
        let d = self.depth[v] - self.depth[u];
        for i in 0..bit_length(d) {
            if d >> i & 1 == 1 { v = self.ancestor[i][v]; }
        }
        if v == u { return u; }
        for a in self.ancestor.iter().rev() {
            let nu = a[u];
            let nv = a[v];
            if nu != nv { u = nu; v = nv;}
        }
        self.ancestor[0][u]
    }
}


pub fn with_hl_decomposition() {}


pub mod eulertour_rmq {

    use super::{SparseTable, DisjointSparseTable, euler_tour_node, Semigroup};
    use super::{SegmentTree, Monoid};


    pub struct WithSparseTable<'a, S> {
        first_idx: Vec<usize>,
        sp: DisjointSparseTable<'a, S>,
    }
    impl<'a> WithSparseTable<'a, (usize, usize)> {
        pub fn new(g: &Vec<(usize, usize)>, root: usize) -> Self {
            let (tour, first_idx, _, _, depth) = euler_tour_node(g, root);
            let sg = Semigroup::<'a, (usize, usize)> {
                op: &|x, y| std::cmp::min(*x, *y),
                commutative: true,
                idempotent: true,
            };
            let mut a = Vec::with_capacity(tour.len());
            for &i in tour.iter() {
                a.push((depth[i as usize], i as usize));
            }
            let sp = DisjointSparseTable::new(sg, &a);
            Self { first_idx: first_idx, sp: sp }
        }

        pub fn get(&self, u: usize, v: usize) -> usize {
            let mut l = self.first_idx[u];
            let mut r = self.first_idx[v];
            if l > r { std::mem::swap(&mut l, &mut r); }
            self.sp.get(l, r + 1).1
        }
    }


    pub struct WithSegmentTree<'a, S: Copy> {
        first_idx: Vec<usize>,
        seg: SegmentTree<'a, S>,
    }
    impl<'a> WithSegmentTree<'a, (usize, usize)> {
        pub fn new(g: &Vec<(usize, usize)>, root: usize) -> Self {
            let (tour, first_idx, _, _, depth) = euler_tour_node(g, root);
            let m = Monoid::<'a, (usize, usize)> {
                op: &|x, y| std::cmp::min(*x, *y),
                e: &|| (std::usize::MAX, 0),
                commutative: true,
                idempotent: false,
            };
            let mut a = Vec::with_capacity(tour.len());
            for &i in tour.iter() {
                a.push((depth[i as usize], i as usize));
            }
            let seg = SegmentTree::from_vec(m, &a);
            Self { first_idx: first_idx, seg: seg }
        }

        pub fn get(&self, u: usize, v: usize) -> usize {
            let mut l = self.first_idx[u];
            let mut r = self.first_idx[v];
            if l > r { std::mem::swap(&mut l, &mut r); }
            self.seg.get(l, r + 1).1
        }
    }


    pub struct WithSqrtDecomposition {}

}

/// references
/// - https://ei1333.hateblo.jp/entry/2018/05/29/011140
/// - https://www.slideshare.net/iwiwi/2-12188845
pub struct WithHLD {}
