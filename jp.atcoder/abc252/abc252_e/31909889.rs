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

#[derive(Debug, PartialEq)]
pub struct NegativeCycleError {
    msg: &'static str,
}

impl NegativeCycleError {
    pub fn new() -> Self { Self { msg: "Negative Cycle Found." } }
}

impl std::fmt::Display for NegativeCycleError {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        write!(f, "{}", self.msg)
    }
}

impl std::error::Error for NegativeCycleError {
    fn description(&self) -> &str { &self.msg }
}

pub trait Edge {}

pub trait UndirectedEdge {
    type V;
    fn u(&self) -> &Self::V;
    fn v(&self) -> &Self::V;
}

pub trait ToDirected {
    type E;
    fn to_directed(self) -> Self::E;
}

pub trait From {
    type V;
    fn from(&self) -> &Self::V;
}

pub trait To {
    type V;

    fn to(&self) -> &Self::V;
}

pub trait DirectedEdge: To {}

pub trait Reversed {
    fn reversed(self) -> Self;
}

pub trait Value {
    type T;
    fn value(&self) -> &Self::T;
}

pub trait Weight<T> {
    fn weight(&self) -> &T;
}

pub fn edges_to_directed<UE, DE>(undirected_edges: Vec<UE>) -> Vec<DE>
where
    UE: Clone + ToDirected<E = DE>,
    DE: Reversed,
{
    let di_edges = undirected_edges.into_iter().map(|e| e.to_directed());
    let rev = di_edges.clone().map(|e| e.reversed());
    di_edges.chain(rev).collect()
}

#[derive(Debug, Clone)]
pub struct AdjacencyList<E> {
    pub(crate) edges: Vec<Vec<E>>,
}

impl<E> AdjacencyList<E> {
    pub fn size(&self) -> usize { self.edges.len() }

    pub fn edges(&self) -> &[Vec<E>] { &self.edges }

    pub fn new(size: usize) -> Self {
        Self {
            edges: (0..size).map(|_| Vec::new()).collect(),
        }
    }

    pub fn add_node(&mut self) { self.edges.push(Vec::new()); }
}

impl<E> std::ops::Index<usize> for AdjacencyList<E> {
    type Output = Vec<E>;

    fn index(&self, i: usize) -> &Self::Output { &self.edges[i] }
}

impl<T> std::ops::IndexMut<usize> for AdjacencyList<T> {
    fn index_mut(&mut self, i: usize) -> &mut Self::Output {
        &mut self.edges[i]
    }
}

impl<E> std::convert::From<(usize, Vec<E>)> for AdjacencyList<E>
where
    E: From<V = usize>,
{
    fn from((size, edges): (usize, Vec<E>)) -> Self {
        let mut g = Self::new(size);
        for e in edges.into_iter() {
            g[*e.from()].push(e);
        }
        g
    }
}

impl<E> std::convert::Into<Vec<E>> for AdjacencyList<E>
where
    E: From<V = usize>,
{
    fn into(self) -> Vec<E> {
        self.edges
            .into_iter()
            .enumerate()
            .flat_map(|(u, edges)| {
                assert!(edges.iter().all(|e| e.from() == &u));
                edges
            })
            .collect()
    }
}

impl<T> ToDirected for (usize, usize, T) {
    type E = Self;

    fn to_directed(self) -> Self::E { self }
}

impl<T> Reversed for (usize, usize, T) {
    fn reversed(mut self) -> Self {
        std::mem::swap(&mut self.0, &mut self.1);
        self
    }
}

impl<T> From for (usize, usize, T) {
    type V = usize;

    fn from(&self) -> &Self::V { &self.0 }
}

impl<T> To for (usize, usize, T) {
    type V = usize;

    fn to(&self) -> &Self::V { &self.1 }
}

impl<T> Value for (usize, usize, T) {
    type T = T;

    fn value(&self) -> &Self::T { &self.2 }
}

impl<T: Weight<U>, U> Weight<U> for (usize, usize, T) {
    fn weight(&self) -> &U { self.2.weight() }
}

impl Weight<Self> for u64 {
    fn weight(&self) -> &Self { self }
}

impl Weight<Self> for i64 {
    fn weight(&self) -> &Self { self }
}

pub trait PriorityQueue {}

pub trait MinimumQueue {}
pub trait MaximumQueue {}

pub trait Push {
    type T;

