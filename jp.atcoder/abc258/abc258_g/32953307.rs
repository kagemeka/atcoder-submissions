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

pub mod bit_array {

    // pub const CHUNK_SIZE: usize = 64;
    // pub const MASK: usize = std::usize::MAX;

    const K: usize = 6;
    const M: usize = (1 << K) - 1;

    fn bucket(index: usize) -> usize { index >> K }
    fn point(index: usize) -> usize { index & M }
    fn value(index: usize) -> usize { 1 << point(index) }

    #[derive(Clone)]
    pub struct BitArray(Vec<usize>);

    impl BitArray {
        pub fn new(size: usize) -> Self { BitArray(vec![0; (size + M) >> K]) }

        pub fn set(&mut self, i: usize) { self.0[bucket(i)] |= value(i); }

        pub fn reset(&mut self, i: usize) { self.0[bucket(i)] &= !value(i); }

        pub fn flip(&mut self, i: usize) { self.0[bucket(i)] ^= value(i); }

        pub fn is_set(&self, i: usize) -> bool {
            self.0[bucket(i)] >> point(i) & 1 == 1
        }
    }

    impl From<&[bool]> for BitArray {
        fn from(is_set: &[bool]) -> Self {
            let mut a = BitArray::new(is_set.len());
            for (i, &ok) in is_set.iter().enumerate() {
                if ok {
                    a.set(i)
                }
            }
            a
        }
    }
    use std::ops::*;

    fn min_len(lhs: &BitArray, rhs: &BitArray) -> usize {
        lhs.0.len().min(rhs.0.len())
    }

    fn max_len(lhs: &BitArray, rhs: &BitArray) -> usize {
        lhs.0.len().max(rhs.0.len())
    }

    impl BitAnd for BitArray {
        type Output = Self;

        fn bitand(mut self, rhs: Self) -> Self::Output {
            for i in 0..min_len(&self, &rhs) {
                self.0[i] &= rhs.0[i];
            }
            self
        }
    }

    impl BitArray {
        pub fn popcount(&self) -> u64 {
            self.0.iter().map(|x| x.count_ones() as u64).sum()
        }
    }

    // TODO:
    // &, |,  <<, >>, ==
}

fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());

    let n: usize = read();
    use bit_array::*;
    let mut a: Vec<BitArray> = Vec::with_capacity(n);
    for _ in 0..n {
        let row = read::<String>()
            .as_bytes()
            .iter()
            .map(|&x| x == b'1')
            .collect::<Vec<_>>();
        a.push(row.as_slice().into());
    }

    let mut cnt = 0;
    for i in 0..n {
        for j in 0..i {
            if !a[i].is_set(j) {
                continue;
            }
            cnt += (a[i].clone() & a[j].clone()).popcount()
        }
    }
    writeln!(writer, "{}", cnt / 3).unwrap();
}
