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
    let mut k: usize = sc.scan();
    let mut s: Vec<char> = sc.scan::<String>().chars().collect();

    let mut swap_cost = vec![1; n];
    for i in 0..n {
        let mut hq = std::collections::BinaryHeap::new();
        for j in i + 1..n {
            if s[j] >= s[i] { continue; }
            let cost = swap_cost[i] + swap_cost[j];
            if cost > k { continue; }
            hq.push((std::cmp::Reverse(s[j]), std::cmp::Reverse(cost), j));
        }
        if let Some((_, std::cmp::Reverse(cost), j)) = hq.pop() {
            k -= cost;
            s.swap(i, j);
            swap_cost[i] = 0;
            swap_cost[j] = 0;
        }
    }
    writeln!(out, "{}", s.iter().collect::<String>()).unwrap();
}
