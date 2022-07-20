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
pub fn bfs_grid(
    inf: u32, is_path: &[Vec<bool>], sy: usize, sx: usize,
) -> Vec<Vec<u32>> {
    let h = is_path.len();
    let w = is_path[0].len();
    let mut dist = vec![vec![inf; w]; h];
    dist[sy][sx] = 0;
    let mut que = std::collections::VecDeque::new();
    que.push_back((sy, sx));
    let on_path = |y, x| {
        if !(0 <= y && y < h as isize && 0 <= x && x < w as isize) {
            return false;
        }
        is_path[y as usize][x as usize]
    };
    let dyx = [(-1, 0), (0, -1), (1, 0), (0, 1)];
    while let Some((y, x)) = que.pop_front() {
        let d = dist[y][x] + 1;
        for &(dy, dx) in dyx.iter() {
            let ny = y as isize + dy;
            let nx = x as isize + dx;
            if !on_path(ny, nx) {
                continue;
            }
            let ny = ny as usize;
            let nx = nx as usize;
            if dist[ny][nx] != inf {
                continue;
            }
            dist[ny][nx] = d;
            que.push_back((ny, nx));
        }
    }
    dist
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
    let mut is_path = vec![vec![false; w]; h];
    for i in 0..h {
        for j in 0..w {
            is_path[i][j] = grid[i][j] == '.';
        }
    }
    let res = bfs_grid(1 << 30, &is_path, sy, sx);
    writeln!(writer, "{}", res[gy][gx]).unwrap();
}
