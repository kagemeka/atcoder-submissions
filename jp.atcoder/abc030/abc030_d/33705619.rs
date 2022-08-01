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
// class functional_graph_kth_from {
// public:
//   vector<int> path;
//   int cycle_size;
//   int cycle_start_idx;
//   functional_graph_kth_from(vector<int> const& f, int src) {
//     int n = f.size();
//     vector<int> order(n, -1);
//     for(int i = src, j = 0;; j++) {
//       if(order[i] != -1) {
//         cycle_size = j - order[i];
//         cycle_start_idx = order[i];
//         break;
//       }
//       order[i] = j;
//       path.push_back(i);
//       i = f[i];
//     }
//   }
//   auto operator()(long k) -> int const& {
//     if(k >= cycle_start_idx)
//       k = (k - cycle_start_idx) % cycle_size + cycle_start_idx;
//     return path[k];
//   }
// };
pub struct FunctionalGraphKthFrom {
    pub path: Vec<usize>,
    pub cycle_size: usize,
    pub cycle_start_idx: usize,
}
impl FunctionalGraphKthFrom {
    pub fn new(f: &[usize], src: usize) -> Self {
        let n = f.len();
        let mut path = vec![];
        let mut order = vec![n; n];
        let mut i = src;
        let mut j = 0;
        loop {
            if order[i] != n {
                return Self {
                    path,
                    cycle_size: j - order[i],
                    cycle_start_idx: order[i],
                };
            }
            order[i] = j;
            path.push(i);
            i = f[i];
            j += 1;
        }
    }

    pub fn get(&self, mut k: usize) -> usize {
        let s = self.cycle_start_idx;
        if k >= self.cycle_start_idx {
            k = (k - s) % self.cycle_size + s;
        }
        self.path[k]
    }
}
fn main() {
    use std::io::Write;
    let out = std::io::stdout();
    let writer = &mut std::io::BufWriter::new(out.lock());
    let n: usize = read();
    let a: usize = read::<usize>() - 1;
    let k: String = read();
    let f: Vec<_> = (0..n).map(|_| read::<usize>() - 1).collect();
    let res: usize;
    let f = FunctionalGraphKthFrom::new(&f, a);
    if k.len() < 10 {
        let k: usize = k.parse().unwrap();
        res = f.get(k);
    } else {
        let l = f.cycle_size as isize;
        let s = f.cycle_start_idx as isize;
        let mut i = -s;
        let mut p = 1isize;
        for c in k.chars().rev() {
            let d = c.to_string().parse::<isize>().unwrap();
            i += d * p;
            p *= 10;
            i %= l;
            p %= 10;
        }
        i = (i + l) % l;
        i += s;
        res = f.get(i as usize);
    }
    writeln!(writer, "{}", res + 1).unwrap();
}
