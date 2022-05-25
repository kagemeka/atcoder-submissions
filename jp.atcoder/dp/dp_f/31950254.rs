pub struct ReadWrapper<R> {
    reader: R,
    tokens: Vec<String>,
}

impl<R> ReadWrapper<R> {
    pub fn new(reader: R) -> Self { Self { reader, tokens: vec![] } }
}

impl<R: std::io::BufRead> ReadWrapper<R> {
    pub fn read<T: std::str::FromStr>(
        &mut self,
    ) -> Result<T, <T as std::str::FromStr>::Err> {
        while self.tokens.is_empty() {
            let mut buf = String::new();
            self.reader.read_line(&mut buf).unwrap();
            self.tokens =
                buf.split_whitespace().map(str::to_string).rev().collect();
        }
        self.tokens.pop().unwrap().parse::<T>()
    }
}

pub fn locked_stdin_reader() -> ReadWrapper<std::io::StdinLock<'static>> {
    let stdin = Box::leak(Box::new(std::io::stdin()));
    ReadWrapper::new(stdin.lock())
}

pub fn locked_stdin_buf_writer()
-> std::io::BufWriter<std::io::StdoutLock<'static>> {
    let stdout = Box::leak(Box::new(std::io::stdout()));
    std::io::BufWriter::new(stdout.lock())
}

// #[allow(warnings)]
fn main() -> Result<(), Box<dyn std::error::Error>> {
    use std::io::Write;
    let mut reader = locked_stdin_reader();
    let mut writer = locked_stdin_buf_writer();

    let s: String = reader.read()?;
    let t: String = reader.read()?;
    let lcs = struct_lcs(
        &s.chars().collect::<Vec<_>>(),
        &t.chars().collect::<Vec<_>>(),
    );
    // writeln!(writer, "{:?}", lcs.len())?;
    writeln!(writer, "{}", lcs.iter().collect::<String>())?;

    writer.flush()?;
    Ok(())
}

pub fn lcs_dp<T: PartialEq>(a: &[T], b: &[T]) -> Vec<Vec<usize>> {
    let n = a.len();
    let m = b.len();
    let mut length = vec![vec![0; m + 1]; n + 1];
    for i in 0..n {
        for j in 0..m {
            if a[i] == b[j] {
                length[i + 1][j + 1] = length[i][j] + 1;
                continue;
            }
            length[i + 1][j + 1] = std::cmp::max(
                length[i][j + 1],
                length[i + 1][j],
            );
        }
    }
    length
}

pub fn struct_lcs<T: PartialEq + Clone>(a: &[T], b: &[T]) -> Vec<T> {
    let n = a.len();
    let m = b.len();
    let length = lcs_dp(a, b);
    let mut lcs = Vec::with_capacity(length[n][m]);

    let mut i = n;
    let mut j = m;
    while i > 0 && j > 0 {
        let l = length[i][j];
        if length[i][j - 1] == l {
            j -= 1;
            continue;
        }
        if length[i - 1][j] == l {
            i -= 1;
            continue;
        }
        i -= 1;
        j -= 1;
        lcs.push(a[i].clone());
    }
    lcs.reverse();
    lcs
}
