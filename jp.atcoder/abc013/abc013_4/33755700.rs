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
pub struct KthFrom {
    cycles: Vec<Vec<usize>>,
    cycle_id: Vec<usize>,
    idx_in_cycle: Vec<usize>,
}
impl KthFrom {
    pub fn new(f: &[usize]) -> Self {
        let mut cycles = vec![];
        let n = f.len();
        let mut cycle_id = vec![n; n];
        let mut idx_in_cycle = vec![n; n];
        for mut i in 0..n {
            if cycle_id[i] != n {
                continue;
            }
            let id = cycles.len();
            let mut cycle = vec![];
            for j in 0..n {
                if cycle_id[i] != n {
                    break;
                }
                cycle_id[i] = id;
                idx_in_cycle[i] = j;
                cycle.push(i);
                i = f[i];
            }
            cycles.push(cycle);
        }
        Self { cycles, cycle_id, idx_in_cycle }
    }

    pub fn get(&self, i: usize, k: usize) -> usize {
        let cycle = &self.cycles[self.cycle_id[i]];
        cycle[(k + self.idx_in_cycle[i]) % cycle.len()]
    }
}
pub fn solve_ghost_leg(n: usize, edges: &[usize]) -> Vec<usize> {
    let mut res = (0..n).collect::<Vec<_>>();
    for &i in edges.iter().rev() {
        res.swap(i, i + 1);
    }
    res
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: usize = read();
    let m: usize = read();
    let k: usize = read();
    let b: Vec<_> = (0..m).map(|_| read::<usize>() - 1).collect();
    let a = solve_ghost_leg(n, &b);
    let f = KthFrom::new(&a);
    for i in 0..n {
        writeln!(writer, "{}", f.get(i, k) + 1).unwrap();
    }
}
