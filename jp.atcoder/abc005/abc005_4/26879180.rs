pub fn scan<T: std::str::FromStr>() -> T {
    use std::io::Read;
    std::io::stdin().lock().bytes().map(|c|c.unwrap()as char)
    .skip_while(|c|c.is_whitespace())
    .take_while(|c|!c.is_whitespace())
    .collect::<String>().parse::<T>().ok().unwrap()
}


// #[allow(warnings)]
fn main() {
    use std::io::Write;
    let out = &mut std::io::BufWriter::new(std::io::stdout());

    let n: usize = scan();
    let mut d = vec![vec![0i32; n + 1]; n + 1];
    for i in 0..n {
        for j in 0..n {
            d[i + 1][j + 1] = scan();
        }
    }
    for i in 0..n {
        for j in 0..n + 1 {
            d[i + 1][j] += d[i][j];
        }
    }
    for j in 0..n {
        for i in 0..n + 1 {
            d[i][j + 1] += d[i][j];
        }
    }

    let mut res = vec![0i32; n * n + 1];
    for dy in 1..n + 1 {
        for dx in 1..n + 1 {
            let k = dy * dx;
            for y in 0..n - dy + 1{
                for x in 0..n - dx + 1 {
                    res[k] = std::cmp::max(
                        res[k],
                        d[y + dy][x + dx] - d[y + dy][x] - d[y][x + dx] + d[y][x],
                    );
                }
            }
        }
    }

    for i in 0..n * n {
        res[i + 1] = std::cmp::max(res[i + 1], res[i]);
    }
    let q: usize = scan();
    for _ in 0..q {
        let p: usize = scan();
        writeln!(out, "{}", res[p]).unwrap();
    }

}
