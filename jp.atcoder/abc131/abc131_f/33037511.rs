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
    let n: usize = read();
    const K: usize = 1 << 17;
    let mut g = vec![vec![]; 2 * K];
    for _ in 0..n {
        let x = read::<usize>() - 1;
        let y = read::<usize>() - 1 + K;
        g[x].push(y);
        g[y].push(x);
    }
    use connected_components_group_by_id::group_by_id;
    let comp = group_by_id(connected_components(&g));
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
pub fn connected_components(g: &[Vec<usize>]) -> Vec<usize> {
    let n = g.len();
    let mut ids = vec![n; n];
    let mut id = 0;
    let mut que = std::collections::VecDeque::new();
    for i in 0..n {
        if ids[i] != n {
            continue;
        }
        ids[i] = id;
        que.push_back(i);
        while let Some(u) = que.pop_front() {
            for &v in &g[u] {
                if ids[v] != n {
                    continue;
                }
                ids[v] = id;
                que.push_back(v);
            }
        }
        id += 1;
    }
    ids
}
