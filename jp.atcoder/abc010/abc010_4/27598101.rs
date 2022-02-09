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
    let k: usize = sc.scan();
    let m: usize = sc.scan();
    let mut g: Vec<Vec<(usize, u64)>> = vec![vec![]; n + 1];
    for _ in 0..k {
        let p: usize = sc.scan();
        g[p].push((n, 1));
    }
    for _ in 0..m {
        let a: usize = sc.scan();
        let b: usize = sc.scan();
        g[a].push((b, 1));
        g[b].push((a, 1));
    }
    // let f = dinic(&g, 0, n);
    // let f = ford_fulkerson(&g, 0, n);
    let f = edmonds_karp(&g, 0, n);
    writeln!(out, "{}", f).unwrap();
}



/// O(V^2E)
pub fn dinic(g: &Vec<Vec<(usize, u64)>>, src: usize, sink: usize) -> u64 {
    let n = g.len();
    let mut rf = vec![vec![0; n]; n];
    for u in 0..n {
        for &(v, f) in g[u].iter() { rf[u][v] += f; }
    }
    let mut g: Vec<Vec<usize>> = vec![vec![]; n];
    for u in 0..n {
        for v in 0..n { if rf[u][v] > 0 { g[u].push(v); }; }
    }
    let update_level = |g: &Vec<Vec<usize>>| {
        let mut level = vec![n; n];
        level[src] = 0;
        let mut que = std::collections::VecDeque::new();
        que.push_back(src);
        while let Some(u) = que.pop_front() {
            for &v in g[u].iter() {
                if level[v] != n { continue; }
                level[v] = level[u] + 1;
                que.push_back(v);
            }
        }
        level
    };

    fn flow_to_sink(
        sink: usize,
        rf: &mut Vec<Vec<u64>>,
        g: &mut Vec<Vec<usize>>,
        level: &Vec<usize>,
        u: usize,
        mut flow_in: u64,
    ) -> u64 {
        if u == sink { return flow_in; }
        let mut flow_out = 0;
        let edges = g[u].clone();
        g[u].clear();
        for &v in edges.iter() {
            if level[v] <= level[u] { g[u].push(v); continue; }
            let f = flow_to_sink(sink, rf, g, level, v, std::cmp::min(flow_in, rf[u][v]));
            rf[u][v] -= f;
            if rf[u][v] > 0 { g[u].push(v); }
            if rf[v][u] == 0 && f > 0 { g[v].push(u); }
            rf[v][u] += f;
            flow_in -= f;
            flow_out += f;
        }
        flow_out
    }


    let mut flow = 0;
    loop {
        let level = update_level(&g);
        if level[sink] == n { break; }
        flow += flow_to_sink(sink, &mut rf, &mut g, &level, src, std::u64::MAX);
    }
    flow
}


/// O(V^2 + VE^2)
pub fn edmonds_karp(g: &Vec<Vec<(usize, u64)>>, src: usize, sink: usize) -> u64 {
    let n = g.len();
    let mut rf = vec![vec![0; n]; n];
    for u in 0..n {
        for &(v, f) in g[u].iter() { rf[u][v] += f; }
    }
    let mut g: Vec<Vec<usize>> = vec![vec![]; n];
    for u in 0..n {
        for v in 0..n { if rf[u][v] > 0 { g[u].push(v); }; }
    }

    fn find_path(rf: &Vec<Vec<u64>>, g: &mut Vec<Vec<usize>>, src: usize, sink: usize) -> Vec<usize> {
        let n = g.len();
        let mut parent = vec![n; n];
        parent[src] = src;
        let mut que = std::collections::VecDeque::new();
        que.push_back(src);
        while let Some(u) = que.pop_front() {
            g[u].retain(|&v| rf[u][v] != 0);
            for &v in g[u].iter() {
                if parent[v] != n { continue; }
                parent[v] = u;
                que.push_back(v);
            }
        }
        let mut v = sink;
        let mut path = vec![v];
        while parent[v] != n && parent[v] != v {
            v = parent[v];
            path.push(v);
        }
        path
    }

    fn augment_flow(rf: &mut Vec<Vec<u64>>, g: &mut Vec<Vec<usize>>, path: &Vec<usize>) -> u64 {
        let mut flow = std::u64::MAX;
        for i in 0..path.len() - 1 {
            flow = std::cmp::min(flow, rf[path[i + 1]][path[i]]);
        }
        for i in 0..path.len() - 1 {
            let u = path[i + 1];
            let v = path[i];
            rf[u][v] -= flow;
            if rf[v][u] == 0 { g[v].push(u); }
            rf[v][u] += flow;
        }
        flow
    }

    let mut flow = 0;
    loop {
        let path = find_path(&rf, &mut g, src, sink);
        if path.len() == 1 { break; }
        let f = augment_flow(&mut rf, &mut g, &path);
        flow += f;
    }
    flow
}


/// O(V^2 + Ef)
pub fn ford_fulkerson(g: &Vec<Vec<(usize, u64)>>, src: usize, sink: usize) -> u64 {
    let n = g.len();
    let mut rf = vec![vec![0; n]; n];
    for u in 0..n {
        for &(v, f) in g[u].iter() { rf[u][v] += f; }
    }
    let mut g: Vec<Vec<usize>> = vec![vec![]; n];
    for u in 0..n {
        for v in 0..n { if rf[u][v] > 0 { g[u].push(v); }; }
    }

    fn augment_flow(
        sink: usize,
        rf: &mut Vec<Vec<u64>>,
        g: &mut Vec<Vec<usize>>,
        visited: &mut Vec<bool>,
        u: usize,
        flow_in: u64,
    ) -> u64 {
        visited[u] = true;
        if u == sink { return flow_in; }
        let edges = g[u].clone();
        g[u].clear();
        let mut flow = 0;
        for &v in edges.iter() {
            if visited[v] || flow > 0 { g[u].push(v); continue; }
            flow = augment_flow(sink, rf, g, visited, v, std::cmp::min(flow_in, rf[u][v]));
            rf[u][v] -= flow;
            if rf[u][v] > 0 { g[u].push(v); }
            if flow == 0 { continue; }
            if rf[v][u] == 0 { g[v].push(u); }
            rf[v][u] += flow;
        }
        flow
    }

    // let mut visited = vec![false; n];
    let mut flow = 0;
    loop {
        // visited.fill(false);
        let mut visited = vec![false; n];
        let f = augment_flow(sink, &mut rf, &mut g, &mut visited, src, std::u64::MAX);
        if f == 0 { break; }
        flow += f;
    }
    flow
}
