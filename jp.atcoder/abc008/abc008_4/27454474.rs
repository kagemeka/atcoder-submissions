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


    let w: usize = sc.scan();
    let h: usize = sc.scan();
    let n: usize = sc.scan();

    let mut points = Vec::with_capacity(n);
    for _ in 0..n {
        let x: usize = sc.scan();
        let y: usize = sc.scan();
        points.push(Point { x: x - 1, y: y - 1});
    }

    let mut cache = std::collections::HashMap::new();
    fn max_count(
        cache: &mut std::collections::HashMap<(usize, usize, usize, usize), usize>,
        points: &[Point],
        l: usize, r: usize, d: usize, u: usize,
    ) -> usize {
        let rect = (l, r, d, u);
        if cache.contains_key(&rect) { return *cache.get(&rect).unwrap(); }
        let mut mx = 0;
        for p in points.iter() {
            if p.x < l || r <= p.x || p.y < d || u <= p.y { continue; }
            let mut cnt = r - l + u - d - 1;
            cnt += max_count(cache, points, l, p.x, d, p.y);
            cnt += max_count(cache, points, l, p.x, p.y + 1, u);
            cnt += max_count(cache, points, p.x + 1, r, d, p.y);
            cnt += max_count(cache, points, p.x + 1, r, p.y + 1, u);
            mx = std::cmp::max(mx, cnt);
        }
        cache.insert(rect, mx);
        mx
    }
    writeln!(out, "{}", max_count(&mut cache, &points, 0, w, 0, h)).unwrap();
}

struct Point {
    x: usize,
    y: usize,
}
