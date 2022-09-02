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
pub fn toposort(labels: Vec<usize>) -> Vec<usize> {
    let k = *labels.iter().max().unwrap();
    labels.into_iter().map(|l| k - l).collect()
}
pub fn scc(adjacency_list: &[Vec<usize>]) -> Vec<usize> {
    let g = adjacency_list;
    let n = g.len();
    let mut order = vec![n; n];
    let mut labels = vec![n; n];
    let mut ord = 0;
    let mut label = 0;
    let mut preorder = Vec::with_capacity(n);
    let mut low = Vec::with_capacity(n);
    let mut st_dfs: Vec<isize> = (0..n as isize).rev().collect();
    while let Some(u) = st_dfs.pop() {
        if u < 0 {
            let u = !u as usize;
            if low.last().unwrap() != &u {
                continue;
            }
            loop {
                let v = preorder.pop().unwrap();
                labels[v] = label;
                if v == u {
                    break;
                }
            }
            label += 1;
            low.pop();
            continue;
        }
        let u = u as usize;
        if order[u] != n {
            continue;
        }
        st_dfs.push(!(u as isize));
        order[u] = ord;
        ord += 1;
        preorder.push(u);
        low.push(u);
        for &v in g[u].iter() {
            if order[v] == n {
                st_dfs.push(v as isize);
            } else if labels[v] == n {
                while order[*low.last().unwrap()] > order[v] {
                    low.pop();
                }
            }
        }
    }
    toposort(labels)
}
pub struct TwoSat {
    g: Vec<Vec<usize>>,
    solution: Option<Vec<bool>>,
    updated: bool,
}
impl TwoSat {
    pub fn new(size: usize) -> Self {
        Self { g: vec![vec![]; size << 1], solution: None, updated: false }
    }

    fn n(&self) -> usize { self.g.len() >> 1 }

    /// add a clause (i-th node is f) or (j-th node is g)
    pub fn add_clause(&mut self, i: usize, f: bool, j: usize, g: bool) {
        let f = f as usize;
        let g = g as usize;
        self.g[i << 1 | f].push(j << 1 | (g ^ 1));
        self.g[j << 1 | g].push(i << 1 | (f ^ 1));
        // false: 2k
        // true: 2k + 1
        self.updated = false;
    }

    fn update(&mut self) {
        if self.updated {
            return;
        }
        self.updated = true;
        let id = scc(&self.g);
        let n = self.n();
        let mut res = vec![false; n];
        for i in 0..self.n() {
            let u = id[i << 1];
            let v = id[i << 1 | 1];
            if u == v {
                self.solution = None;
                return;
            }
            res[i] = u > v;
        }
        self.solution = Some(res)
    }

    pub fn is_satisfiable(&mut self) -> bool {
        self.update();
        self.solution.is_some()
    }

    pub fn solve(&mut self) -> Option<Vec<bool>> {
        self.update();
        self.solution.clone()
    }
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: usize = read();
    let d: i64 = read();
    let mut ts = TwoSat::new(n);
    let a: Vec<_> = (0..n).map(|_| (read::<i64>(), read::<i64>())).collect();
    for i in 0..n {
        for j in 0..i {
            if (a[i].0 - a[j].0).abs() < d {
                ts.add_clause(i, false, j, false);
            }
            if (a[i].0 - a[j].1).abs() < d {
                ts.add_clause(i, false, j, true);
            }
            if (a[i].1 - a[j].0).abs() < d {
                ts.add_clause(i, true, j, false);
            }
            if (a[i].1 - a[j].1).abs() < d {
                ts.add_clause(i, true, j, true);
            }
        }
    }
    let res = ts.solve();
    if res.is_none() {
        writeln!(writer, "No").unwrap();
        return;
    }
    let res = res.unwrap();
    writeln!(writer, "Yes").unwrap();
    for i in 0..n {
        writeln!(writer, "{}", if res[i] { a[i].0 } else { a[i].1 }).unwrap();
    }
}
