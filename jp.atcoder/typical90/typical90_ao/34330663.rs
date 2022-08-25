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
pub fn polygon_area_x2(a: &[(i64, i64)]) -> i64 {
    let mut s = 0;
    let n = a.len();
    for i in 0..n {
        let j = (i + 1) % n;
        s += (a[i].0 - a[j].0) * (a[i].1 + a[j].1);
    }
    s.abs()
}
pub fn convex_hull(points: &[(i64, i64)]) -> Vec<(i64, i64)> {
    let mut a = points.to_vec();
    a.sort_unstable();
    let is_ccw = |p0: &(i64, i64), p1: &(i64, i64), p2: &(i64, i64)| -> bool {
        let (x0, y0) = p0;
        let (x1, y1) = p1;
        let (x2, y2) = p2;
        (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0) >= 0
    };
    let mut h = Vec::new();
    // upper hull
    for p in a.iter() {
        let mut k = h.len();
        while k >= 2 && is_ccw(&h[k - 2], &h[k - 1], p) {
            h.pop();
            k -= 1;
        }
        h.push(*p);
    }
    // lower hull
    let m = h.len();
    for p in a.iter().rev().skip(1) {
        let mut k = h.len();
        while k > m && is_ccw(&h[k - 2], &h[k - 1], p) {
            h.pop();
            k -= 1;
        }
        h.push(*p);
    }
    h.pop();
    h
}
pub fn gcd(a: i64, b: i64) -> i64 {
    if b == 0 { a.abs() } else { gcd(b, a % b) }
}
pub fn segment_lattice_points(x0: i64, y0: i64, x1: i64, y1: i64) -> i64 {
    gcd(x1 - x0, y1 - y0) + 1
}
pub fn polygon_lattice_points(a: &[(i64, i64)]) -> i64 {
    let n = a.len();
    let s2 = polygon_area_x2(&a);
    let mut b = 0;
    for i in 0..n {
        let j = (i + 1) % n;
        b += segment_lattice_points(a[i].0, a[i].1, a[j].0, a[j].1) - 1;
    }
    let i = (s2 + 2 - b) / 2;
    i + b
}
pub fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: usize = read();
    let mut a: Vec<_> =
        (0..n).map(|_| (read::<i64>(), read::<i64>())).collect();
    a = convex_hull(&a);
    writeln!(writer, "{}", polygon_lattice_points(&a) - n as i64).unwrap();
}
