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

    let h: usize = sc.scan();
    let w: usize = sc.scan();

    let sy = sc.scan::<usize>() - 1;
    let sx = sc.scan::<usize>() - 1;
    let gy = sc.scan::<usize>() - 1;
    let gx = sc.scan::<usize>() - 1;

    let mut grid: Vec<Vec<char>> = vec![Vec::new(); h];
    for i in 0..h {
        grid[i] = sc.scan::<String>().chars().collect();
    }

    let n = h * w;
    let dyx = [(-1, 0), (0, -1), (1, 0), (0, 1)];
    let mut g: Vec<Vec<usize>> = vec![vec![]; n];
    for i in 1..h - 1 {
        for j in 1..w - 1 {
            if grid[i][j] == '#' { continue; }
            for (dy, dx) in dyx.iter() {
                let ni = (i as i32 + dy) as usize;
                let nj = (j as i32 + dx) as usize;
                if grid[ni][nj] == '#' { continue; }
                g[i * w + j].push(ni * w + nj);
            }
        }
    }
    let dist = bfs(&g, sy * w + sx)[gy * w + gx];
    writeln!(out, "{}", dist).unwrap();

}


pub fn bfs(g: &[Vec<usize>], src: usize) -> Vec<usize> {
    let n: usize = g.len();
    let inf = std::usize::MAX;
    let mut dist = vec![inf; n];
    dist[src] = 0;
    let mut que = std::collections::VecDeque::new();
    que.push_back(src);
    while let Some(u) = que.pop_front() {
        for &v in g[u].iter() {
            if dist[u] + 1 >= dist[v] { continue; }
            dist[v] = dist[u] + 1;
            que.push_back(v);
        }
    }
    dist
}
