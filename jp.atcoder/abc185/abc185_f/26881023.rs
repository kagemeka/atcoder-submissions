pub struct Scanner<R: std::io::Read> {
    reader: R,
}

impl<R: std::io::Read> Scanner<R> {
    /// let stdin = std::io::stdin();
    /// let mut sc = Scanner::new(stdin.lock());
    pub fn new(reader: R) -> Self { Self { reader: reader } }

    pub fn scan<T: std::str::FromStr>(&mut self) -> T {
        use std::io::Read;
        self.reader.by_ref().bytes().map(|c|c.unwrap()as char)
        .skip_while(|c|c.is_whitespace())
        .take_while(|c|!c.is_whitespace())
        .collect::<String>().parse::<T>().ok().unwrap()
    }
}



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
pub struct SegmentTree<'a, S: Copy> {
    m: &'a Monoid<S>,
    data: Vec<S>,
    size: usize,
}


impl<'a, S: std::fmt::Debug + Copy> std::fmt::Debug for SegmentTree<'a, S> {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        f.debug_tuple("SegmentTree").field(&self.data).finish()
    }
}

impl<'a, S: Copy> SegmentTree<'a, S> {

    pub fn new(m: &'a Monoid<S>, n: usize) -> Self {
        Self::from_vec(m, vec![(m.e)(); n])
    }

    pub fn from_vec(m: &'a Monoid<S>, a: Vec<S>) -> Self {
        let size = a.len();
        let n = size.next_power_of_two();
        let mut data = vec![(m.e)(); n << 1];
        for i in 0..size { data[n + i] = a[i]; }
        let mut seg = Self { m, data, size };
        for i in (0..n).rev() { seg.merge(i); }
        seg
    }

    fn merge(&mut self, i: usize) {
        self.data[i] = (self.m.op)(&self.data[i << 1], &self.data[i << 1 | 1]);
    }

    pub fn set(&mut self, mut i: usize, x: S) {
        assert!(i < self.size);
        i += self.data.len() >> 1;
        self.data[i] = x;
        while i > 1 { i >>= 1; self.merge(i); }
    }

    pub fn get(&self, mut l: usize, mut r: usize) -> S {
        assert!(l <= r && r <= self.size);
        let n = self.data.len() >> 1;
        l += n; r += n;
        let mut vl = (self.m.e)();
        let mut vr = (self.m.e)();
        while l < r {
            if l & 1 == 1 { vl = (self.m.op)(&vl, &self.data[l]); l += 1; }
            if r & 1 == 1 { r -= 1; vr = (self.m.op)(&self.data[r], &vr); }
            l >>= 1; r >>= 1;
        }
        (self.m.op)(&vl, &vr)
    }

    pub fn max_right(&self, is_ok: Box<dyn Fn(&S) -> bool>, l: usize) -> usize {
        assert!(l < self.size);
        let n = self.data.len() >> 1;
        let mut v = (self.m.e)();
        let mut i = (l + n) as i32;
        loop {
            i /= i & -i;
            if is_ok(&(self.m.op)(&v, &self.data[i as usize])) {
                v = (self.m.op)(&v, &self.data[i as usize]);
                i += 1;
                if i & -i == i { return self.size; }
                continue;
            }
            while i < n as i32 {
                i <<= 1;
                if is_ok(&(self.m.op)(&v, &self.data[i as usize])) {
                    v = (self.m.op)(&v, &self.data[i as usize]);
                }
            }
            return i as usize - n;
        }
    }
}


impl<'a, S: Copy> std::ops::Index<usize> for SegmentTree<'a, S> {
    type Output = S;

    fn index(&self, i: usize) -> &Self::Output {
        assert!(i < self.size);
        &self.data[i + (self.data.len() >> 1)]
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
        let mut seg = SegmentTree::from_vec(&m, a);
        assert_eq!(seg.get(0, 10), 45);
        assert_eq!(
            seg.data,
            [45, 45, 28, 17, 6, 22, 17, 0, 1, 5, 9, 13, 17, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0, 0, 0],
        );
        println!("{:?}", seg);
        seg.set(4, 8);
        assert_eq!(seg.get(3, 8), 29);
    }
}


// #[allow(warnings)]
fn main() {
    use std::io::Write;
    let stdin = std::io::stdin();
    let mut sc = Scanner::new(stdin.lock());
    let stdout = std::io::stdout();
    let out = &mut std::io::BufWriter::new(stdout.lock());

    let op = |x: &u32, y: &u32| { x ^ y };
    let e = || { 0u32 };
    let m = Monoid::<u32> { op: Box::new(op), e: Box::new(e), commutative: true};

    let n: usize = sc.scan();
    let q: usize = sc.scan();
    let mut a = vec![0u32; n];
    for i in 0..n { a[i] = sc.scan(); }
    let mut seg = SegmentTree::from_vec(&m, a);
    for _ in 0..q {
        let t: u8 = sc.scan();
        let x: usize = sc.scan::<usize>() - 1;
        let y: usize = sc.scan();
        if t == 1 {
            seg.set(x, seg[x] ^ y as u32);
        } else {
            writeln!(out, "{}", seg.get(x, y)).unwrap();
        }
    }
}