    fn push(&mut self, x: Self::T);
}

pub trait Pop {
    type T;

    fn pop(&mut self) -> Option<Self::T>;
}

pub trait Top {
    type T;

    fn top(&mut self) -> &Self::T;
}

impl<T: std::cmp::Ord> Push
    for std::collections::BinaryHeap<std::cmp::Reverse<T>>
{
    type T = T;

    fn push(&mut self, x: Self::T) { Self::push(self, std::cmp::Reverse(x)); }
}

impl<T: std::cmp::Ord> Pop
    for std::collections::BinaryHeap<std::cmp::Reverse<T>>
{
    type T = T;

    fn pop(&mut self) -> Option<Self::T> {
        if let Some(std::cmp::Reverse(x)) = Self::pop(self) {
            Some(x)
        } else {
            None
        }
    }
}

impl<T: std::cmp::Ord> MinimumQueue
    for std::collections::BinaryHeap<std::cmp::Reverse<T>>
{
}

pub trait DijkstraSparseQueue:
    MinimumQueue + Push<T = (u64, usize)> + Pop<T = (u64, usize)> + Default
{
}

impl<Q> DijkstraSparseQueue for Q where
    Q: MinimumQueue + Push<T = (u64, usize)> + Pop<T = (u64, usize)> + Default
{
}

pub fn general_dijkstra_sparse<E, T, F, Q>(
    sparse_graph: &[Vec<E>],
    callback: &F,
    mut data: T,
    src: usize,
) -> (Vec<Option<u64>>, T)
where
    E: To<V = usize> + Weight<u64>,
    F: Fn(&Vec<Option<u64>>, &mut T, usize, &E),
    Q: DijkstraSparseQueue,
{
    let n = sparse_graph.len();
    let mut hq = Q::default();
    let mut dist = vec![None; n];
    dist[src] = Some(0);
    hq.push((0, src));
    while let Some((du, u)) = hq.pop() {
        if du > dist[u].unwrap() {
            continue;
        }
        for e in sparse_graph[u].iter() {
            callback(&dist, &mut data, u, e);
            let v = *e.to();
            let dv = du + e.weight();
            if dist[v].is_some() && dv >= dist[v].unwrap() {
                continue;
            }
            dist[v] = Some(dv);
            hq.push((dv, v));
        }
    }
    (dist, data)
}

pub fn dijkstra_sparse<E, Q>(
    sparse_graph: &[Vec<E>],
    src: usize,
) -> Vec<Option<u64>>
where
    E: To<V = usize> + Weight<u64>,
    Q: DijkstraSparseQueue,
{
    general_dijkstra_sparse::<_, _, _, Q>(
        sparse_graph,
        &|_, _, _, _| {},
        (),
        src,
    )
    .0
}

#[allow(dead_code)]
pub type DijkstraQueueBinaryHeapStd =
    std::collections::BinaryHeap<std::cmp::Reverse<(u64, usize)>>;

pub fn spfa<E>(
    sparse_graph: &[Vec<E>],
    src: usize,
) -> Result<Vec<Option<i64>>, NegativeCycleError>
where
    E: To<V = usize> + Weight<i64>,
{
    let n = sparse_graph.len();
    let mut dist = vec![None; n];
    dist[src] = Some(0);
    let mut que = vec![src];
    let mut in_que = vec![false; n];
    in_que[src] = true;
    for _ in 0..n {
        let mut next_que = vec![];
        for u in que.into_iter() {
            in_que[u] = false;
            for e in &sparse_graph[u] {
                let v = *e.to();
                let dv = Some(dist[u].unwrap() + e.weight());
                if dist[v].is_some() && dv >= dist[v] {
                    continue;
                }
                dist[v] = dv;
                if !in_que[v] {
                    next_que.push(v);
                    in_que[v] = true;
                }
            }
        }
        que = next_que;
        if que.is_empty() {
            return Ok(dist);
        }
    }
    Err(NegativeCycleError::new())
}

pub trait ShortestPathPotentialEdge:
    From<V = usize>
    + To<V = usize>
    + Weight<i64>
    + std::convert::From<(usize, usize, i64)>
{
}

impl<T> ShortestPathPotentialEdge for T where
    T: From<V = usize>
        + To<V = usize>
        + Weight<i64>
        + std::convert::From<(usize, usize, i64)>
{
}

