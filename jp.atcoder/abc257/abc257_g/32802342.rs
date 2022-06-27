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

pub mod morris_pratt_table_0_indexed {
    pub fn morris_pratt_table<T: PartialEq>(a: &[T]) -> Vec<usize> {
        let n = a.len();
        let mut lb = vec![0; n];
        let mut d = 0;
        for i in 1..n {
            while d != 0 && a[d] != a[i] {
                d = lb[d - 1];
            }
            if a[d] == a[i] {
                d += 1;
            }
            lb[i] = d;
        }
        lb
    }
}

fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());

    let mut s = read::<String>().chars().collect::<Vec<_>>();
    let mut t = read::<String>().chars().collect::<Vec<_>>();
    let n = s.len();
    let m = t.len();
    s.push('$');
    s.append(&mut t);
    use morris_pratt_table_0_indexed::*;
    let lb = &morris_pratt_table(&s)[n + 1..];
    let mut i = m;
    let mut k = 0;
    while i > 0 {
        let d = lb[i - 1];
        if d == 0 {
            writeln!(writer, "-1").unwrap();
            return;
        }
        i -= d;
        k += 1;
    }
    writeln!(writer, "{}", k).unwrap();
}
