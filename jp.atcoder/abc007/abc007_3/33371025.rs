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
pub fn a_star<F>(
    inf: i64, g: &[Vec<(usize, i64)>], src: usize, dst: usize,
    heuristic_func: F,
) -> i64
where
    F: Fn(usize) -> i64,
{
    use std::cmp::Reverse;
    let n = g.len();
    let mut cost = vec![inf; n];
    cost[src] = 0;
    let mut que = std::collections::BinaryHeap::new();
    // (smaller score, larger cost (or smaller heuristic value), node)
    que.push((Reverse(heuristic_func(src)), 0, src));
    while let Some((Reverse(_), cu, u)) = que.pop() {
        if u == dst {
            return cu;
        }
        if cu > cost[u] {
            continue;
        }
        for &(v, w) in g[u].iter() {
            let cv = cu + w;
            if cv >= cost[v] {
                continue;
            }
            cost[v] = cv;
            let sv = heuristic_func(v) + cv;
            que.push((Reverse(sv), cv, v));
        }
    }
    inf
}
fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let h: usize = read();
    let w: usize = read();
    let sy = read::<usize>() - 1;
    let sx = read::<usize>() - 1;
    let gy = read::<usize>() - 1;
    let gx = read::<usize>() - 1;
    let grid = (0..h)
        .map(|_| read::<String>().chars().collect::<Vec<_>>())
        .collect::<Vec<_>>();
    let n = h * w;
    let mut g = vec![vec![]; n];
    let dyx = [(-1, 0), (0, -1), (1, 0), (0, 1)];
    let is_path = |y, x| {
        if !(0 <= y && y < h as isize && 0 <= x && x < w as isize) {
            return false;
        }
        grid[y as usize][x as usize] == '.'
    };
    for i in 0..h {
        for j in 0..w {
            let u = i * w + j;
            for &(dy, dx) in dyx.iter() {
                let ny = i as isize + dy;
                let nx = j as isize + dx;
                if !is_path(ny, nx) {
                    continue;
                }
                let v = ny as usize * w + nx as usize;
                g[u].push((v, 1));
            }
        }
    }
    let hf = |u: usize| {
        let y = u / w;
        let x = u % w;
        (y as i64 - gy as i64).abs() + (x as i64 - gx as i64).abs()
    };
    const INF: i64 = 1 << 30;
    let src = sy * w + sx;
    let dst = gy * w + gx;
    let res = a_star(INF, &g, src, dst, &hf);
    writeln!(writer, "{}", res).unwrap();
}