/// used to map edge weights from integer to non-negative integer space.
/// mainly spawned as preprocessing
/// before calling Dijkstra's algorithm multiple times
/// on a graph which might be containing negative weighted edges.
pub fn shortest_path_potential<E>(
    v_size: usize,
    mut directed_edges: Vec<E>,
) -> Result<Vec<i64>, NegativeCycleError>
where
    E: ShortestPathPotentialEdge,
{
    directed_edges.extend((0..v_size).map(|i| (v_size, i, 0).into()));
    let g = AdjacencyList::<E>::from((v_size + 1, directed_edges));
    match spfa(g.edges(), v_size) {
        Ok(mut potential) => {
            potential.pop();
            Ok(potential.into_iter().map(|x| x.unwrap()).collect())
        },
        Err(e) => Err(e),
    }
}

pub fn johnson_sparse<E, Q>(
    v_size: usize,
    directed_edges: Vec<E>,
) -> Result<Vec<Vec<Option<i64>>>, NegativeCycleError>
where
    E: ShortestPathPotentialEdge + Clone,
    Q: DijkstraSparseQueue,
{
    let p = shortest_path_potential::<E>(v_size, directed_edges.clone())?;
    type E2 = (usize, usize, u64);
    let edges = directed_edges
        .into_iter()
        .map(|e| {
            let u = *e.from();
            let v = *e.to();
            let w: u64 = (e.weight() - p[v] + p[u]) as u64;
            (u, v, w)
        })
        .collect::<Vec<E2>>();
    let g = AdjacencyList::<E2>::from((v_size, edges));
    let mut results = vec![];
    for i in 0..v_size {
        let dist = dijkstra_sparse::<E2, Q>(g.edges(), i)
            .into_iter()
            .enumerate()
            .map(|(j, d)| d.map(|x| x as i64 + p[j] - p[i]))
            .collect();
        results.push(dist);
    }
    Ok(results)
}

pub fn dijkstra_dense(
    dense_graph: &[Vec<Option<u64>>],
    src: usize,
) -> Vec<Option<u64>> {
    let g = dense_graph;
    let n = g.len();
    let mut dist = vec![None; n];
    dist[src] = Some(0);
    let mut visited = vec![false; n];
    loop {
        let mut u = None;
        let mut du = None;
        for i in 0..n {
            if visited[i] || dist[i].is_none() {
                continue;
            }
            if du.is_none() || dist[i] < du {
                u = Some(i);
                du = dist[i];
            }
        }
        if u.is_none() {
            break;
        }
        let u = u.unwrap();
        let du = du.unwrap();
        visited[u] = true;
        for v in 0..n {
            if g[u][v].is_none() {
                continue;
            }
            let dv = Some(du + g[u][v].unwrap());
            if dist[v].is_none() || dv < dist[v] {
                dist[v] = dv;
            }
        }
    }
    dist
}

pub fn johnson_dense(
    dense_graph: &[Vec<Option<i64>>],
) -> Result<Vec<Vec<Option<i64>>>, NegativeCycleError> {
    let n = dense_graph.len();
    let mut edges = vec![];
    for i in 0..n {
        for j in 0..n {
            if let Some(w) = dense_graph[i][j] {
                edges.push((i, j, w));
            }
        }
    }
    let p = shortest_path_potential(n, edges)?;
    let g = dense_graph
        .into_iter()
        .enumerate()
        .map(|(i, row)| {
            row.into_iter()
                .enumerate()
                .map(|(j, &d)| {
                    if d.is_some() {
                        Some((d.unwrap() - p[j] + p[i]) as u64)
                    } else {
                        None
                    }
                })
                .collect::<Vec<_>>()
        })
        .collect::<Vec<_>>();
    let mut results = vec![];
    for i in 0..n {
        let dist = dijkstra_dense(&g, i)
            .into_iter()
            .enumerate()
            .map(|(j, d)| d.map(|x| x as i64 + p[j] - p[i]))
            .collect();
        results.push(dist);
    }
    Ok(results)
}

