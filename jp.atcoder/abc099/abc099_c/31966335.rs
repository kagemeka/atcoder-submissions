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

    const INF: u32 = 1 << 30;
    const K: usize = 1 << 20;
    let mut min_count = vec![INF; K];
    min_count[0] = 0;
    for i in 0..K {
        let mut j = 1;
        while i + j < K {
            min_count[i + j] = std::cmp::min(
                min_count[i + j],
                min_count[i] + 1,
            );
            j *= 6;
        }
        let mut j = 1;
        while i + j < K {
            min_count[i + j] = std::cmp::min(
                min_count[i + j],
                min_count[i] + 1,
            );
            j *= 9;
        }
    }

    let n: u32 = reader.read()?;
    writeln!(
        writer,
        "{}",
        min_count[n as usize]
    )?;

    writer.flush()?;
    Ok(())
}
