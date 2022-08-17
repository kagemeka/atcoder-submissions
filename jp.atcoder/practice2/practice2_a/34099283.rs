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
pub struct UnionFind(Vec<isize>);
impl UnionFind {
    pub fn new(size: usize) -> Self { Self(vec![-1; size]) }

    pub fn size(&self) -> usize { self.0.len() }

    pub fn root(&mut self, u: usize) -> usize {
        return if self.0[u] < 0 {
            u
        } else {
            self.0[u] = self.root(self.0[u] as usize) as isize;
            self.0[u] as usize
        };
    }

    pub fn unite(&mut self, mut u: usize, mut v: usize) {
        u = self.root(u);
        v = self.root(v);
        if u == v {
            return;
        }
        if self.0[u] > self.0[v] {
            std::mem::swap(&mut u, &mut v);
        }
        self.0[u] += self.0[v];
        self.0[v] = u as isize;
    }

    pub fn size_of(&mut self, mut u: usize) -> usize {
        u = self.root(u);
        -self.0[u] as usize
    }

    pub fn same(&mut self, u: usize, v: usize) -> bool {
        self.root(u) == self.root(v)
    }

    pub fn labels(&mut self) -> Vec<usize> {
        let n = self.size();
        let mut labels = vec![n; n];
        let mut l = 0;
        for i in 0..n {
            let r = self.root(i);
            if labels[r] == n {
                labels[r] = l;
                l += 1;
            }
            labels[i] = labels[r];
        }
        labels
    }
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: usize = read();
    let q: usize = read();
    let mut uf = UnionFind::new(n);
    for _ in 0..q {
        let t: usize = read();
        let u: usize = read();
        let v: usize = read();
        if t == 0 {
            uf.unite(u, v);
        } else {
            writeln!(writer, "{}", if uf.same(u, v) { 1 } else { 0 }).unwrap();
        }
    }
}