pub fn dijkstra_sparse_predecessors<E, Q>(
    sparse_graph: &[Vec<E>],
    src: usize,
) -> Vec<Vec<usize>>
where
    E: To<V = usize> + Weight<u64>,
    Q: DijkstraSparseQueue,
{
    let mut predecessors = vec![vec![]; sparse_graph.len()];
    predecessors = general_dijkstra_sparse::<_, _, _, Q>(
        sparse_graph,
        &|dist, pre: &mut Vec<Vec<usize>>, u, e: &E| {
            let v = *e.to();
            let dv = dist[u].unwrap() + e.weight();
            if let Some(prev_dv) = dist[v] {
                if dv < prev_dv {
                    pre[v] = vec![u];
                } else if dv == prev_dv {
                    pre[v].push(u);
                }
            } else {
                pre[v] = vec![u];
            }
        },
        predecessors,
        src,
    )
    .1;
    predecessors[src] = vec![];
    predecessors
}

// pub fn dijkstra_sparse_parent<E, Q>(
//     sparse_graph: &[Vec<E>],
//     src: usize,
// ) -> Vec<Option<usize>>
// where
//     E: To<V = usize> + Weight<u64>,
//     Q: DijkstraSparseQueue,
// {
//     let n = sparse_graph.len();
//     let predecessors =
//         dijkstra_sparse_predecessors::<E, Q>(sparse_graph, src);
//     let mut parent = vec![None; n];
//     for v in 0..n {
//         for u in predecessors[v].iter() {
//             if parent[v] == Some(u) {
//                 continue;
//             }

//         }
//     }
//     parent

// }

#[derive(Debug, PartialEq)]
pub struct DisconnectedError {
    msg: &'static str,
}

impl DisconnectedError {
    pub fn new() -> Self {
        Self {
            msg: "given graph is not connected.",
        }
    }
}

impl std::fmt::Display for DisconnectedError {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        write!(f, "{}", self.msg)
    }
}

impl std::error::Error for DisconnectedError {
    fn description(&self) -> &str { &self.msg }
}

// pub fn dijkstra_sparse_arborescense<E, Q>(
//     v_size: usize,
//     directed_edges: &[E],
//     root: usize,
// ) -> Vec<usize>
// where
//     E: From<V = usize> + To<V = usize> + Weight<u64> + Clone,
//     Q: DijkstraSparseQueue,
// {
//     let g = AdjacencyList::from((v_size, directed_edges.to_vec()));
//     let pre = dijkstra_sparse_predecessors::<E, Q>(g.edges(), root);
//     directed_edges
//         .iter()
//         .enumerate()
//         .filter_map(|(i, e)| {
//             let u = *e.from();
//             let v = *e.to();
//             if !pre[v].is_empty() && pre[v][0] == u {
//                 Some(i)
//             } else {
//                 None
//             }
//         })
//         .collect()
// }

// pub fn dijkstra_sparse_tree<E, Q>(
//     undirected_connected_edges: &[E],
//     sparse_graph: &[Vec<E>],
//     src: usize,
// ) -> ()
// // contained edges.
// where
//     E: To<V = usize> + Weight<u64>,
//     Q: DijkstraSparseQueue,
// {
// }

// #[allow(warnings)]
fn main() -> Result<(), Box<dyn std::error::Error>> {
    use std::io::Write;
    let mut reader = locked_stdin_reader();
    let mut writer = locked_stdin_buf_writer();

    let n = reader.read::<usize>()?;
    let m = reader.read::<usize>()?;

    let mut edges = (0..m)
        .map(|_| {
            (
                reader.read::<usize>().unwrap() - 1,
                reader.read::<usize>().unwrap() - 1,
                reader.read::<u64>().unwrap(),
            )
        })
        .collect::<Vec<_>>();

    edges = edges_to_directed(edges);
    let g = AdjacencyList::from((n, edges.clone()));

    type Q = DijkstraQueueBinaryHeapStd;
    let dist = dijkstra_sparse::<_, Q>(g.edges(), 0);

    let mut is_child = vec![false; n];
    let mut res = vec![];
    for (i, &(mut u, mut v, w)) in edges.iter().enumerate() {
        if dist[u] > dist[v] {
            std::mem::swap(&mut u, &mut v);
        }
        if is_child[v] || dist[u].unwrap() + w > dist[v].unwrap() {
            continue;
        }
        is_child[v] = true;
        res.push(i);
    }
    assert_eq!(res.len(), n - 1);
    for i in 0..n - 1 {
        write!(
            writer,
            "{}{}",
            res[i] + 1,
            if i < n - 2 { " " } else { "\n" }
        )?;
    }

    writer.flush()?;
    Ok(())
}
