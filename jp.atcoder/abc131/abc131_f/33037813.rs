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
fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    use connected_components_group_by_id::group_by_id;
    let n: usize = read();
    const K: usize = 1 << 17;
    let mut edges = vec![];
    for _ in 0..n {
        let x = read::<usize>() - 1;
        let y = read::<usize>() - 1 + K;
        edges.push((x, y));
    }
    let comp = group_by_id(connected_components(2 * K, &edges));
    let mut tot = 0usize;
    for c in comp.into_iter() {
        let mut x = 0;
        let mut y = 0;
        for i in c.into_iter() {
            if i < K {
                x += 1;
            } else {
                y += 1;
            }
        }
        tot += x * y;
    }
    tot -= n;
    writeln!(writer, "{}", tot).unwrap();
}
use crate::{union_find::UnionFind, union_find_trait::*};
pub fn connected_components(
    v_size: usize, edges: &[(usize, usize)],
) -> Vec<usize> {
    let mut uf = UnionFind::new(v_size);
    for &(u, v) in edges {
        uf.unite(u, v);
    }
    uf.labels()
}
pub mod connected_components_group_by_id {
    pub fn group_by_id(ids: Vec<usize>) -> Vec<Vec<usize>> {
        let k = ids.iter().max().unwrap() + 1;
        let mut comp = vec![vec![]; k];
        for (u, id) in ids.into_iter().enumerate() {
            comp[id].push(u);
        }
        comp
    }
}
pub mod union_find {
    use crate::union_find_trait::*;
    #[derive(Debug)]
    pub struct UnionFind(Vec<isize>); // root: neg-size, other: parent
    impl UnionFind {
        pub fn new(size: usize) -> Self { Self(vec![-1; size]) }
    }
    impl Size for UnionFind {
        fn size(&self) -> usize { self.0.len() }
    }
    impl Root for UnionFind {
        fn root(&mut self, u: usize) -> usize {
            if self.0[u] < 0 {
                return u;
            }
            self.0[u] = self.root(self.0[u] as usize) as isize;
            self.0[u] as usize
        }
    }
    impl Unite for UnionFind {
        fn unite(&mut self, u: usize, v: usize) {
            let mut u = self.root(u);
            let mut v = self.root(v);
            if u == v {
                return;
            }
            if self.0[u] > self.0[v] {
                std::mem::swap(&mut u, &mut v);
            }
            self.0[u] += self.0[v];
            self.0[v] = u as isize;
        }
    }
    impl SizeOf for UnionFind {
        fn size_of(&mut self, u: usize) -> usize {
            let u = self.root(u);
            -self.0[u] as usize
        }
    }
}
pub mod union_find_trait {
    pub trait Root {
        fn root(&mut self, u: usize) -> usize;
    }
    #[allow(private_in_public)]
    pub trait Size {
        fn size(&self) -> usize;
    }
    pub trait Unite {
        fn unite(&mut self, u: usize, v: usize);
    }
    /// size of the component containing the node
    pub trait SizeOf {
        fn size_of(&mut self, u: usize) -> usize;
    }
    pub trait Same {
        fn same(&mut self, u: usize, v: usize) -> bool;
    }
    impl<U: Root> Same for U {
        fn same(&mut self, u: usize, v: usize) -> bool {
            self.root(u) == self.root(v)
        }
    }
    pub trait Labels {
        fn labels(&mut self) -> Vec<usize>;
    }
    impl<U: Root + Size> Labels for U {
        /// same label -> same component.
        fn labels(&mut self) -> Vec<usize> {
            let n = self.size();
            let mut lb = vec![n; n];
            let mut l = 0;
            for i in 0..n {
                let r = self.root(i);
                if lb[r] == n {
                    lb[r] = l;
                    l += 1;
                }
                lb[i] = lb[r];
            }
            lb
        }
    }
}
