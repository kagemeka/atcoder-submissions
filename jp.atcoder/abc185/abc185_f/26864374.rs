pub fn readline() -> String {
    let mut buf: String = String::new();
    std::io::stdin().read_line(&mut buf).unwrap();
    buf
}

pub fn read_int() -> i64 {
    readline().trim().parse::<i64>().unwrap()
}


#[derive(Default)]
pub struct Scanner {
    buffer: Vec<String>,
}

/// ```
/// let mut sc: Scanner = Scanner::default();
/// let a: i32 = sc.scan::<i32>();
/// ```
impl Scanner {
    pub fn scan<T>(&mut self) -> T
    where
        T: std::str::FromStr,
        T::Err: std::fmt::Debug,
    {
        loop {
            if let Some(token) = self.buffer.pop() {
                return token.parse::<T>().unwrap();
            }
            self.buffer =
                readline()
                .trim()
                .split_whitespace().rev()
                .map(String::from)
                .collect();
        }
    }

    pub fn i32(&mut self) -> i32 {
        self.scan::<i32>()
    }

    pub fn string(&mut self) -> String {
        self.scan::<String>()
    }
}


pub fn scan<T: std::str::FromStr>() -> T {
    use std::io::Read;
    std::io::stdin().bytes().map(|c|c.unwrap()as char)
    .skip_while(|c|c.is_whitespace())
    .take_while(|c|!c.is_whitespace())
    .collect::<String>().parse::<T>().ok().unwrap()
}


// use std::io::Write;
/// let out = &mut std::io::BufWriter::new(std::io::stdout());


/// Fn(&S, &S) -> S is a trait.
/// this is a dynamic size object at compilation time.
/// thus, it's needed to be enclosed with Box<dyn> pointer.
pub struct Monoid<S> {
    pub op: Box<dyn Fn(&S, &S) -> S>,
    pub e: Box<dyn Fn() -> S>,
    pub commutative: bool,
}


/// explicit lifetime for Monoid<S>.
/// S implements Copy trait for convenience.
pub struct FenwickTree<'a, S: Copy> {
    m: &'a Monoid<S>,
    data: Vec<S>,
}


impl<'a, S: std::fmt::Debug + Copy> std::fmt::Debug for FenwickTree<'a, S> {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        f.debug_tuple("FenwickTree").field(&self.data).finish()
    }
}

impl<'a, S: Copy> FenwickTree<'a, S> {

    pub fn new(m: &'a Monoid<S>, n: usize) -> Self {
        Self::from_vec(m, vec![(m.e)(); n])
    }

    pub fn from_vec(m: &'a Monoid<S>, a: Vec<S>) -> Self {
        let n = a.len();
        let mut data = vec![(m.e)(); n + 1];
        for i in 0..n { data[i + 1] = a[i]; }
        for i in 1..=n as i32 {
            let j = (i + (i & -i)) as usize;
            if j < n + 1 { data[j] = (m.op)(&data[j], &data[i as usize]); }
        }
        Self { m, data }
    }


    pub fn set(&mut self, mut i: usize, x: &S) {
        assert!(i < self.data.len() - 1);
        i += 1;
        while i < self.data.len() {
            self.data[i] = (self.m.op)(&self.data[i], x);
            i += (i as i32 & -(i as i32)) as usize;
        }
    }

    pub fn get(&self, mut i: usize) -> S {
        assert!(i < self.data.len());
        let mut v = (self.m.e)();
        while i > 0 {
            v = (self.m.op)(&v, &self.data[i]);
            i -= (i as i32 & -(i as i32)) as usize;
        }
        v
    }

    pub fn max_right(&self, is_ok: Box<dyn Fn(&S) -> bool>) -> usize {
        let n = self.data.len();
        let mut l = 1;
        while l << 1 < n { l <<= 1; }
        let mut v = (self.m.e)();
        let mut i = 0usize;
        while l > 0 {
            if i + l < n && is_ok(&(self.m.op)(&v, &self.data[i + l])) {
                i += l;
                v = (self.m.op)(&v, &self.data[i + 1]);
            }
            l >>= 1;
        }
        i
    }
}





#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_segment_tree() {
        let op = |x: &i32, y: &i32| { x + y };
        let e = || { 0 };
        let m = Monoid::<i32> { op: Box::new(op), e: Box::new(e), commutative: true};
        let mut a = vec![0i32; 10];
        for i in 0..10i32 { a[i as usize] = i; }
        let mut fw = FenwickTree::from_vec(&m, a);
        assert_eq!(fw.get(10), 45);
        assert_eq!(
            fw.data,
            vec![0, 0, 1, 2, 6, 4, 9, 6, 28, 8, 17],
        );
        println!("{:?}", fw);
        fw.set(4, &4);
        assert_eq!(fw.get(8) - fw.get(3), 29);
    }
}



use std::io::Write;
/// let out = &mut std::io::BufWriter::new(std::io::stdout());

// #[allow(warnings)]
fn main() {
    let op = |x: &u32, y: &u32| { x ^ y };
    let e = || { 0u32 };
    let m = Monoid::<u32> { op: Box::new(op), e: Box::new(e), commutative: true};
    let n: usize = scan();
    let q: usize = scan();
    let mut a = vec![0u32; n];
    for i in 0..n { a[i] = scan(); }
    let mut fw = FenwickTree::from_vec(&m, a);
    let out = &mut std::io::BufWriter::new(std::io::stdout());
    for _ in 0..q {
        let t: u8 = scan();
        let x: usize = scan::<usize>() - 1;
        let y: usize = scan();
        if t == 1 {
            let y = y as u32;
            fw.set(x, &y);
        } else {
            // println!("{}", fw.get(y) ^ fw.get(x));
            // out.write_fmt("{}", fw.get(y) ^ fw.get(x));
            writeln!(out, "{}", (fw.get(y) ^ fw.get(x))).unwrap();
        }
    }
}
