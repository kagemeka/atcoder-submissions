
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
    let mut c = vec![0usize; n];
    for i in 0..n { c[i] = sc.scan::<usize>() - 1; }

    let mut g: Vec<(usize, usize)> = Vec::with_capacity(n - 1);
    for _ in 0..n - 1 {
        let a: usize = sc.scan();
        let b: usize = sc.scan();
        g.push((a - 1, b - 1));
    }
    let (tour, _, _) = euler_tour_edge(&g, 0);
    let mut cnt = vec![0usize; 1 << 20];

    let mut res = Vec::new();
    for &u in tour.iter() {
        if u < 0 {
            cnt[c[!u as usize]] -= 1;
            continue;
        }
        if cnt[c[u as usize]] == 0 {
            res.push(u as usize + 1);
        }
        cnt[c[u as usize]] += 1;
    }
    res.sort();
    for x in res.iter() {
        writeln!(out, "{}", x).unwrap();
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
