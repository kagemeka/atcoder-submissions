package main

import (
	"fmt"
	"bufio"
	"os"
	"sort"
	"strconv"
	"strings"
	"unicode"
	"math"
	"container/heap"
	"container/list"
	"math/bits"
	// "reflect"
)

const (
	// Mod .
	Mod = int(1e9 + 7)
	// Eps .
	Eps = 1e-13

	// Inf (int)
	Inf = 1001001001001
)


type contest map[string]func()
type proconSite struct {contests map[string]contest; problems map[string]func()}


// RuneSlice .
type RuneSlice []rune
func (p RuneSlice) Len() int { return len(p) }
func (p RuneSlice) Less(i, j int) bool { return p[i] < p[j] }
func (p RuneSlice) Swap(i, j int) {p[i], p[j] = p[j], p[i]}

// ByteSlice .
type ByteSlice []byte
func (p ByteSlice) Len() int { return len(p) }
func (p ByteSlice) Less(i, j int) bool { return p[i] < p[j] }
func (p ByteSlice) Swap(i, j int) {p[i], p[j] = p[j], p[i]}

// PairInt .
type PairInt struct{ x, y int }
// Pair .
type Pair struct {first, second interface{}}

// ReversedString . (caution: string + string is too slow)
func ReversedString(s string) string {
	l := len(s); t := make([]byte, l)
	for i := 0; i < l; i++ {t[l-1-i] = s[i]}
	return string(t)
}

// SumInt .
func SumInt(a ...int) (s int) {for _, v := range a {s += v}; return}
// AbsInt .
func AbsInt(x int) int {if x < 0 {x *= -1}; return x}
// AbsFloat .
func AbsFloat(x float64) float64 {return math.Abs(x)}
// MaxInt .
func MaxInt(a ...int) int {m := a[0]; for _, x := range a {if x > m {m = x}}; return m}
// MinInt .
func MinInt(a ...int) int {m := a[0]; for _, x := range a {if x < m {m = x}}; return m}
// Min .
func Min(a ...interface{}) interface{} {
	n := len(a); if n == 0 {return nil}
	switch a[0].(type) {
	case int:
		b := make([]int, n); for i := 0; i < n; i++ {b[i] = a[i].(int)}
		m := b[0]; for _, x := range b {if x < m {m = x}}; return m
	case byte:
		b := make([]byte, n); for i := 0; i < n; i++ {b[i] = a[i].(byte)}
		m := b[0]; for _, x := range b {if x < m {m = x}}; return m
	case rune:
		b := make([]rune, n); for i := 0; i < n; i++ {b[i] = a[i].(rune)}
		m := b[0]; for _, x := range b {if x < m {m = x}}; return m
	case string:
		b := make([]string, n); for i := 0; i < n; i++ {b[i] = a[i].(string)}
		m := b[0]; for _, x := range b {if x < m {m = x}}; return m
	case float64:
		b := make([]float64, n); for i := 0; i < n; i++ {b[i] = a[i].(float64)}
		m := b[0]; for _, x := range b {if x < m {m = x}}; return m
	default:
		return nil
	}
}
// Max .
func Max(a ...interface{}) interface{} {
	n := len(a); if n == 0 {return nil}
	switch a[0].(type) {
	case int:
		b := make([]int, n); for i := 0; i < n; i++ {b[i] = a[i].(int)}
		m := b[0]; for _, x := range b {if x > m {m = x}}; return m
	case byte:
		b := make([]byte, n); for i := 0; i < n; i++ {b[i] = a[i].(byte)}
		m := b[0]; for _, x := range b {if x > m {m = x}}; return m
	case rune:
		b := make([]rune, n); for i := 0; i < n; i++ {b[i] = a[i].(rune)}
		m := b[0]; for _, x := range b {if x > m {m = x}}; return m
	case string:
		b := make([]string, n); for i := 0; i < n; i++ {b[i] = a[i].(string)}
		m := b[0]; for _, x := range b {if x > m {m = x}}; return m
	case float64:
		b := make([]float64, n); for i := 0; i < n; i++ {b[i] = a[i].(float64)}
		m := b[0]; for _, x := range b {if x > m {m = x}}; return m
	default:
		return nil
	}
}
// Divmod .
func Divmod(a, b int) (int, int) {return a/b, a%b}
// Gcd .
func Gcd(a, b int) int {if (b == 0) {return AbsInt(a)}; return Gcd(b, a%b)}
// Lcm .
func Lcm(a, b int) int {return AbsInt(a/Gcd(a, b)*b)}
// BisectLeft .
func BisectLeft(a []int, x int) int { return sort.SearchInts(a, x) }
// BisectRight .
func BisectRight(a []int, x int) int {return sort.Search(len(a), func(i int) bool {return a[i] > x})}
// Booltoi .
func Booltoi(b bool) int { if b {return 1}; return 0}
// BitsLen .
func BitsLen(x int) int {return bits.Len(uint(x))}
// BitsCount .
func BitsCount(x int) int {return bits.OnesCount(uint(x))}
// BitwiseNot .
func BitwiseNot(x int) int {return x ^ (1<<63-1)}
// SubStr . don't use many times on a string.
func SubStr(s string, l, r int) string {return string([]rune(s)[l:r])}
// FindDivisors .
func FindDivisors(n int) (res []int) {for i := 1; i*i <= n; i++ {if n%i == 0 {res = append(res, i); if n/i != i {res = append(res, n/i)}}}; sort.Ints(res); return}
// NthRoot (Newton's method)
func NthRoot(y, n float64) (x float64) {x = 1; for i := 0; i < 100; i++ { x -= (math.Pow(x, n)-y)/(n*math.Pow(x, n-1))}; return}

// SortedStr .
func SortedStr(s string) string { t := RuneSlice([]rune(s)); sort.Sort(t); return string(t)}
// Pow .
func Pow(x, n int, args ...int) int {
  // x, n := args[0], args[1]
	y := 1
	mod := 1001001001001001; if len(args)==1 {mod = args[0]}
  for n>0 { if n&1 == 1 {y = y*x%mod}; n >>= 1; x = x*x%mod}
  return y
}


// LIS .
func LIS(a []int) []int {
	res := make([]int, len(a))
	for i := 0; i < len(res); i++ {res[i] = Inf}
	for _, x := range a {res[BisectLeft(res, x)] = x}
	return res
}





// Identity .
func Identity(n int) [][]int {
	a := make([][]int, n)
	for i := 0; i < n; i++ {a[i] = make([]int, n); a[i][i] = 1}
	return a
}

// Dot .
func Dot(a, b [][]int) [][]int {
	h, w, l := len(a), len(b[0]), len(b)
	c := make([][]int, len(a))
	for i := 0; i < h; i++ {c[i] = make([]int, w)}
	for i := 0; i < h; i++ {
		for j := 0; j < w; j++ {
			for k := 0; k < l; k++ {
				c[i][j] += a[i][k]*b[k][j]
			}
		}
	}
	return c

}
// MatrixPow .
func MatrixPow(a [][]int, n int, args ...int) [][]int {
	m := len(a)
	mod := Mod; if len(args)!=0 {mod = args[0]}
	b := Identity(m)
	for n>0 {
		if n&1 == 1 {b = Dot(b, a)}
		n >>= 1; a = Dot(a, a)
		for i := 0; i < m; i++ {
			for j := 0; j < m; j++ {
				a[i][j] %= mod; b[i][j] %= mod
			}
		}
	}
	return b
}

// BitwiseDot .
func BitwiseDot(a, b [][]int) [][]int {
	h, w, l := len(a), len(b[0]), len(b)
	c := make([][]int, h)
	for i := 0; i < h; i++ {c[i] = make([]int, w)}
	for i := 0; i < h; i++ {
		for j := 0; j < w; j++ {
			for k := 0; k < l; k++ {
				c[i][j] ^= a[i][k]&b[k][j]
			}
		}
	}
	return c

}
// BitwiseMatPow .
func BitwiseMatPow(a [][]int, n int) [][]int {
	m := len(a)
	b := Identity(m); for i := 0; i < m; i++ {b[i][i] = Inf}
	for n>0 {
		if n&1 == 1 {b = BitwiseDot(b, a)}
		n >>= 1; a = BitwiseDot(a, a)
	}
	return b
}



// NumberTheory .
type NumberTheory struct {
	IsPrime []bool
	PrimeNumbers[]int

	mod int
	Fac []int
	IFac []int
}

// GenerateFacIFacTables .
func (nt *NumberTheory) GenerateFacIFacTables(n int) {
	p := nt.mod
	fac, ifac := make([]int, n+1), make([]int, n+1)
	fac[0] = 1; for i := 0; i < n; i++ {fac[i+1] = fac[i]*(i+1)%p}
	ifac[n] = Pow(fac[n],p-2,p); for i := n; i > 0; i-- {ifac[i-1] = ifac[i]*i%p}
	nt.Fac, nt.IFac = fac, ifac
}

// GeneratePrimeNumbers (NumberTheory) .
func (nt *NumberTheory) GeneratePrimeNumbers(n int) {nt.IsPrime, nt.PrimeNumbers = SieveOfEratosthenes(n)}

// SieveOfEratosthenes .
func SieveOfEratosthenes(n int) (isPrime []bool, primeNumbers []int) {
  sieve := make([]bool, n+1); for i := 2; i < n+1; i++ {sieve[i] = true}
  for i := 2; i*i <= n; i++ {if sieve[i] {for j := i*2; j < n+1; j += i {sieve[j] = false}}}
  isPrime = sieve
  for i := 0; i < n+1; i++ {if isPrime[i] {primeNumbers = append(primeNumbers, i)}}
  return isPrime, primeNumbers
}

// PrimeFactorize .
func (nt *NumberTheory) PrimeFactorize(n int) map[int]int {
	res := make(map[int]int)
  m := int(math.Sqrt(float64(n)))
  for _, p := range nt.PrimeNumbers {
    if p > m {break}
    for n%p == 0 {n /= p; res[p]++}
    if n == 1 {return res}
  }
  res[n] = 1; return res
}
// PrimeFactorizeFactorial .
func (nt *NumberTheory) PrimeFactorizeFactorial(n int) map[int]int {res := make(map[int]int); for i := 1; i < n+1; i++ {for p, c := range nt.PrimeFactorize(i) {res[p] += c}}; return res}


// Combinatorics .
type Combinatorics struct{
	fac, ifac []int
	nCr map[[2]int]int
	mod int
}

// Init .
func (cn *Combinatorics) Init(n, mod int) {
	cn.nCr = make(map[[2]int]int)
	cn.mod = mod
	nt := NumberTheory{mod: mod}
	nt.GenerateFacIFacTables(n)
	cn.fac, cn.ifac = nt.Fac, nt.IFac

}

// Choose .
func (cn *Combinatorics) Choose(n, r int) int {
	if r>n || r<0 {return 0} else if r==0 {return 1}
	k := [2]int{n, r}
	if v, ok := cn.nCr[k]; ok {return v}
	cn.nCr[k] = (cn.Choose(n-1, r)+cn.Choose(n-1, r-1)) % cn.mod
	return cn.nCr[k]
}

// ChooseMod .
func (cn * Combinatorics) ChooseMod(n, r int) int {
	if r>n || r<0 {return 0}
	p := cn.mod; return cn.fac[n]*cn.ifac[r]%p*cn.ifac[n-r]%p
}

// MakeNChooseModTable .
func (cn *Combinatorics) MakeNChooseModTable(n int) []int {
	p, r := cn.mod, len(cn.fac)-1
	nChoose := make([]int, r+1); nChoose[0] = 1
	fmt.Println(len(nChoose))
	for i := 0; i < r; i++ {nChoose[i+1] = nChoose[i]*(n-i)%p}
	for i := 1; i < r; i++ {nChoose[i] = nChoose[i]*cn.ifac[i]%p}
	return nChoose
}

// Permutations (recursive). static method
func (cn *Combinatorics) Permutations(a []interface{}, r int) [][]interface{} {
	var Perm func(a []interface{}, r, i int) (res [][]interface{})
	Perm = func(a []interface{}, r, i int) (res [][]interface{}) {
		n := len(a)
		if r > n || i > r {return}
		if i == r {return append(res, a[:r])}
		for j := i; j < n; j++ {
			a[i], a[j] = a[j], a[i]
			b := make([]interface{}, n); copy(b, a)
			res = append(res, Perm(b, r, i+1)...)
		}
		return
	}
	return Perm(a, r, 0)
}

// Combinations . static method
func (cn *Combinatorics) Combinations(a []interface{}, r int) (res [][]interface{}) {
	n := len(a)
	if r > n || r < 0 {return}
	indices := make([]int, r); for i := 0; i < r; i++ {indices[i] = i}
	res = append(res, a[:r])
	for {
		flg := false
		i := r-1
		for ; i > -1; i-- {if indices[i] != i+n-r {flg = true; break}}
		if !flg {return}
		indices[i]++;
		for j := i+1; j < r; j++ {indices[j] = indices[j-1]+1}
		tmp := make([]interface{}, r); for j := 0; j < r; j++ {tmp[j] = a[indices[j]]}
		res = append(res, tmp)
	}
	return
}

// Node .
type Node struct{}
// Edge .
type Edge struct{
	capacity int `default:1`
	weight int
}
// Graph .
type Graph struct{
	nodes []*Node
	edges []map[int]*Edge

	// tree
	depth, lv, dist, parent []int
	ancestors [][]int
}
// Init .
func (g *Graph) Init(n int) {
	g.nodes = make([]*Node, n)
	// g.toNode = make([]interface{}, 0)
	g.edges = make([]map[int]*Edge, n)
	for u := 0; u < n; u++ {g.edges[u] = make(map[int]*Edge)}
}
// AddNode .
func (g *Graph) AddNode(u int, node *Node) {g.nodes[u] = node}
// AddEdge .
func (g *Graph) AddEdge(u, v int, e *Edge) {g.edges[u][v] = e}

// GetSize .
func (g *Graph) GetSize() int {return len(g.nodes)}

// FloydWarshall .
func (g *Graph) FloydWarshall() [][]int {
	n := g.GetSize()
	d := make([][]int, n)
	for u := 0; u < n; u++ {
		d[u] = make([]int, n)
		for v := 0; v < n; v++ {d[u][v] = Inf}
		d[u][u] = 0
		for v, e := range g.edges[u] {d[u][v] = e.weight}
	}
	for w := 0; w < n; w++ {
		for u := 0; u < n; u++ {
			for v := 0; v < n; v++ {
				d[u][v] = MinInt(d[u][v], d[u][w]+d[w][v])
			}
		}
	}
	return d
}

// DijkstraItem .
type DijkstraItem struct {node int; dist int}
// DijkstraQueue .
type DijkstraQueue []*DijkstraItem
func (h DijkstraQueue) Len() int {return len(h)}
func (h DijkstraQueue) Swap(i, j int) {h[i], h[j] = h[j], h[i]}
func (h DijkstraQueue) Less(i, j int) bool {return h[i].dist < h[j].dist}
// Push .
func (h *DijkstraQueue) Push(x interface{}) {*h = append(*h, x.(*DijkstraItem))}
// Pop .
func (h *DijkstraQueue) Pop() interface{} {n := len(*h); item := (*h)[n-1]; *h = (*h)[:n-1]; return item}

// Dijkstra .
func (g *Graph) Dijkstra(src int) (dist, paths []int) {
	n := g.GetSize()
	dist = make([]int, n); for u := 0; u < n; u++ {dist[u]=Inf}; dist[src]=0
	paths = make([]int, n); paths[src] = 1
	visited := make([]bool, n)
	h := new(DijkstraQueue); heap.Init(h)
	heap.Push(h, &DijkstraItem{node: src, dist:0})
	for len(*h) > 0 {
		item := heap.Pop(h).(*DijkstraItem); u, d := item.node, item.dist
		if visited[u] {continue}; visited[u] = true
		for v, e := range g.edges[u] {
			dv := d + e.weight
			if dv>=dist[v] {if dv==dist[v] {paths[v]+=paths[u]; paths[v]%=Mod}; continue}
			paths[v], dist[v] = paths[u], dv
			heap.Push(h, &DijkstraItem{node: v, dist: dv})
		}
	}
	return
}


// AStarItem .
type AStarItem struct {node int; cost int; heuristicCost, score float64}
// AStarQueue .
type AStarQueue []*AStarItem
func (h AStarQueue) Len() int {return len(h)}
func (h AStarQueue) Swap(i, j int) {h[i], h[j] = h[j], h[i]}
func (h AStarQueue) Less(i, j int) bool {if h[i].score == h[j].score {return h[i].cost < h[j].cost}; return h[i].score < h[j].score}
// Push .
func (h *AStarQueue) Push(x interface{}) {*h = append(*h, x.(*AStarItem))}
// Pop .
func (h *AStarQueue) Pop() interface{} {n := len(*h); item := (*h)[n-1]; *h = (*h)[:n-1]; return item}
// AStarSearch .
func (g *Graph) AStarSearch(src, tgt int, heuristicFunc func(u, tgt int) float64) int {
	n := g.GetSize()
	cost := make([]int, n); for u := 0; u < n; u++ {cost[u]=Inf}
	h := new(AStarQueue); heap.Init(h)
	heap.Push(h, &AStarItem{node: src, cost:0, score: heuristicFunc(src, tgt)})
	for len(*h) > 0 {
		item := heap.Pop(h).(*AStarItem)
		u, c := item.node, item.cost
		if u == tgt {return c}
		if cost[u] != Inf {continue}; cost[u] = c
		for v, e := range g.edges[u] {
			if cost[v] != Inf {continue}
			heuristicCost := heuristicFunc(v, tgt)
			nc := c + e.weight
			heap.Push(h, &AStarItem{node: v, cost: nc, score: float64(nc)+heuristicCost})
		}
	}
	return Inf
}

// BFS .
func (g *Graph) BFS(src int) []int {
	n := g.GetSize()
	g.lv = make([]int, n); for i := 0; i < n; i++ {g.lv[i] = -1}; g.lv[src]=0
	g.dist = make([]int, n); for i := 0; i < n; i++ {g.dist[i] = Inf}; g.dist[src]=0
	g.parent = make([]int, n); for i := 0; i < n; i++ {g.parent[i] = -1}; g.parent[src]=src
	q := []int{src}
	for len(q) > 0 {
		u := q[0]; q = q[1:]
		for v, e := range g.edges[u] {
			if e.capacity==0 || g.lv[v] != -1 {continue}
			g.lv[v] = g.lv[u]+1
			g.dist[v] = g.dist[u] + e.weight
			g.parent[v] = u
			q = append(q, v)
		}
	}
	g.depth = g.lv // for tree.
	return g.lv
}
// Dinic .
func (g *Graph) Dinic(src, sink int) int {
	var flowToSink func(u, flowIn int) int
	flowToSink = func(u, flowIn int) int {
		if u == sink {return flowIn}
		flow := 0
		for v, e := range g.edges[u] {
			if e.capacity == 0 || g.lv[v]<=g.lv[u] {continue}
			f := flowToSink(v, MinInt(flowIn, e.capacity))
			if f == 0 {continue}
			g.edges[u][v].capacity -= f
			if _, has := g.edges[v][u]; has {g.edges[v][u].capacity+=f} else {g.AddEdge(v,u, &Edge{capacity: f})}
			flowIn -= f; flow += f
		}
		return flow
	}
	flow := 0
	for {
		g.BFS(src)
		if g.lv[sink] == -1 {return flow}
		flow += flowToSink(src, Inf)
	}
}

// FindAncestors .
func (g *Graph) FindAncestors() { // Tree Doubling.
	n := g.GetSize()
	g.ancestors = make([][]int, 1); g.ancestors[0] = g.parent
	for i, l := 0, BitsLen(MaxInt(g.depth...)); i < l; i++ {
		ancestor := g.ancestors[len(g.ancestors)-1]
		nxtAncestor := make([]int, n)
		for j := 0; j < n; j++ {nxtAncestor[j] = ancestor[ancestor[j]]}
		g.ancestors = append(g.ancestors, nxtAncestor)
	}
}

// FindDist .
func (g *Graph) FindDist(u, v int) int {return g.dist[u]+g.dist[v] - 2*g.dist[g.FindLCA(u,v)]}
// FindLCA .
func (g *Graph) FindLCA(u, v int) int {
	du, dv := g.depth[u], g.depth[v]
	if du > dv {u,v=v,u; du,dv=dv,du}
	d := dv-du

	// up-stream
	for i, l := 0, BitsLen(d); i < l; i++ {if d>>i&1 == 1 {v = g.ancestors[i][v]}}
	if u==v {return u}

	for i := BitsLen(du)-1; i > -1; i-- {
		nu, nv := g.ancestors[i][u], g.ancestors[i][v]
		if nu == nv {continue}
		u, v = nu, nv
	}
	return g.parent[u]
}

// change "Item, Less" according to problems.

// Item .
type Item struct {
	char rune; cost, index int // ABC009 C
}
// Heap .
type Heap []*Item

func (h Heap) Len() int {return len(h)}
func (h Heap) Swap(i, j int) {h[i], h[j] = h[j], h[i]}
func (h Heap) Less(i, j int) bool {
	// ABC009 C
	if h[i].char == h[j].char {
		if h[i].cost == h[j].cost {
			return h[i].index > h[j].index
		}
		return h[i].cost < h[j].cost
	}
	return h[i].char < h[j].char

}
// Push .
func (h *Heap) Push(x interface{}) { *h = append(*h, x.(*Item))}
// Pop .
func (h *Heap) Pop() interface{} {
	old := *h
	n := len(old)
	item := old[n-1]
	old[n-1] = nil
	*h = old[:n-1]
	return item
}



// UnionFind (Disjoint set).
type UnionFind struct {
	parent, rank, size []int // h := height
}

// Init .
func (uf *UnionFind) Init(n int) {
	uf.parent = make([]int, n); for i := 0; i < n; i++ {uf.parent[i] = i}
	uf.rank = make([]int, n)
	uf.size = make([]int, n); for i := 0; i < n; i++ {uf.size[i] = 1}
}

// Find .
func (uf *UnionFind) Find(u int) int {
	if uf.parent[u]==u {return u}
	uf.parent[u] = uf.Find(uf.parent[u]); return uf.parent[u]
}

// Unite .
func (uf *UnionFind) Unite(u, v int) {
	u, v = uf.Find(u), uf.Find(v)
	if u==v {return}
	if uf.rank[u]<uf.rank[v] {u,v = v,u}
	uf.parent[v] = u
	uf.size[u] += uf.size[v]
	uf.rank[u] = MaxInt(uf.rank[u], uf.rank[v]+1)
}

// Same .
func (uf *UnionFind) Same(u, v int) bool {
	return uf.Find(u) == uf.Find(v)
}




// SignedTriangleArea .
func SignedTriangleArea(p1, p2, p3 PairInt) float64 {
	var x1, y1, x2, y2 float64
	x1 = float64(p2.x - p1.x)
	y1 = float64(p2.y - p1.y)
	x2 = float64(p3.x - p1.x)
	y2 = float64(p3.y - p1.y)
	return (x1*y2 - x2*y1) / 2
}

// TriangleArea .
func TriangleArea(p1, p2, p3 PairInt) float64 {
	return AbsFloat(SignedTriangleArea(p1, p2, p3))
}

// LineSegment .
type LineSegment struct { a, b PairInt }

// LineSegmentIntersect .
func LineSegmentIntersect(seg1, seg2 LineSegment) bool {
	p1, p2, p3, p4 := seg1.a, seg1.b, seg2.a, seg2.b
	t1 := SignedTriangleArea(p1, p2, p3)
	t2 := SignedTriangleArea(p1, p2, p4)
	t3 := SignedTriangleArea(p3, p4, p1)
	t4 := SignedTriangleArea(p3, p4, p2)
	return t1*t2 < 0 && t3*t4 < 0
}




// Kitamasa .
func Kitamasa() {}



var (
	scanner = bufio.NewScanner(os.Stdin)
	reader = bufio.NewReader(os.Stdin)
	writer = bufio.NewWriter(os.Stdout)
)

// Scan .
func Scan() string {
	scanner.Scan()
	return scanner.Text()
}

// ScanInt .
func ScanInt() int {
	v, _ := strconv.Atoi(Scan())
	return v
}



// AtCoder .
var AtCoder = proconSite{
	contests: map[string]contest{
		"ABC001": contest{
			"A": func() {
				var a, b int; fmt.Scan(&a, &b)
				fmt.Println(a - b)
			},

			"B": func() {
				var m float64
				fmt.Scan(&m)
				m *= 0.001
				if m < 0.1 {
					m = .0
				} else if m <= 5 {
					m *= 10
				} else if m <= 30 {
					m += 50
				} else if m <= 70 {
					m = (m - 30) / 5 + 80
				} else {
					m = 89
				}

				res := strconv.Itoa(int(m))
				if len(res) == 1 {
					res = "0" + res
				}
				fmt.Println(res)
			},

		},

		"ABC002": contest{
			"A": func() {
				var x, y int; fmt.Scan(&x, &y)
				fmt.Println(MaxInt(x, y))
			},

			"B": func() {
				var vowels = make(map[rune]bool)
				for _, c := range "aeiou" {
					vowels[c] = true
				}
				var s string; fmt.Scan(&s)
				var t string
				for _, c := range s {
					if !vowels[c] {t += string(c)}
				}
				fmt.Println(t)
			},

			"C": func() {
				var x0, y0, x1, y1, x2, y2 int
				fmt.Scan(&x0, &y0, &x1, &y1, &x2, &y2)
				fmt.Println(TriangleArea(PairInt{x0,y0}, PairInt{x1,y1}, PairInt{x2,y2}))

			},

			"D": func() {
				var n, m int
				var a, b int
				fmt.Scan(&n, &m)

				relations := make([]int, n)

				for i := 0; i < m; i++ {
					fmt.Scan(&a, &b)
					a--; b--
					relations[a] |= 1<<b
					relations[b] |= 1<<a
				}

				res := 0
				for i := 0; i < 1<<n; i++ {
					cnt := 0
					s := (1<<n) - 1
					for j := 0; j < n; j++ {
						if i>>j&1 == 1 {
							cnt++
							s &= relations[j] | 1<<j
						}
						if s&i == i {
							res = MaxInt(res, cnt)
						}
					}
				}
				fmt.Println(res)

			},
		},

		"ABC003": contest{
			"A": func() {
				var n int
				fmt.Scan(&n)
				fmt.Println((n+1)*5000)

			},

			"B": func() {
				var s, t string
				fmt.Scan(&s, &t)
				var atcoder = make(map[byte]bool)
				for _, c := range "atcoder" {atcoder[byte(c)] = true}
				for i := 0; i < len(s); i++ {
					if s[i] == t[i] {continue}
					if s[i] == '@' && atcoder[t[i]] || t[i] == '@' && atcoder[s[i]] {continue}
					fmt.Println("You will lose")
					return
				}
				fmt.Println("You can win")
			},

			"C": func() {
				var n, k int
				fmt.Scan(&n, &k)
				r := make([]int, n)
				for i := 0; i < n; i++ {
					fmt.Scan(&r[i])
				}
				sort.Ints(r)
				res := .0
				for _, v := range r[len(r)-k:] {
					res = (res + float64(v)) / 2
				}
				fmt.Println(res)

			},

		},

		"ABC004": contest{
			"A": func() {
				var n int
				fmt.Scan(&n)
				fmt.Println(2*n)
			},

			"B": func() {
				n := 4
				var board [4]string

				for i := 0; i < n; i++ {
					scanner.Scan()
					board[i] = scanner.Text()

				}
				for i := 3; i > -1; i-- {
					fmt.Println(ReversedString(board[i]))
				}
			},

			"C": func() {
				var n int
				fmt.Scan(&n)
				n %= 30
				res := []rune("123456")
				for i := 0; i < n; i++ {
					j := i % 5
					res[j], res[j+1] = res[j+1], res[j]
				}
				fmt.Println(string(res))
			},

		},

		"ABC005": contest{
			"A": func() {
				var x, y int
				fmt.Scan(&x, &y)
				fmt.Println(y / x)
			},

			"B": func() {
				var n int
				fmt.Scan(&n)
				var t = make([]int, n)
				for i := 0; i < n; i++ {fmt.Scan(&t[i])}
				sort.Ints(t)
				fmt.Println(t[0])
			},

			"C": func() {
				var t, n, m int
				var a, b []int
				fmt.Scan(&t, &n)
				a = make([]int, n)
				for i := 0; i < n; i++ {
					fmt.Scan(&a[i])
				}
				fmt.Scan(&m)
				b = make([]int, m)
				for i := 0; i < m; i++ {
					fmt.Scan(&b[i])
				}

				i, j := 0, 0
				for j < m {
					if i == n {
						fmt.Println("no")
						return
					}
					for b[j] - a[i] > t {
						i++
						if i == n {
							fmt.Println("no")
							return
						}
					}
					if b[j] - a[i] < 0 {
						fmt.Println("no")
						return
					}
					j++; i++
				}
				fmt.Println("yes")

			},

			"D": func() {
				var n int
				fmt.Scan(&n)
				var d = make([][]int, n+1); d[0] = make([]int, n+1)
				for i := 1; i <= n; i++ {
					d[i] = make([]int, n+1)
					for j := 1; j <= n; j++ {
						fmt.Scan(&d[i][j])
					}
				}
				var q int
				fmt.Scan(&q)
				var p = make([]int, q)
				for i := 0; i < q; i++ {
					fmt.Scan(&p[i])
				}

				for i := 1; i <= n; i++ {
					for j := 1; j < n; j++ {
						d[i][j+1] += d[i][j]
					}
				}
				for j := 1; j <= n; j++ {
					for i := 1; i < n; i++ {
						d[i+1][j] += d[i][j]
					}
				}

				res := make([]int, n*n+1)
				for y := 1; y <= n; y++ {
					for x := 1; x <= n; x++ {
						for i := y; i <= n; i++{
							for j := x; j <= n; j++{
								k := (i-y+1) * (j-x+1)
								res[k] = MaxInt(res[k], d[i][j] - d[i][x-1] - d[y-1][j] + d[y-1][x-1])
							}
						}
					}
				}

				for i := 1; i <= n*n; i++ {
					res[i] = MaxInt(res[i], res[i-1])
				}
				for _, v := range p {fmt.Println(res[v])}
			},

		},

		"ABC006": contest{
			"A": func() {
				var n int
				fmt.Scan(&n)
				ans := "NO"
				if n % 3 == 0 {
					ans = "YES"
				} else if strings.Contains(strconv.Itoa(n), "3") {
					ans = "YES"
				}
				fmt.Println(ans)
			},

			"B": func() {
				var n int
				fmt.Scan(&n)
				mod := 10007
				a := [][]int{
					{1, 1, 1},
					{1, 0, 0},
					{0, 1, 0},
				}
				fmt.Println(MatrixPow(a, n-1, mod)[2][0])

			},

			"C": func() {
				var n, m int
				fmt.Scan(&n, &m)
				var x, y, z int

				if m & 1 == 1 {
					y = 1
					m -= 3
					n--
				}

				z = m/2 - n
				x = n - z
				if x >= 0 && y >= 0 && z >= 0 {
					fmt.Printf("%v %v %v\n", x, y, z)
				} else {
					fmt.Println(-1, -1, -1)
				}

			},

			"D": func() {
				var n int
				fmt.Scan(&n)
				var c = make([]int, n)
				for i := 0; i < n; i++ {
					scanner.Scan()
					x, _ := strconv.Atoi(scanner.Text())
					c[i] = x
				}

				a := make([]int, n)
				for i := 0; i < n; i++ {
					a[i] = math.MaxInt64
				}
				for _, v := range c {
					a[BisectLeft(a, v)] = v
				}
				fmt.Println(n - BisectLeft(a, math.MaxInt64))

			},
		},

		"ABC007": contest{
			"A": func() {
				var n int
				fmt.Scan(&n)
				fmt.Println(n - 1)
			},

			"B": func() {
				var s string
				fmt.Scan(&s)
				if s == "a" {
					fmt.Println(-1)
				} else {
					fmt.Println("a")
				}
			},

			"C": func() {
				var h, w, sy, sx, gy, gx int
				fmt.Scan(&h, &w, &sy, &sx, &gy, &gx)
				sy--; sx--; gy--; gx--
				var maze = make([]string, h)
				for i := 0; i < h; i++ {
					fmt.Scan(&maze[i])
				}
				var dist = make([][]int, h)
				for i := 0; i < h; i++ {
					dist[i] = make([]int, w)
					for j := 0; j < w; j++ {
						dist[i][j] = math.MaxInt64
					}
				}
				dist[sy][sx] = 0
				queue := [][]int{[]int{sy, sx}}

				for len(queue) > 0 {
					y, x := queue[0][0], queue[0][1]
					queue = queue[1:]
					for i := -1; i <= 1; i++ {
						for j := -1; j <= 1; j++ {
							if AbsInt(i) == AbsInt(j) { continue }
							ny, nx := y+i, x+j
							if dist[ny][nx] != math.MaxInt64 { continue }
							if maze[ny][nx] == '#' { continue }
							dist[ny][nx] = dist[y][x] + 1
							queue = append(queue, []int{ny, nx})
						}
					}
				}
				fmt.Println(dist[gy][gx])
			},

			"D": func() {
				count := func(d int) int {
					if d <= 4 {return d};
					return d-1;
				}

				f := func(x int) int {
					n := strconv.Itoa(x)
					dp := make([][]int, len(n)+1)
					dp[0] = make([]int, 2); dp[0][0] = 1
					for i := 0; i < len(n); i++ {
						dp[i+1] = make([]int, 2)
						d := int(n[i]-'0')
						dp[i+1][1] = dp[i][1]*8 + dp[i][0]*count(d)
						dp[i+1][0] = dp[i][0]*Booltoi(d != 4 && d != 9)

					}
					return x+1 - (dp[len(n)][0] + dp[len(n)][1])

				}
				var a, b int
				fmt.Scan(&a, &b)
				fmt.Println(f(b) - f(a-1))

			},
		},

		"ABC008": contest{
			"A": func() {
				var s, t int
				fmt.Scan(&s, &t)
				fmt.Println(t-s+1)

			},
			"B": func() {
				var n int
				fmt.Scan(&n)
				var numVotes = make(map[string]int)
				for i := 0; i < n; i++ {
					scanner.Scan()
					numVotes[scanner.Text()]++
				}

				var p []Pair
				for name, cnt := range numVotes {
					p = append(p, Pair{name, cnt})
				}

				sort.SliceStable(p, func(i, j int) bool {
					return p[i].second.(int) > p[j].second.(int)
				})

				fmt.Println(p[0].first.(string))
			},

			"C": func() {
				var n int
				fmt.Scan(&n)
				c := make([]int, n)
				for i := 0; i < n; i++ {
					fmt.Scan(&c[i])
				}
				divCnt := make([]int, n)
				for i := 0; i < n; i++ {
					for _, v := range c {
						divCnt[i] += Booltoi(c[i]%v == 0)
					}
				}
				res := .0
				for _, v := range divCnt {
					res += float64((v+1)/2)/float64(v)
				}
				fmt.Println(res)

			},

			"D": func() {
				var w, h, n int
				fmt.Scan(&w, &h, &n)

				type rectangle struct {
					x1, y1, x2, y2 int
				}

				xy := make([]PairInt, n)
				for i := 0; i < n; i++ {
					x, y := ScanInt(), ScanInt()
					xy[i] = PairInt{x, y}
				}

				cnt := make(map[rectangle]int)

				var count func(r rectangle) int
				count = func(r rectangle) int {
					if res, has := cnt[r]; has {return res}
					res := 0
					x1, y1, x2, y2 := r.x1, r.y1, r.x2, r.y2
					for _, coord := range xy {
						x, y := coord.x, coord.y
						if !(x1 <= x && x <= x2 && y1 <= y && y <= y2) {continue}

						tmp := (x2-x1) + (y2-y1) + 1
						tmp += count(rectangle{x1, y1, x-1, y-1})
						tmp += count(rectangle{x1, y+1, x-1, y2})
						tmp += count(rectangle{x+1, y1, x2, y-1})
						tmp += count(rectangle{x+1, y+1, x2, y2})
						res = MaxInt(res, tmp)
					}
					cnt[r] = res
					return res

				}

				fmt.Println(count(rectangle{1, 1, w, h}))

			},
		},

		"ABC009": contest{
			"A": func() {
				var n int
				fmt.Scan(&n)
				fmt.Println((n+1)/2)
			},
			"B": func() {
				var n int
				fmt.Scan(&n)
				price := make([]int, n)
				for i := 0; i < n; i++ {
					fmt.Scan(&price[i])
				}
				sort.Ints(price)
				fmt.Println(price[BisectLeft(price, price[len(price)-1])-1])
			},

			"C": func() {
				var n, k int
				var s string
				fmt.Scan(&n, &k, &s)
				t := []rune(s)

				cost := make([]int, n)
				for i := 0; i < n; i++ {cost[i] = 1}

				for i := 0; i < n; i++ {
					h := &Heap{}; heap.Init(h)
					for j := i+1; j < n; j++ {
						if t[j] >= t[i] {continue}
						heap.Push(h, &Item{t[j], cost[i]+cost[j], j})
					}
					for len(*h) > 0 {
						item := heap.Pop(h).(*Item)
						if item.cost > k {continue}
						k -= item.cost
						j := item.index
						cost[i], cost[j] = 0, 0
						t[i], t[j] = t[j], t[i]
						break
					}
				}
				fmt.Println(string(t))
			},

			"D": func() {
				var k, m int
				fmt.Scan(&k, &m)
				a, c := make([]int, k), make([]int, k)
				for i := 0; i < k; i++ {fmt.Scan(&a[i])}
				for i := 0; i < k; i++ {fmt.Scan(&c[i])}
				d := make([][]int, k)
				d[0] = c
				mask := 1<<32 - 1
				for i := 0; i < k-1; i++ {
					d[i+1] = make([]int, k)
					d[i+1][i] = mask
				}

				if m <= k {fmt.Println(a[m-1]); return}
				b := make([][]int, k)
				for i := 0; i < k; i++ {
					b[i] = []int{a[k-1-i]}
				}
				d = BitwiseMatPow(d, m-k)
				fmt.Println(BitwiseDot(d, b)[0][0])

			},
		},

		"ABC010": contest{
			"A": func() {
				var s string
				fmt.Scan(&s)
				fmt.Println(s + "pp")
			},

			"B": func() {
				var n int
				fmt.Scan(&n)
				res := 0
				var a int
				for i := 0; i < n; i++ {
					fmt.Scan(&a)
					for a%2 == 0 || a%3 == 2 {
						a--; res++
					}
				}
				fmt.Println(res)
			},

			"C": func() {
				var x1, y1, x2, y2, t, v float64
				var n int
				fmt.Scan(&x1, &y1, &x2, &y2, &t, &v, &n)

				dist := func(x1, y1, x2, y2 float64) float64 {
					return math.Sqrt(math.Pow(x2-x1, 2) + math.Pow(y2-y1, 2))
				}
				ans := "NO"
				for i := 0; i < n; i++ {
					var x, y float64
					fmt.Scan(&x, &y)
					if dist(x1, y1, x, y) + dist(x, y, x2, y2) <= v*t {ans = "YES"}
				}
				fmt.Println(ans)
			},

			"D": func() {
				var n, m, r int
				fmt.Scan(&n, &m, &r)
				g := new(Graph); g.Init(n+1)
				for i := 0; i < m; i++ {
					p := ScanInt()
					g.AddEdge(p, n, &Edge{capacity: 1})
				}

				for i := 0; i < r; i++ {
					a, b := ScanInt(), ScanInt()
					g.AddEdge(a, b, &Edge{capacity: 1})
					g.AddEdge(b, a, &Edge{capacity: 1})
				}
				fmt.Println(g.Dinic(0, n))

			},
		},

		"ABC011": contest{
			"A": func() {
				var n int
				fmt.Scan(&n)
				fmt.Println(n%12+1)
			},
			"B": func() {
				var s string
				fmt.Scan(&s)
				fmt.Println(strings.ToUpper(s[:1]) + strings.ToLower(s[1:]))
			},

			"C": func() {
				var n int
				fmt.Scan(&n)
				ng := make(map[int]bool)
				for i := 0; i < 3; i++ {
					var tmp int
					fmt.Scan(&tmp)
					ng[tmp] = true
				}

				if ng[n] {
					fmt.Println("NO")
					return
				}
				for i := 0; i < 100; i++ {
					flg := false
					for d := -3; d < 0; d++ {
						if ng[n+d] {continue}
						n += d; flg = true
						break
					}
					if !flg {
						fmt.Println("NO")
						return
					}
					if n <= 0 {
						fmt.Println("YES")
						return
					}
				}
				fmt.Println("NO")
			},

			"D": func() {
				var n, d, x, y int
				fmt.Scan(&n, &d, &x, &y)
				x, y = AbsInt(x), AbsInt(y)
				if x%d != 0 || y%d != 0 {fmt.Println(0); return}
				x /= d; y /= d
				r := n - (x+y)
				if r < 0 || r&1 == 1 {fmt.Println(0); return}

				nCr := make(map[PairInt]float64)
				var comb func(n, r int) float64
				comb = func(n, r int) float64 {
					if r < 0 || r > n {return .0}
					if r == 0 {return 1.0}
					p := PairInt{n, r}
					if v, has := nCr[p]; has {return v}
					nCr[p] = comb(n-1, r) + comb(n-1, r-1)/4
					return nCr[p]
				}
				res := .0
				for i := 0; i <= r/2; i++ {
					j := (r - 2*i)/2
					south, north, west, east := i, y+i, j, x+j
					res += comb(n, south) * comb(n-south, north) *
								 comb(n-south-north, west) * comb(n-south-north-west, east)
				}
				fmt.Println(res)


			},
		},

		"ABC012": contest{
			"A": func() {
				var a, b int
				fmt.Scan(&a, &b)
				fmt.Println(b, a)
			},
			"B": func() {
				var n int
				fmt.Scan(&n)
				h := n/3600; n = n%3600
				m := n/60; n = n%60
				s := n
				fmt.Printf("%02d:%02d:%02d\n", h, m, s)
			},

			"C": func() {
				var n int
				fmt.Scan(&n)
				n = 2025 - n
				for i := 1; i <= 9; i++ {
					if n%i != 0 || n/i > 9 {continue}
					fmt.Printf("%d x %d\n", i, n/i)
				}
			},

			"D": func() {
				var n, m int
				fmt.Scan(&n, &m)
				g := new(Graph); g.Init(n)
				for i := 0; i < m; i++ {
					a, b, t := ScanInt(), ScanInt(), ScanInt(); a--; b--
					g.AddEdge(a, b, &Edge{weight: t})
					g.AddEdge(b, a, &Edge{weight: t})
				}
				d := g.FloydWarshall()
				res := Inf
				for _, dists := range d {
					tmp := 0; for _, dist := range dists {tmp = MaxInt(tmp, dist)}
					res = MinInt(res, tmp)
				}
				fmt.Println(res)
			},
		},


		"ABC013": contest{
			"A": func() {
				var x string
				fmt.Scan(&x)
				fmt.Println(x[0] - 'A' + 1)
			},

			"B": func() {
				var a, b int
				fmt.Scan(&a, &b)
				d := AbsInt(a - b)
				fmt.Println(MinInt(d, 10-d))
			},

			"C": func() {
				var n, h, a, b, c, d, e int
				fmt.Scan(&n, &h, &a, &b, &c, &d, &e)

				f := func(y int) (x int) {
					x = int(math.Floor(float64(n*e-h-(d+e)*y)/float64(b+e)) + 1)
					x = MinInt(MaxInt(x, 0), n-y)
					return x
				}
				cand := make([]int, 0)
				for y := 0; y <= n; y++ {
					x := f(y)
					cand = append(cand, a*x + c*y)
				}

				fmt.Println(MinInt(cand...))
			},

			"D": func() {
				var n, m, d int
				fmt.Scan(&n, &m, &d)
				a := make([]int, m)
				for i := 0; i < m; i++ {a[i] = ScanInt()}
				res := make([]int, n)
				for i := 0; i < n; i++ {res[i] = i}
				swap := func(i, j int) {res[i], res[j] = res[j], res[i]}
				for i := m-1; i > -1; i-- {swap(a[i]-1, a[i])}

				binaryMethod := func(a []int, p int) []int {
					b := make([]int, n)
					for i := 0; i < n; i++ {b[i] = i}
					for p>0 {
						if p&1==1 {for i := 0; i < n; i++ {b[i] = a[b[i]]}}
						p >>= 1
						nxt := make([]int, n)
						copy(nxt, a)
						for i := 0; i < n; i++ {nxt[i] = a[nxt[i]]}
						a = nxt
					}
					return b
				}

				for _, x := range binaryMethod(res, d) {fmt.Fprintln(writer, x+1)}
				writer.Flush()
			},
		},

		"ABC014": contest{
			"A": func() {
				var a, b int
				fmt.Scan(&a, &b)
				fmt.Println((a+b-1)/b * b - a)
			},

			"B": func() {
				var n, x int
				fmt.Scan(&n, &x)
				a := make([]int, n)
				for i := 0; i < n; i++ {a[i] = ScanInt()}
				tot := 0
				for i := 0; i < n; i++ {
					if x>>i&1 == 1 {tot += a[i]}
				}
				fmt.Println(tot)
			},

			"C": func() {
				var n int
				fmt.Scan(&n)
				res := make([]int, 1001001)
				for i := 0; i < n; i++ {
					a, b := ScanInt(), ScanInt()
					res[a]++; res[b+1]--
				}
				for i := 0; i < 1e6; i++ {
					res[i+1] += res[i]
				}
				fmt.Println(MaxInt(res...))

			},

			"D": func() {
				n := ScanInt()
				g := Graph{}; g.Init(n)
				for i := 0; i < n-1; i++ {
					a, b := ScanInt(), ScanInt(); a--; b--
					g.AddEdge(a, b, &Edge{weight: 1, capacity:1})
					g.AddEdge(b, a, &Edge{weight: 1, capacity:1})
				}
				g.BFS(0)
				g.FindAncestors()


				q := ScanInt()
				for i := 0; i < q; i++ {
					a, b := ScanInt(), ScanInt(); a--; b--
					fmt.Println(g.FindDist(a, b)+1)
				}

			},

		},

		"ABC015": contest{
			"A": func() {
				var a, b string
				fmt.Scan(&a, &b)
				if len(a) > len(b) {
					fmt.Println(a)
				} else {
					fmt.Println(b)
				}
			},

			"B": func() {
				n := ScanInt()
				tot, cnt := 0, 0
				for i := 0; i < n; i++ {
					a := ScanInt()
					if a != 0 {
						cnt++
						tot += a
					}
				}
				fmt.Println((tot + cnt - 1) / cnt)
			},


			"C": func() {
				n, k := ScanInt(), ScanInt()
				t := make([][]int, n)
				for i := 0; i < n; i++ {
					t[i] = make([]int, k)
					for j := 0; j < k; j++ {
						t[i][j] = ScanInt()
					}
				}

				ans := "Nothing"
				stack := make([][2]int, 1)
				stack[0] = [2]int{-1, 0}

				for len(stack) > 0 {
					data := stack[len(stack)-1]; stack = stack[:len(stack)-1]
					d, x := data[0], data[1]
					if d == n-1 {
						if x == 0 {ans = "Found"; break}
						continue
					}
					for j := 0; j < k; j++ {
						stack = append(stack, [2]int{d+1, x^t[d+1][j]})
					}
				}

				fmt.Println(ans)

			},

			"D": func() {
				var w, n, m int
				fmt.Scan(&w, &n, &m)
				dp := make([][]int, m+1)
				for i := 0; i < m+1; i++ {dp[i] = make([]int, w+1)}

				for i := 0; i < n; i++ {
					a, b := ScanInt(), ScanInt()
					for j := m; j > 0; j-- {
						for k := a; k < w+1; k++ {
							dp[j][k] = MaxInt(dp[j][k], dp[j-1][k-a]+b)
						}
					}
				}
				fmt.Println(dp[m][w])
			},


		},

		"ABC016": contest{
			"A": func() {
				var m, d int
				fmt.Scan(&m, &d)
				ans := "NO"
				if m%d == 0 {ans = "YES"}
				fmt.Println(ans)
			},

			"B": func() {
				var a, b, c int
				fmt.Scan(&a, &b, &c)
				f1, f2 := a+b==c, a-b==c
				var ans string
				if f1 && f2 {
					ans = "?"
				} else if f1 && !f2 {
					ans = "+"
				} else if !f1 && f2 {
					ans = "-"
				} else {
					ans = "!"
				}
				fmt.Println(ans)
			},

			"C": func() {
				var n, m int
				fmt.Scan(&n, &m)
				f := make([]int, n)
				for i := 0; i < m; i++ {
					a, b := ScanInt(), ScanInt()
					a--; b--
					f[a] |= 1<<b
					f[b] |= 1<<a
				}

				res := make([]int, n)
				for i := 0; i < n; i++ {
					tmp := 0
					for j := 0; j < n; j++ {
						if f[i]>>j & 1 == 1 {tmp |= f[j]}
					}

					tmp &= BitwiseNot(f[i] | (1<<i))
					res[i] = BitsCount(tmp)
				}
				for i := 0; i < n; i++ {fmt.Println(res[i])}
			},

			"D": func() {
				var ax, ay, bx, by, n int
				fmt.Scan(&ax, &ay, &bx, &by, &n)

				xy := make([]PairInt, n)
				for i := 0; i < n; i++ {
					xy[i].x, xy[i].y = ScanInt(), ScanInt()
				}

				seg1 := LineSegment{PairInt{ax, ay}, PairInt{bx, by}}
				cnt := 0
				for i := 0; i < n; i++ {
					seg2 := LineSegment{xy[i%n], xy[(i+1)%n]}
					cnt += Booltoi(LineSegmentIntersect(seg1, seg2))
				}
				fmt.Println(cnt/2 + 1)
			},

		},

		"ABC017": contest{
			"A": func() {
				tot := 0
				for i := 0; i < 3; i++ {
					s, e := ScanInt(), ScanInt()
					tot += s/10 *e
				}
				fmt.Println(tot)
			},

			"B": func() {
				x := Scan()

				chokuTail := map[string]bool{
					"ch": true,
					"o": true,
					"k": true,
					"u": true,
				}

				var isChokuWord func(s string) bool
				isChokuWord = func(s string) bool {
					if s == "" {return true}
					var t string
					if len(s) >= 1 {
						t = string(s[len(s)-1])
						if chokuTail[t] && isChokuWord(SubStr(s, 0, len(s)-1)) {
							return true
						}
					}
					if len(s) >= 2 {
						t = SubStr(s, len(s)-2, len(s))
						if chokuTail[t] && isChokuWord(SubStr(s, 0, len(s)-2)) {
							 return true
						}
					}
					return false
				}

				if isChokuWord(x) {
					fmt.Println("YES")
				} else {
					fmt.Println("NO")
				}
			},

			"C": func() {
				var n, m int
				fmt.Scan(&n, &m)
				score := make([]int, m+1)
				tot := 0
				for i := 0; i < n; i++ {
					l, r, s := ScanInt(), ScanInt(), ScanInt()
					score[l-1] += s; score[r] -= s
					tot += s
				}
				for i := 0; i < m; i++ {
					score[i+1] += score[i]
				}
				fmt.Println(tot - MinInt(score[:m]...))
			},

			"D": func() {
				var n, m int
				fmt.Scan(&n, &m)
				f := make([]int, n)
				for i := 0; i < n; i++ {f[i] = ScanInt()}
				prev := make([]int, n+1)
				tmp := make(map[int]int)
				for i := 0; i < n; i++ {
					prev[i+1] = tmp[f[i]]
					tmp[f[i]] = i+1
				}
				dp := make([]int, n+1); dp[0] = 1
				l, s := 0, dp[0]
				for i := 1; i <= n; i++ {
					for l < prev[i] {
						s = (s - dp[l]) % Mod; if s<0 {s += Mod}
						l++
					}
					dp[i] = s
					s = (s + dp[i]) % Mod
				}
				fmt.Println(dp[n])

			},
		},

		"ABC018": contest{
			"A": func() {
				a := make([][]int, 3)
				for i := 0; i < 3; i++ {
					a[i] = make([]int, 2)
					a[i][0] = i
					a[i][1] = ScanInt()
				}
				sort.SliceStable(a, func(i, j int) bool {
					return a[i][1] > a[j][1]
				})
				res := make([]int, 3)
				for i := 0; i < 3; i++ {
					res[a[i][0]] = i+1
				}
				for i := 0; i < 3; i++ {
					fmt.Println(res[i])
				}

			},
			"B": func() {
				s := []rune(Scan())
				n := ScanInt()
				for i := 0; i < n; i++ {
					l, r := ScanInt(), ScanInt()
					l--; r--
					for j := 0; j < (r-l+1)/2; j++ {
						s[l+j], s[r-j] = s[r-j], s[l+j]
					}
				}
				fmt.Println(string(s))

			},
			"C": func() {
				var r, c, k int
				fmt.Scan(&r, &c, &k)
				a := make([][]int, r+2)
				for i := 0; i < r+2; i++ {a[i] = make([]int, c+2)}

				for i := 0; i < r; i++ {
					s := Scan()
					for j := 0; j < c; j++ {a[i+1][j+1] = Booltoi(s[j]=='o')*math.MaxInt64}
				}

				for i := 1; i < r+1; i++ {
					for j := 1; j < c+1; j++ {
						a[i][j] = MinInt(a[i-1][j]+1, a[i][j])
					}
				}
				for i := r; i > 0; i-- {
					for j := 1; j < c+1; j++ {
						a[i][j] = MinInt(a[i+1][j]+1, a[i][j])
					}
				}
				for j := 1; j < c+1; j++ {
					for i := 1; i < r+1; i++ {
						a[i][j] = MinInt(a[i][j-1]+1, a[i][j])
					}
				}
				for j := c; j > 0; j-- {
					for i := 1; i < r+1; i++ {
						a[i][j] = MinInt(a[i][j+1]+1, a[i][j])
					}
				}
				tot := 0
				for i := 1; i < r+1; i++ {
					for j := 1; j < c+1; j++ {
						tot += Booltoi(a[i][j] >= k)
					}
				}
				fmt.Println(tot)
			},
			"D": func() {
				var n, m, p, q, r int
				fmt.Scan(&n, &m, &p, &q, &r)
				h := make([][]int, n)
				for i := 0; i < n; i++ {h[i] = make([]int, m)}

				for i := 0; i < r; i++ {
					x, y, z := ScanInt(), ScanInt(), ScanInt()
					x--; y--
					h[x][y] = z
				}

				S := make([]interface{}, n); for i := 0; i < n; i++ {S[i] = i}
				res := 0
				cn := Combinatorics{}
				for _, s := range cn.Combinations(S, p) {
					tmp := make([]int, m)
					for _, i := range s {
						for j := 0; j < m; j++ {tmp[j] += h[i.(int)][j]}
					}
					sort.Ints(tmp)
					res = MaxInt(res, SumInt(tmp[m-q:]...))
				}
				fmt.Println(res)
			},

		},
		"ABC019": contest{
			"A": func() {
				a := make([]int, 3)
				for i := 0; i < 3; i++ {a[i] = ScanInt()}
				sort.Ints(a)
				fmt.Println(a[1])

			},
			"B": func() {
				s := Scan() + "$"
				t := ""
				prev := "$"
				cnt := 0
				for _, c := range s {
					if string(c) == prev {
						cnt++
					} else {
						t += prev + strconv.Itoa(cnt)
						prev = string(c)
						cnt = 1
					}
				}
				fmt.Println(SubStr(t, 2, len(t)))


			},
			"C": func() {
				n := ScanInt()
				a := make([]int, n)
				for i := 0; i < n; i++ {a[i] = ScanInt()}
				res := make(map[int]bool)
				for i := 0; i < n; i++ {
					for a[i]&1 == 0 {
						a[i] >>= 1
					}
					res[a[i]] = true
				}
				fmt.Println(len(res))

			},
			"D": func() {
				n := ScanInt()
				inquire := func(u, v int) int {
					fmt.Println(fmt.Sprintf("? %v %v", u, v))
					return ScanInt()
				}
				find := func(u int) (v, dist int) {
					for i := 1; i <= n; i++ {
						if i==u {continue}
						d := inquire(u, i)
						if d>dist {dist=d; v=i}
					}
					return
				}
				u, _ := find(1)
				_, d := find(u)
				fmt.Printf("! %v\n", d)
			},

		},
		"ABC020": contest{
			"A": func() {
				q := ScanInt()
				if q == 1 {
					fmt.Println("ABC")
				} else {
					fmt.Println("chokudai")
				}

			},
			"B": func() {
				var a, b string
				fmt.Scan(&a, &b)
				c, _ := strconv.Atoi(a+b)
				fmt.Println(c*2)


			},
			"C": func() {
				var h, w, t int
				fmt.Scan(&h, &w, &t)
				s := make([][]rune, h)
				for i := 0; i < h; i++ {s[i] = []rune(Scan())}
				var sy, sx, gy, gx int
				for i := 0; i < h; i++ {
					for j := 0; j < w; j++ {
						if s[i][j] == 'S' {sy, sx = i, j}
						if s[i][j] == 'G' {gy, gx = i, j}
					}
				}
				s[sy][sx] = '.'
				s[gy][gx] = ','
				src, tgt := sy*w+sx, gy*w+gx

				heuristicFunc := func(u, tgt int) float64 {
					uy, ux := Divmod(u,w)
					vy, vx := Divmod(tgt,w)
					return math.Abs(float64(vy-uy)) + math.Abs(float64(vx-ux))
				}

				shortestDist := func(x int) int {
					g := new(Graph); g.Init(h*w)

					for i := 0; i < h; i++ {
						for j := 0; j < w; j++ {
							u := i*w + j
							if i > 0 {
								weight := 1; if s[i-1][j] == '#' {weight = x}
								g.AddEdge(u, (i-1)*w+j, &Edge{weight: weight})
							}
							if i < h-1 {
								weight := 1
								if s[i+1][j] == '#' {weight = x}
								g.AddEdge(u, (i+1)*w+j, &Edge{weight: weight})
							}
							if j > 0 {
								weight := 1
								if s[i][j-1] == '#' {weight = x}
								g.AddEdge(u, i*w+j-1, &Edge{weight: weight})
							}
							if j < w-1 {
								weight := 1
								if s[i][j+1] == '#' {weight = x}
								g.AddEdge(u, i*w+j+1, &Edge{weight: weight})
							}
						}
					}
					dist, _ := g.Dijkstra(src)
					return dist[tgt]
					return g.AStarSearch(src, tgt, heuristicFunc)
				}

				binarySearch := func() int {
					lo, hi := 1, t+1
					for lo+1 < hi {
						x := (lo+hi)/2
						d := shortestDist(x)
						if d > t {
							hi = x
						} else {
							lo = x
						}
					}
					return lo
				}
				fmt.Println(binarySearch())

			},

			"D": func() {
				var n, k int
				fmt.Scan(&n, &k)
				div := FindDivisors(k)
				l := len(div)
				s := make([]int, l)
				for i, d := range div {s[i] = (1+n/d)*(n/d)/2 * d % Mod}
				for i := l-1; i > -1; i-- {
					for j := i+1; j < l; j++ {
						if div[j]%div[i] == 0 {
							s[i] = (s[i]-s[j])%Mod; if s[i] < 0 {s[i] += Mod}
						}
					}
				}
				tot := 0
				for i := 0; i < l; i++ {
					tot += s[i] * k / div[i]
					tot %= Mod
				}
				fmt.Println(tot)


			},

		},

		"ABC021": contest{
			"A": func() {
				n := ScanInt()
				res := []int{}
				for i := 0; i < 5; i++ {
					if n>>i & 1 == 1 {res = append(res, 1<<i)}
				}
				fmt.Println(len(res))
				for _, v := range res {fmt.Println(v)}
			},
			"B": func() {
				var n, a, b, k int
				fmt.Scan(&n, &a, &b, &k)
				p := make([]int, k)
				for i := 0; i < k; i++ {p[i] = ScanInt()}
				p = append(p, b)
				visited := map[int]bool{a: true}
				for _, v:= range p {
					if visited[v] {fmt.Println("NO"); return}
					visited[v] = true
				}
				fmt.Println("YES")


			},

			"C": func() {
				var n, a, b, m int
				fmt.Scan(&n, &a, &b, &m)
				a--; b--

				g := new(Graph); g.Init(n)

				for i := 0; i < m; i++ {
					x, y := ScanInt(), ScanInt()
					x--; y--
					g.AddEdge(x, y, &Edge{weight: 1})
					g.AddEdge(y, x, &Edge{weight: 1})

				}

				_, paths := g.Dijkstra(a)

				fmt.Println(paths[b])

			},

			"D": func() {
				var n, k int
				fmt.Scan(&n, &k)
				cn := Combinatorics{}; cn.Init(2e5, Mod)
				fmt.Println(cn.ChooseMod(n+k-1, k))
			},
		},

		"ABC022": contest{
			"A": func() {
				var n, s, t, w int
				fmt.Scan(&n, &s, &t, &w)
				a := make([]int, n); a[0] = w
				tot := Booltoi(s<=w && w<=t)
				for i := 1; i < n; i++ {
					a[i] = ScanInt()
					a[i] += a[i-1]
					tot += Booltoi(s<=a[i] && a[i]<=t)
				}
				fmt.Println(tot)

			},

			"B": func() {
				n := ScanInt()
				a := make([]int, n)
				for i := 0; i < n; i++ {a[i] = ScanInt()}
				cnt := make(map[int]int)
				for _, v := range a {cnt[v]++}
				fmt.Println(n-len(cnt))
			},

			"C": func() {
				var n, m int
				fmt.Scan(&n, &m)

				g := new(Graph); g.Init(n)
				dist0 := make([]int, n)
				for i := 0; i < n; i++ {dist0[i] = Inf}

				for i := 0; i < m; i++ {
					u, v, l := ScanInt(), ScanInt(), ScanInt()
					u--; v--
					if u > v {u,v = v,u}
					if u == 0 {dist0[v] = l; continue}
					g.AddEdge(u,v, &Edge{weight: l})
					g.AddEdge(v,u, &Edge{weight: l})
				}

				dist := g.FloydWarshall()
				tmp := make([]interface{}, n-1)
				for i := 0; i < n-1; i++ {tmp[i] = i+1}
				res := Inf
				cn := Combinatorics{}
				for _, comb := range cn.Combinations(tmp, 2) {
					u := comb[0].(int)
					v := comb[1].(int)
					d := dist0[u] + dist[u][v] + dist0[v]
					res = MinInt(res, d)
				}

				if res == Inf {fmt.Println(-1)} else {fmt.Println(res)}
			},

			"D": func() {
				n := ScanInt()
				a, b := make([]PairInt, n), make([]PairInt, n)
				for i := 0; i < n; i++ {
					x, y := ScanInt(), ScanInt()
					a[i] = PairInt{x,y}
				}
				for i := 0; i < n; i++ {
					x, y := ScanInt(), ScanInt()
					b[i] = PairInt{x,y}
				}

				findG := func(a []PairInt) (float64, float64) {
					var gx, gy float64
					n := float64(len(a))
					for _, p := range a {
						gx += float64(p.x)
						gy += float64(p.y)
					}
					gx /= n; gy /= n
					return gx, gy
				}
				findDist := func(a []PairInt) float64 {
					gx, gy := findG(a)
					tot := .0
					for _, p := range a {
						tot += math.Sqrt(math.Pow(float64(p.x)-gx, 2) + math.Pow(float64(p.y)-gy, 2))
					}
					return tot
				}
				fmt.Println(findDist(b)/findDist(a))
			},
		},

		"ABC023": contest{
			"A": func() {
				x := ScanInt()
				fmt.Println(x/10 + x%10)
			},

			"B": func() {
				n, s := ScanInt(), Scan()
				if n&1^1 == 1 {fmt.Println(-1); return}
				a := []rune("abc")
				i := ((1-n/2)%3+3)%3
				for _, c := range s {
					if c != a[i] {fmt.Println(-1); return}
					i = (i+1)%3
				}
				fmt.Println(n/2)
			},

			"C": func() {
				var h, w, k, n int
				fmt.Scan(&h, &w, &k, &n)
				r, c := make([]int, n), make([]int, n)
				for i := 0; i < n; i++ {
					r[i], c[i] = ScanInt()-1, ScanInt()-1
				}

				rb, cb := make([]int, h), make([]int, w)
				for i := 0; i < n; i++ {
					rb[r[i]]++; cb[c[i]]++
				}

				rbb := make([]int, MaxInt(k+1, w+1))
				for i := 0; i < h; i++ {
					rbb[rb[i]]++
				}
				cbb := make([]int, MaxInt(k+1, h+1))
				for i := 0; i < w; i++ {
					cbb[cb[i]]++
				}

				tot := 0
				for i := 0; i < k+1; i++ {
					tot += rbb[i] * cbb[k-i]
				}

				real := make([]int, MaxInt(k+1, h+w))
				for i := 0; i < n; i++ {
					real[rb[r[i]]+cb[c[i]]-1]++
				}
				tot -= real[k-1]; tot += real[k]
				fmt.Println(tot)

			},

			"D": func() {
				n := ScanInt()
				h, s := make([]int, n), make([]int, n)
				for i := 0; i < n; i++ {h[i], s[i] = ScanInt(), ScanInt()}
				isOk := func(x int) bool {
					tLim := make([]int, n)
					for i := 0; i < n; i++ {
						d := x-h[i]; if d < 0 {d -= (s[i]-1)}
						tLim[i] = d/s[i]
					}
					sort.Ints(tLim)
					for i := 0; i < n; i++ {if tLim[i] < i {return false}}
					return true
				}
				binarySearch := func() int {
					lo, hi := 0, int(1e14)
					for lo+1 < hi {if x := (lo+hi)/2; isOk(x) {hi = x} else {lo = x}}
					return hi
				}
				fmt.Println(binarySearch())
			},

		},

		"ABC024": contest{
			"A": func() {
				var a, b, c, k, s, t int
				fmt.Scan(&a, &b, &c, &k, &s, &t)
				fmt.Println(a*s+b*t - (s+t)*c*Booltoi(s+t>=k))
			},

			"B": func() {
				var n, t int
				fmt.Scan(&n, &t)
				a := make([]int, n)
				for i := 0; i < n; i++ {a[i] = ScanInt()}
				tot := t
				for i := 0; i < n-1; i++ {tot += MinInt(t, a[i+1]-a[i])}
				fmt.Println(tot)
			},

			"C": func() {
				var n, d, k int
				fmt.Scan(&n, &d, &k)
				l, r := make([]int, d), make([]int, d)
				for i := 0; i < d; i++ {l[i], r[i] = ScanInt(), ScanInt()}
				s, t := make([]int, k), make([]int, k)
				for i := 0; i < k; i++ {s[i], t[i] = ScanInt(), ScanInt()}

				res := make([]int, k)
				for i := 0; i < d; i++ {
					for j := 0; j < k; j++ {
						if s[j] == t[j] {continue}
						if s[j]<l[i] || s[j]>r[i] {continue}
						if t[j]<l[i] {
							s[j] = l[i]
						} else if t[j]>r[i] {
							s[j] = r[i]
						} else {
							s[j] = t[j]
							res[j] = i+1
						}
					}
				}
				for _, v := range res {fmt.Println(v)}
			},

			"D": func() {
				var a, b, c int
				fmt.Scan(&a, &b, &c)
				p := Mod
				denom := Pow(((a*b-b*c+c*a)%p+p)%p, p-2, p)
				w := ((b*c-a*b)%p+p)%p*denom%p
				h := ((b*c-a*c)%p+p)%p*denom%p
				fmt.Println(h, w)
			},
		},

		"ABC025": contest{
			"A": func() {
				s, n := Scan(), ScanInt()
				i, j := Divmod(n-1, 5)
				fmt.Println(string(s[i])+string(s[j]))
			},

			"B": func() {
				var n, a, b int
				fmt.Scan(&n, &a, &b)
				dist := make(map[string]int)
				for i := 0; i < n; i++ {
					s, d := Scan(), ScanInt()
					dist[s] += MinInt(MaxInt(d, a), b)
				}
				d := dist["East"] - dist["West"]
				if d == 0 {
					fmt.Println(0)
				} else if d > 0 {
					fmt.Printf("East %v\n", d)
				} else {
					fmt.Printf("West %v\n", -d)
				}
			},

			"C": func() {
				b, c := make([]int, 6), make([]int, 8)
				for i := 0; i < 6; i++ {b[i] = ScanInt()}
				for i := 0; i < 8; i++ {if (i+1)%3==0 {continue}; c[i] = ScanInt()}

				tot := SumInt(b...) + SumInt(c...)
				var f func(s [9]int) int
				cache := make(map[[9]int]int)
				f = func(s [9]int) int {
					if v, has := cache[s]; has {return v}
					cand := []int{}
					for i := 0; i < 9; i++ {
						if s[i] == 0 {cand = append(cand, i)}
					}
					if len(cand) == 0 {
						tot := 0
						for i := 0; i < 6; i++ {tot += b[i]*Booltoi(s[i]==s[i+3])}
						for i := 0; i < 8; i++ {tot += c[i]*Booltoi(s[i]==s[i+1])}
						cache[s] = tot
						return tot
					}
					flg := len(cand)&1
					res := []int{}
					for _, i := range cand {
						s[i] = (flg^1) + 1
						res = append(res, f(s))
						s[i] = 0
					}
					sort.Ints(res)

					if flg==0 {cache[s]=res[0]} else {cache[s]=res[len(res)-1]}
					return cache[s]
				}
				var tmp [9]int
				a := f(tmp)
				fmt.Printf("%v\n%v\n", a, tot-a)

			},
		},

		"ABC026": contest{
			"A": func() {
				a := ScanInt()
				fmt.Println(a/2 * (a-a/2))
			},

			"B": func() {
				n := ScanInt()
				r := make([]int, n)
				for i := 0; i < n; i++ {r[i] = ScanInt()}
				sort.Ints(r)
				s := make([]float64, n)
				for i := 0; i < n; i++ {s[i] = math.Pow(float64(r[i]), 2)*math.Pi}
				tot := .0
				for i := n-1; i > -1; i-=2 {
					tot += s[i]
				}
				for i := n-2; i > -1; i-=2 {
					tot -= s[i]
				}
				fmt.Println(tot)
			},

			"C": func() {
				n := ScanInt()
				g := new(Graph); g.Init(n)
				for i := 1; i < n; i++ {
					g.AddEdge(ScanInt()-1, i, &Edge{})
				}

				var f func(u int) int
				f = func(u int) int {
					if len(g.edges[u])==0 {return 1}
					s := []int{}
					for v := range g.edges[u] {
						s = append(s, f(v))
					}
					sort.Ints(s)
					return s[0] + s[len(s)-1] + 1
				}

				fmt.Println(f(0))
			},

			"D": func() {
				var a, b, c float64
				fmt.Scan(&a, &b, &c)

				f := func(t float64) float64 {
					return a*t + b*math.Sin(c*t*math.Pi) - 100
				}

				bisect := func() float64 {
					lo, hi := .0, 200.0
					for hi-lo > 1e-13 {
						t := (lo+hi)/2
						if f(t) > 0 {hi=t} else {lo=t}
					}
					return lo
				}
				fmt.Println(bisect())


			},
		},
		"ABC027": contest{
			"A": func() {
				l := make([]int, 3)
				for i := 0; i < 3; i++ {l[i] = ScanInt()}
				sort.Ints(l)
				if l[0]==l[1] {fmt.Println(l[2])} else {fmt.Println(l[0])}
			},
			"B": func() {
				n := ScanInt()
				a := make([]int, n)
				for i := 0; i < n; i++ {a[i] = ScanInt()}
				m, r := Divmod(SumInt(a...), n)
				if r!=0 {fmt.Println(-1); return}
				tot := 0
				cnt := 0
				pop := 0
				for _, x := range a {
					pop += x; cnt++
					if pop != m*cnt {tot++} else {pop,cnt = 0,0}
				}
				fmt.Println(tot)
			},

			"C": func() {
				n := ScanInt()
				flg := BitsLen(n)&1^1
				t := 0
				x := 1
				for x <= n {
					t++
					if t&1^flg == 0 {x = 2*x} else {x = 2*x+1}
				}
				if t&1==1 {fmt.Println("Aoki")} else {fmt.Println("Takahashi")}
			},
		},

		"ABC028": contest{

			"A": func() {
				n := ScanInt()
				var ans string
				if n < 60 {
					ans = "Bad"
				} else if n < 90 {
					ans = "Good"
				} else if n < 100 {
					ans = "Great"
				} else {
					ans = "Perfect"
				}
				fmt.Println(ans)
			},

			"B": func() {
				s := Scan()
				cnt := make(map[rune]int)
				for _, c := range s {
					cnt[c]++;
				}
				res := []int{}
				for _, c := range "ABCDEF" {
					res = append(res, cnt[c])
				}
				fmt.Println(strings.Trim(fmt.Sprint(res), "[]"))

			},

			"C": func() {
				var a, b, c, d, e int
				fmt.Scan(&a, &b, &c, &d, &e)
				fmt.Println(MaxInt(b+c+e, a+d+e))

			},

			"D": func() {
				var n, k float64
				fmt.Scan(&n, &k)
				c := 3*2*(k-1)*(n-k) + 3*(n-1) + 1
				fmt.Println(c/math.Pow(n, 3))
			},


		},

		"ABC029": contest{
			"A": func() {
				w := Scan()
				fmt.Println(w+"s")
			},

			"B": func() {
				cnt := 0
				for i := 0; i < 12; i++ {
					s := Scan()
					cnt += Booltoi(strings.ContainsRune(s, 'r'))
				}
				fmt.Println(cnt)
			},

			"C": func() {
				n := ScanInt()
				q := []string{""}
				for len(q[0]) < n {
					s := q[0]; q = q[1:]
					for _, c := range "abc" {
						q = append(q, s+string(c))
					}
				}
				for _, s := range q {
					fmt.Println(s)
				}
			},

			"C2": func() {
				n := ScanInt()
				q := list.New()
				q.PushBack("")
				for {
					s := q.Front()
					if len(s.Value.(string)) == n {break}
					for _, c := range "abc" {
						q.PushBack(s.Value.(string)+string(c))
					}
					q.Remove(s)
				}
				for q.Len() > 0 {
					s := q.Front()
					fmt.Println(s.Value.(string))
					q.Remove(s)
				}
			},

			"C3": func() {
				n := ScanInt()

				var dfs func(s string)
				dfs = func(s string) {
					if len(s) == n {fmt.Println(s); return}
					for _, c := range "abc" {dfs(s+string(c))}
				}
				dfs("")
			},

			"D": func() {
				n := ScanInt()
				tot := 0
				for i := 0; i < 9; i++ {
					tot += n/Pow(10,i+1)*Pow(10,i) + MinInt(MaxInt(n%Pow(10,i+1)-Pow(10,i)+1,0),Pow(10,i))
				}
				fmt.Println(tot)
			},

		},

		"ABC030": contest{
			"A": func() {
				var a, b, c, d int
				fmt.Scan(&a, &b, &c, &d)
				e, f := b*c, d*a
				var ans string
				if e>f {
					ans = "TAKAHASHI"
				} else if e<f {
					ans = "AOKI"
				} else {
					ans = "DRAW"
				}
				fmt.Println(ans)

			},

			"B": func() {
				var n int; var m float64
				fmt.Scan(&n, &m)
				d := AbsFloat((float64(n%12)+m/60)*30 - m*6)
				fmt.Println(Min(d, 360-d))
			},

			"C": func() {
				var n, m, x, y int
				fmt.Scan(&n, &m, &x, &y)
				a := make([]int, n)
				b := make([]int, m)
				for i := 0; i < n; i++ {a[i] = ScanInt()}
				for i := 0; i < m; i++ {b[i] = ScanInt()}

				cnt := 0
				p := 1
				t := 0
				for {
					if p==1 {
						i := BisectLeft(a, t)
						if i==n {break}
						t = a[i]+x
					} else {
						i := BisectLeft(b, t)
						if i==m {break}
						t = b[i]+y
						cnt++
					}
					p ^= 1
				}
				fmt.Println(cnt)
			},

			"D": func() {
				var n, a int; var k string
				fmt.Scan(&n, &a); k = Scan()
				a--;
				b := make([]int, n)
				for i := 0; i < n; i++ {b[i] = ScanInt()-1}

				c := make([]int, n); for i := 0; i < n; i++ {c[i] = -1}
				for i := 0; i < n+1; i++ {
					if strconv.Itoa(i)==k {fmt.Println(a+1); return}
					if c[a] != -1 {
						l, d := i-c[a], c[a]
						r, m := 1, int(k[len(k)-1]-'0')
						for i := len(k)-2; i > -1; i-- {r = r*10%l; m += r*int(k[i]-'0')%l}
						m = ((m-d)%l+l)%l
						for i := 0; i < m; i++ {a = b[a]}
						fmt.Println(a+1); return
					}
					c[a] = i; a = b[a]
				}
			},

		},

		"ABC031": contest{
			"A": func() {
				var a, d int
				fmt.Scan(&a, &d)
				if a > d {a,d = d,a}
				fmt.Println((a+1)*d)
			},

			"B": func() {
				var l, h, n int
				fmt.Scan(&l, &h, &n)
				for i := 0; i < n; i++ {
					a := ScanInt()
					if a < l {
						fmt.Println(l-a)
					} else if a > h {
						fmt.Println(-1)
					} else {
						fmt.Println(0)
					}
				}
			},

			"C": func() {
				n := ScanInt()
				a := make([]int, n)
				for i := 0; i < n; i++ {a[i] = ScanInt()}
				for i := 0; i < n-2; i+=2 {a[i+2] += a[i]}
				for i := 1; i < n-2; i+=2 {a[i+2] += a[i]}
				a = append(make([]int, 2), a...)

				score := func(i, j int) (x, y int) {
					if i > j {i,j = j,i}
					i += 2; j += 2

					if (j-i)&1 == 1 {
						x = a[j-1] - a[i-2]
						y = a[j] - a[i-1]
					} else {
						x = a[j] - a[i-2]
						y = a[j-1] - a[i-1]
					}
					return
				}

				res := -Inf
				for i := 0; i < n; i++ {
					s, t := -Inf, -Inf
					for j := 0; j < n; j++ {
						if i==j {continue}
						x, y := score(i,j)
						if y>s {s, t = y, x}
					}
					res = MaxInt(res, t)
				}
				fmt.Println(res)
			},

			"D": func() {
				var k, n int
				fmt.Scan(&k, &n)
				q := make([]string, 1); q[0] = ""
				for len(q[0]) < k {
					s := q[0]; q = q[1:]
					for _, c := range "123" {q = append(q, s+string(c))}
				}

				v := make([]string, n)
				w := make([]string, n)
				for i := 0; i < n; i++ {v[i], w[i] = Scan(), Scan()}

				for _, comb := range q {
					s := make(map[int]string)
					flg := true
					for i := 0; i < n; i++ {
						l := 0
						for _, c := range v[i] {
							d := int(c-'0')-1
							r := l+int(comb[d]-'0')
							if r > len(w[i]) {flg = false; break}
							t := w[i][l:r]
							if s[d] != "" && s[d] != t {flg = false; break}
							s[d] = t
							l = r
						}
						if (flg) && l==len(w[i]) {continue}
						flg = false; break
					}
					if flg {for i := 0; i < k; i++ {fmt.Println(s[i])}; return}
				}
			},
		},

		"ABC032": contest{
			"A": func() {
				var a, b, n int
				fmt.Scan(&a, &b, &n)
				l := Lcm(a, b)
				fmt.Println((n+l-1)/l*l)
			},

			"B": func() {
				cand := make(map[string]bool)
				s, k := Scan(), ScanInt()
				for i := 0; i+k <= len(s); i++ {
					cand[s[i:i+k]] = true
				}
				fmt.Println(len(cand))
			},

			"C": func() {
				var n, k int
				fmt.Scan(&n, &k)
				s := make([]int, n);
				for i := 0; i < n; i++ {s[i] = ScanInt()}
				if MinInt(s...) == 0 {fmt.Println(n); return}
				if k==0 {fmt.Println(0); return}

				res, tmp := 0, 1
				for l,r := 0,0; r < n; r++ {
					tmp *= s[r]
					for tmp>k {tmp /= s[l]; l++}
					res = MaxInt(res, r-l+1)
				}
				fmt.Println(res)

			},
		},

		"ABC033": contest{
			"A": func() {
				s := Scan()
				for i := 0; i < 3; i++ {
					if s[i] != s[i+1] {fmt.Println("DIFFERENT"); return}
				}
				fmt.Println("SAME")
			},

			"B": func() {
				n := ScanInt()
				s := make([]string, n)
				p := make([]int, n)
				tot := 0
				for i := 0; i < n; i++ {s[i], p[i] = Scan(), ScanInt(); tot += p[i]}
				for i := 0; i < n; i++ {
					if p[i] <= tot/2 {continue}
					fmt.Println(s[i]); return
				}
				fmt.Println("atcoder")

			},

			"C": func() {
				f := Scan()
				tot := 0
				for _, s := range strings.Split(f, "+") {
					tot += Booltoi(!strings.ContainsRune(s, '0'))
				}
				fmt.Println(tot)
			},
		},

		"ABC034": contest{
			"A": func() {
				var x, y int
				fmt.Scan(&x, &y)
				var ans string
				if y>x {ans = "Better"} else {ans = "Worse"}
				fmt.Println(ans)
			},

			"B": func() {
				n := ScanInt()
				if n&1==1 {fmt.Println(n+1)} else {fmt.Println(n-1)}
			},

			"C": func() {
				cn := Combinatorics{}; cn.Init(2e6,Mod)
				var w, h int
				fmt.Scan(&w, &h)
				fmt.Println(cn.ChooseMod(w+h-2, h-1))

			},

			"D": func() {
				var n, k int
				fmt.Scan(&n, &k)
				w, p := make([]float64, n), make([]float64, n)
				for i := 0; i < n; i++ {fmt.Scan(&w[i], &p[i])}

				f := func(x float64) bool {
					a := make([]float64, n)
					for i := 0; i < n; i++ {
						a[i] = w[i]*(p[i]-x)
					}
					sort.SliceStable(a, func(i,j int) bool {return a[i] > a[j]})
					s := .0
					for i := 0; i < k; i++ {s += a[i]}
					return s>=0
				}

				binarySearch := func() float64 {
					lo, hi := .0, 100.1
					for hi-lo > Eps {
						x := (lo+hi)/2
						if f(x) {lo=x} else {hi=x}
					}
					return lo
				}
				fmt.Println(binarySearch())
			},
		},

		"ABC035": contest{
			"A": func() {
				var w, h int
				fmt.Scan(&w, &h)
				if w*3==h*4 {fmt.Println("4:3")} else {fmt.Println("16:9")}
			},

			"B": func() {
				s, t := Scan(), ScanInt()
				z, y, x := 0, 0, 0
				for _, c := range s {
					if c == '?' {z++}
					if c == 'U' {y++}
					if c == 'D' {y--}
					if c == 'L' {x--}
					if c == 'R' {x++}
				}
				a := AbsInt(y) + AbsInt(x)
				if t == 1 {fmt.Println(a+z)} else {fmt.Println(MaxInt(a-z, (a-z)&1))}
			},

			"C": func() {
				var n, q int
				fmt.Scan(&n, &q)
				s := make([]int, n+1)
				for i := 0; i < q; i++ {
					l, r := ScanInt(), ScanInt(); l--; r--
					s[l]++; s[r+1]--
				}

				res := make([]string, n)
				for i := 0; i < n; i++ {
					s[i+1] += s[i]
					res[i] = strconv.Itoa(s[i]&1)
				}
				fmt.Println(strings.Join(res, ""))
			},

			"D": func() {
				var n, m, t int
				fmt.Scan(&n, &m, &t)
				a := make([]int, n)
				for i := 0; i < n; i++ {a[i] = ScanInt()}

				g1 := Graph{}; g1.Init(n)
				g2 := Graph{}; g2.Init(n)
				for i := 0; i < m; i++ {
					u, v, c := ScanInt(), ScanInt(), ScanInt(); u--; v--
					g1.AddEdge(u,v, &Edge{weight:c})
					g2.AddEdge(v,u, &Edge{weight:c})
				}
				d1, _ := g1.Dijkstra(0)
				d2, _ := g2.Dijkstra(0)
				res := make([]int, n)
				for i := 0; i < n; i++ {
					res[i] = (t-d1[i]-d2[i])*a[i]
				}
				fmt.Println(MaxInt(res...))
			},

		},

		"ABC036": contest{
			"A": func() {
				var a, b int; fmt.Scan(&a, &b)
				fmt.Println((b+a-1)/a )
			},

			"B": func() {
				n := ScanInt()
				s := make([][]rune, n)
				for i := 0; i < n; i++ {
					s[i] = []rune(Scan())
				}
				t := make([][]rune, n)
				for i := 0; i < n; i++ {
					t[i] = make([]rune, n)
				}
				for i := 0; i < n; i++ {
					for j := 0; j < n; j++ {
						t[i][j] = s[n-1-j][i]
					}
				}
				for i := 0; i < n; i++ {fmt.Println(string(t[i]))}
			},

			"C": func() {
				n := ScanInt()
				a := make([]int, n); for i := 0; i < n; i++ {a[i] = ScanInt()}
				tmp := make([][2]int, n)
				for i := 0; i < n; i++ {tmp[i] = [2]int{i, a[i]}}
				sort.SliceStable(tmp, func(i, j int) bool {return tmp[i][1] <= tmp[j][1]})
				b := make([]string, n)
				prev := -1
				for i, j := 0, -1; i < n; i++ {
					k, x := tmp[i][0], tmp[i][1]
					if x != prev {j++}
					b[k] = strconv.Itoa(j)
					prev = x
				}
				writer.WriteString(strings.Join(b, "\n")); writer.Flush()
			},

			"D": func() {
				n := ScanInt()
				g := new(Graph); g.Init(n)

				for i := 0; i < n-1; i++ {
					a, b := ScanInt(), ScanInt(); a--; b--
					g.AddEdge(a,b, &Edge{capacity: 1})
					g.AddEdge(b,a, &Edge{capacity: 1})
				}
				g.BFS(0)

				var f func(u int) (int, int)
				f = func(u int) (white, black int){
					white, black = 1, 1
					for v := range g.edges[u] {
						if v==g.parent[u] {continue}
						w, b := f(v)
						white *= (w+b); white %= Mod
						black *= w; black %= Mod
					}
					return
				}
				fmt.Println(SumInt(f(0))%Mod)
			},
		},

		"ABC037": contest{
			"A": func() {
				var a, b, c int
				fmt.Scan(&a, &b, &c)
				fmt.Println(c/MinInt(a,b))
			},

			"B": func() {
				n, q := ScanInt(), ScanInt()
				a := make([]int, n)
				for i := 0; i < q; i++ {
					l, r, t := ScanInt(), ScanInt(), ScanInt()
					l--; r--
					for j := l; j < r+1; j++ {a[j] = t}
				}
				for i := 0; i < n; i++ {fmt.Println(a[i])}
			},

			"C": func() {
				n, k := ScanInt(), ScanInt()
				a := make([]int, n+1)
				for i := 1; i < n+1; i++ {a[i] = ScanInt()}
				for i := 0; i < n; i++ {a[i+1] += a[i]}
				s := 0
				for i := k; i < n+1; i++ {s += a[i]-a[i-k]}
				fmt.Println(s)
			},

			"D": func() {
				h, w := ScanInt(), ScanInt()
				a := make([]int, h*w)
				for i := 0; i < h*w; i++ {a[i] = ScanInt()}

				c := make([]int, h*w)
				var f func(x int) int
				f = func(x int) int {
					if c[x] != 0 {return c[x]}
					c[x] = 1
					i, j := Divmod(x, w)
					if i > 0 && a[x] > a[x-w] {c[x] += f(x-w)}
					if i < h-1 && a[x] > a[x+w] {c[x] += f(x+w)}
					if j > 0 && a[x] > a[x-1] {c[x] += f(x-1)}
					if j < w-1 && a[x] > a[x+1] {c[x] += f(x+1)}
					c[x] %= Mod
					return c[x]
				}
				s := 0
				for i := 0; i < h*w; i++ {s += f(i); s %= Mod}
				fmt.Println(s)

			},
		},

		"ABC038": contest{
			"A": func() {
				s := Scan()
				if s[len(s)-1] == 'T' {fmt.Println("YES")} else {fmt.Println("NO")}
			},

			"B": func() {
				var h1, w1, h2, w2 int
				fmt.Scan(&h1, &w1, &h2, &w2)
				ans := "NO"
				if h1==h2 || h1==w2 || w1==h2 || w1==w2 {ans = "YES"}
				fmt.Println(ans)
			},
			"C": func() {
				n := ScanInt()
				a := make([]int, n+1)
				for i := 0; i < n; i++ {a[i] = ScanInt()}


				tot := n
				cnt := 0
				prev := Inf
				for i := 0; i < n+1; i++ {
					if a[i] <= prev {tot += cnt*(cnt-1)/2; cnt=1} else {cnt++}
					prev = a[i]
				}
				fmt.Println(tot)
			},

			"D": func() {
				n := ScanInt()
				wh := make([][2]int, n)
				for i := 0; i < n; i++ {
					wh[i][0], wh[i][1] = ScanInt(), ScanInt()
				}
				sort.Slice(wh, func(i,j int) bool {
					if wh[i][0] == wh[j][0] {
						return wh[i][1] > wh[j][1]
					}
					return wh[i][0] < wh[j][0]
				})
				a := make([]int, n)
				for i := 0; i < n; i++ {a[i] = wh[i][1]}
				a = LIS(a)
				fmt.Println(BisectLeft(a, Inf))

			},
		},

		"ABC039": contest{
			"A": func() {
				var a, b, c int
				fmt.Scan(&a, &b, &c)
				fmt.Println(2*(a*b+b*c+c*a))
			},
			"B": func() {
				x := ScanInt()

				binarySearch := func() int {
					lo, hi := 1, 200
					for lo+1 < hi {
						n := (lo+hi)/2
						if Pow(n, 4) <= x {lo=n} else {hi=n}

					}
					return lo
				}
				fmt.Println(binarySearch())
			},

			"C": func() {
				board := strings.Repeat("WBWBWWBWBWBW", 3)
				conv := strings.Split("Do, *, Re, *, Mi, Fa, *, So, *, La, *, Si", ", ")
				s := Scan()
				fmt.Println(conv[strings.Index(board, s)])
			},

			"D": func() {
				h, w := ScanInt(), ScanInt()
				var s string
				for i := 0; i < h; i++ {s += Scan()}

				f := func(x int) (u, d, l, r int) {
					i, j := Divmod(x, w)
					if i > 0 {u = -w}
					if i < h-1 {d = w}
					if j > 0 {l = -1}
					if j < w-1 {r = 1}
					return
				}

				white := make([]bool, h*w)
				for i := 0; i < h*w; i++ {
					if s[i]=='#' {continue}
					u, d, l, r := f(i)
					for dy := u; dy < d+1; dy+=w {
						for dx := l; dx < r+1; dx++ {
							white[i+dy+dx] = true
						}
					}
				}
				black := make([]bool, h*w)
				for i := 0; i < h*w; i++ {
					if white[i]==true {continue}
					u, d, l, r := f(i)
					for dy := u; dy < d+1; dy+=w {
						for dx := l; dx < r+1; dx++ {
							black[i+dy+dx] = true
						}
					}
				}

				for i := 0; i < h*w; i++ {
					if s[i]=='#' && !black[i] {fmt.Println("impossible"); return}
				}
				fmt.Println("possible")
				for i := 0; i < h; i++ {
					row := make([]rune, w)
					for j := 0; j < w; j++ {
						if white[i*w+j] {row[j] = '.'} else {row[j] = '#' }
					}
					fmt.Println(string(row))
				}
			},
		},

		"ABC040": contest{
			"A": func() {
				n, x := ScanInt(), ScanInt()
				fmt.Println(MinInt(x-1, n-x))
			},

			"B": func() {
				n := ScanInt()

				res := Inf
				for i := 1; i*i <= n; i++ {
					j, r := Divmod(n, i)
					res = MinInt(res, j-i+r)
				}
				fmt.Println(res)


			},

			"C": func() {
				n := ScanInt()
				a := make([]int, n+1)
				for i := 1; i < n+1; i++ {a[i] = ScanInt()}
				a[0] = a[1]
				dp := make([]int, n+1)
				cost := func(i,j int) int {return dp[j]+AbsInt(a[i]-a[j])}
				for i := 2; i < n+1; i++ {
					dp[i] = MinInt(cost(i, i-2), cost(i, i-1))
				}
				fmt.Println(dp[n])
			},

			"D": func() {
				n, m := ScanInt(), ScanInt()
				uf := new(UnionFind); uf.Init(n)
				q := make([][3]int, 0)
				for i := 0; i < m; i++ {
					a, b, y := ScanInt(), ScanInt(), ScanInt(); a--; b--
					q = append(q, [3]int{2*y, a, b})
				}

				r := ScanInt()
				for i := 0; i < r; i++ {
					u, y := ScanInt(), ScanInt(); u--
					q = append(q, [3]int{2*y+1, u, i})
				}

				sort.SliceStable(q, func(i,j int) bool {return q[i][0] > q[j][0]})

				// fmt.Println(q)
				res := make([]int, r)
				for _, tmp := range q {
					y, i, j := tmp[0], tmp[1], tmp[2]
					if y&1==1 {res[j] = uf.size[uf.Find(i)]} else {uf.Unite(i, j)}
				}
				for _, i := range res {fmt.Println(i)}

			},
		},

		"ABC041": contest{
			"A": func() {
				s, i := Scan(), ScanInt()
				fmt.Println(string(s[i-1]))
			},

			"B": func() {
				var a, b, c int
				fmt.Scan(&a, &b, &c)
				fmt.Println(a*b%Mod*c%Mod)
			},

			"C": func() {
				n := ScanInt()
				a := make([][2]int, n)
				for i := 0; i < n; i++ {a[i][0], a[i][1] = i+1, ScanInt()}
				sort.Slice(a, func(i, j int) bool {return a[i][1] > a[j][1]})
				for i := 0; i < n; i++ {fmt.Println(a[i][0])}
			},

			"D": func() {
				n, m := ScanInt(), ScanInt()
				g := make([]int, n)
				for i := 0; i < m; i++ {
					x, y := ScanInt(), ScanInt(); x--; y--
					g[x] |= 1<<y
				}

				res := make([]int, 1<<n); res[0] = 1
				for i := 0; i < 1<<n; i++ {
					for j := 0; j < n; j++ {
						if i>>j&1==0 || g[j]&i!=0 {continue}
						res[i] += res[i&BitwiseNot(1<<j)]
					}
				}
				fmt.Println(res[1<<n-1])
			},
		},

		"ABC042": contest{
			"A": func() {
				const n = int(3)
				a := make([]int, n)
				for i := 0; i < n; i++ {a[i]= ScanInt()}
				sort.Slice(a, func(i, j int) bool {return a[i] < a[j]})
				ans := "NO"; if a[0]==5 && a[1]==5 && a[2]==7 {ans = "YES"}
				fmt.Println(ans)
			},

			"B": func() {
				n, _ := ScanInt(), ScanInt()
				s := make([]string, n)
				for i := 0; i < n; i++ {s[i] = Scan()}
				sort.Strings(s)
				fmt.Println(strings.Join(s, ""))
			},

			"C": func() {
				n, m := []rune(Scan()), ScanInt()
				n = append(make([]rune, 1), n...)

				d := make(map[rune]bool)
				for i := 0; i < m; i++ {d[[]rune(Scan())[0]] = true}
				l := len(n)

				a := make([]rune, l)
				flg := false
				for i := 1; i < l; i++ {
					if flg {
						for j := '0'; j <= '9'; j++ {if !d[j] {a[i] = j; break}}
					}	else {
						if !d[n[i]] {a[i] = n[i]; continue}
						for j := n[i]+1; j <= '9'; j++ {
							if !d[j] {a[i] = j; flg=true; break}
						}
						if flg {continue}
						for j := '0'; j < n[i]; j++ {if !d[j] {a[i] = j; break}}
						for k := i-1; k > 0; k-- {
							for j := n[k]+1; j <= '9'; j++ {
								if !d[j] {a[k] = j; flg=true; break}
							}
							if flg {break}
							for j := '0'; j < n[k]; j++ {if !d[j] {a[k] = j; break}}
						}
						if flg {continue}
						for j := '1'; j <= '9'; j++ {if !d[j] {a[0] = j; flg=true; break}}
					}
				}

				if a[0]==0 {fmt.Println(string(a[1:]))} else {fmt.Println(string(a))}
			},

			"D": func() {
				var h, w, a, b int
				fmt.Scan(&h, &w, &a, &b)
				cn := Combinatorics{}; cn.Init(2e5, Mod)
				ng := 0
				for i := 0; i < a; i++ {
					ng += cn.ChooseMod(b-1+h-1-i, b-1) * cn.ChooseMod(i+w-1-b, i)
					ng %= Mod
				}
				fmt.Println(((cn.ChooseMod(h+w-2, h-1)-ng)%Mod+Mod)%Mod)

			},
		},

		"ABC043": contest{
			"A": func() {
				n := ScanInt()
				fmt.Println((1+n)*n/2)
			},

			"B": func() {
				s := Scan()

				t := ""
				for _, c := range s {
					if c!='B' {t += string(c); continue}
					if len(t)==0 {continue}
					t = t[:len(t)-1]
				}
				fmt.Println(t)
			},

			"C": func() {
				n := ScanInt()
				a := make([]int, n)
				for i := 0; i < n; i++ {a[i] = ScanInt()}
				m := int(math.Round(float64(SumInt(a...))/float64(n)))
				tot := 0
				for _, x := range a {tot += Pow(m-x, 2)}
				fmt.Println(tot)

			},

			"D": func() {
				s := Scan()
				n := len(s)
				for i := 0; i < n-1; i++ {
					if s[i]==s[i+1] {fmt.Println(i+1, i+2); return}
				}
				for i := 1; i < n-1; i++ {
					if s[i-1]==s[i+1] {fmt.Println(i, i+2); return}
				}
				fmt.Println(-1, -1)
			},
		},

		"ABC044": contest{
			"A": func() {
				var n, k, x, y int
				fmt.Scan(&n, &k, &x, &y)
				fmt.Println(MinInt(n,k)*x + MaxInt(0,n-k)*y)
			},

			"B": func() {
				s := Scan()
				cnt := make(map[rune]int)
				for _, c := range s {cnt[c] ^= 1}
				for _, v := range cnt {
					if v==1 {fmt.Println("No"); return}
				}
				fmt.Println("Yes")
			},

			"C": func() {
				n, a := ScanInt(), ScanInt()
				x := make([]int, n)
				for i := 0; i < n; i++ {x[i] = ScanInt()}
				dp := make([][]int, n+1)
				for i := 0; i < n+1; i++ {dp[i] = make([]int, 2501)}
				dp[0][0] = 1
				for _, v := range x {
					for i := n; i > 0; i-- {
						for j := v; j < 2501; j++ {
							dp[i][j] += dp[i-1][j-v]
						}
					}
				}
				s := 0
				for i := 1; i < n+1; i++ {s += dp[i][i*a]}
				fmt.Println(s)
			},
		},


		"ABC045": contest{
			"A": func() {
				var a, b, h int
				fmt.Scan(&a, &b, &h)
				fmt.Println((a+b)*h/2)
			},

			"B": func() {
				var a, b, c string
				fmt.Scan(&a, &b, &c)
				d := make(map[rune][]rune);
				d['a'] = []rune(ReversedString(a))
				d['b'] = []rune(ReversedString(b))
				d['c'] = []rune(ReversedString(c))
				nx := 'a';
				for {
					l := len(d[nx])
					if l==0 {fmt.Printf("%c\n", unicode.ToUpper(nx)); return}
					d[nx], nx = d[nx][:l-1], d[nx][l-1]
				}
			},

			"C": func() {
				s := Scan(); l := len(s)

				tot := 0
				c := func(l int) int {return 1<<MaxInt(0,l-1)}
				for i := 0; i < l; i++ {
					for j := i; j < l; j++ {
						n, _ := strconv.Atoi(s[i:j+1])
						tot += n * c(i) * c(l-1-j)
					}
				}
				fmt.Println(tot)
			},

			"D": func() {
				var h, w, n int
				fmt.Scan(&h, &w, &n)
				cnt := make(map[[2]int]int)
				for k := 0; k < n; k++ {
					y, x := ScanInt()-1, ScanInt()-1
					for dy := -1; dy < 2; dy++ {
						for dx := -1; dx < 2; dx++ {
							i, j := y+dy, x+dx
							if !(0<i && i<h-1 && 0<j && j<w-1) {continue}
							cnt[[2]int{i,j}]++
						}
					}
				}
				var res [10]int; res[0] = (h-2)*(w-2)
				for _, c := range cnt {res[c]++; res[0]--}
				for i := 0; i < 10; i++ {fmt.Println(res[i])}
			},
		},

		"ABC046": contest{
			"A": func() {
				s := make(map[int]bool)
				for i := 0; i < 3; i++ {
					s[ScanInt()] = true
				}
				fmt.Println(len(s))
			},

			"B": func() {
				n, k := ScanInt(), ScanInt()
				fmt.Println(k*Pow(k-1, n-1))
			},
			"C": func() {
				n := ScanInt()
				x, y := 1, 1
				for i := 0; i < n; i++ {
					a, b := ScanInt(), ScanInt()
					m := MaxInt((x+a-1)/a, (y+b-1)/b)
					x, y = a*m, b*m
				}
				fmt.Println(x+y)
			},

			"D": func() {
				s := Scan()
				c := 0
				for i := 0; i < len(s); i++ {c += Booltoi(s[i]=='p')}
				fmt.Println(len(s)/2 - c)
			},
		},

		"ABC047": contest{
			"A": func() {
				a := make([]int, 3)
				for i := 0; i < 3; i++ {a[i] = ScanInt()}
				sort.Ints(a)
				if a[0]+a[1]==a[2] {fmt.Println("Yes")} else {fmt.Println("No")}
			},

			"B": func() {
				var w, h, n int
				fmt.Scan(&w, &h, &n)

				l, r, u, d := 0, w, h, 0
				for i := 0; i < n; i++ {
					x, y, a := ScanInt(), ScanInt(), ScanInt()
					switch a {
					case 1: l = MaxInt(l, x)
					case 2: r = MinInt(r, x)
					case 3: d = MaxInt(d, y)
					case 4: u = MinInt(u, y)
					}
				}
				fmt.Println(MaxInt(0,r-l)*MaxInt(0,u-d))
			},

			"C": func() {
				s := Scan()
				c := 0
				for i := 0; i < len(s)-1; i++ {c += Booltoi(s[i]!=s[i+1])}
				fmt.Println(c)
			},

			"D": func() {
				n, _ := ScanInt(), ScanInt()
				a := make([]int, n)
				for i := 0; i < n; i++ {a[i] = ScanInt()}
				mx := 0
				mn := a[0]
				cnt := 0
				for i := 1; i < n; i++ {
					d := a[i] - mn
					if d > mx {mx, cnt = d, 1} else if d == mx {cnt++}
					mn = MinInt(mn, a[i])
				}
				fmt.Println(cnt)
			},
		},

		"ABC048": contest{
			"A": func() {
				s := make([]byte, 3)
				for i := 0; i < 3; i++ { s[i] = Scan()[0]}
				fmt.Println(string(s))
			},

			"B": func() {
				a, b, x := ScanInt(), ScanInt(), ScanInt()
				f := func(n int) int {if n==-1 {return -1}; return n/x}
				fmt.Println(f(b)-f(a-1))
			},

			"C": func() {
				n, x := ScanInt(), ScanInt()
				a := make([]int, n+1)
				for i := 0; i < n; i++ {a[i+1] = ScanInt()}
				c := 0
				for i := 1; i < n+1; i++ {
					d := a[i-1]+a[i]-x
					if d <= 0 {continue}
					a[i] -= d; c += d
				}
				fmt.Println(c)

			},

			"D": func() {
				s := Scan()
				l := len(s)
				ans := "First"
				if  ((l&1) ^ Booltoi(s[0]==s[l-1])) == 0 {ans = "Second"}
				fmt.Println(ans)
			},
		},

		"ABC049": contest{
			"A": func() {
				vowel := make(map[rune]bool)
				for _, c := range "aeiou" {vowel[c] = true}
				c := Scan()
				if vowel[[]rune(c)[0]] {fmt.Println("vowel")} else {fmt.Println("consonant")}
			},

			"B": func() {
				h, _ := ScanInt(), ScanInt()
				for i := 0; i < h; i++ {
					s := Scan()
					for i := 0; i < 2; i++ {fmt.Println(s)}
				}

			},

			"C": func() {
				s := Scan()
				c := map[string]bool{
					"dream": true,
					"dreamer": true,
					"erase": true,
					"eraser": true,
				}

				for len(s)>0 {
					l := len(s)
					if c[s[l-5:]] {
						s = s[:l-5]
					} else if c[s[l-6:]] {
						s = s[:l-6]
					} else if c[s[l-7:]]{
						s = s[:l-7]
					} else {
						fmt.Println("NO"); return
					}
				}
				fmt.Println("YES")
			},

			"D": func() {
				var n, k, l int
				fmt.Scan(&n, &k, &l)
				uf1 := new(UnionFind); uf1.Init(n)
				uf2 := new(UnionFind); uf2.Init(n)
				for i := 0; i < k; i++ {
					uf1.Unite(ScanInt()-1, ScanInt()-1)
				}
				for i := 0; i < l; i++ {
					uf2.Unite(ScanInt()-1, ScanInt()-1)
				}
				c := make(map[[2]int]int)
				for i := 0; i < n; i++ {
					c[[2]int{uf1.Find(i), uf2.Find(i)}]++
				}
				a := make([]int, n)
				for i := 0; i < n; i++ {a[i] = c[[2]int{uf1.Find(i), uf2.Find(i)}]}
				fmt.Fprintln(writer, strings.Trim(fmt.Sprint(a), "[]"))
				writer.Flush()

			},
		},

		"ABC050": contest{
			"A": func() {
				a, op, b := ScanInt(), Scan(), ScanInt()
				if op=="+" {fmt.Println(a+b)} else {fmt.Println(a-b)}
			},
		},


		"ABC179": contest{
			"D": func() {
				mod := 998244353
				var n, k int; fmt.Scan(&n, &k);
				l, r := make([]int, k), make([]int, k);
				for i := 0; i < k; i++ {l[i], r[i] = ScanInt(), ScanInt()};
				s := make([]int, n*2); s[0], s[1] = 1, -1;
				for i := 0; i < n-1; i++ {
					s[i+1] = (s[i+1]+s[i])%mod;
					for j := 0; j < k; j++ {
						s[i+l[j]] = (s[i+l[j]]+s[i])%mod;
						s[i+r[j]+1] = ((s[i+r[j]+1]-s[i])%mod+mod)%mod;
					}
				}
				fmt.Println(s[n-1]);
			},

			"E": func() {
				var n, x, m int; fmt.Scan(&n, &x, &m)
				res := make([]int, m); for i := 0; i < m; i++ {res[i] = -1}
				s := 0;
				loop := make([]int, m)
				for i := 0; i < m+1; i++ {
					if i==n {fmt.Println(s); return}
					if res[x] != -1 {
						l := i-res[x]
						loop = loop[res[x]:i]
						q, r := Divmod(n-i, l)
						fmt.Println(s+q*SumInt(loop...)+SumInt(loop[:r]...)); return
					}
					res[x], loop[i] = i, x;
					s += x; x = x*x%m
				}
			},
		},

		"ABC180": contest{
			"A": func() {
				var n, a, b int; fmt.Scan(&n, &a, &b)
				fmt.Println(n-a+b)
			},

			"B": func() {
				n := ScanInt()
				x := make([]int, n)
				for i := 0; i < n; i++ {x[i] = AbsInt(ScanInt())}
				fmt.Println(SumInt(x...))
				d := 0
				for i := 0; i < n; i++ {d += x[i]*x[i]}
				fmt.Println(NthRoot(float64(d), 2))

				fmt.Println(MaxInt(x...))
			},

			"C": func() {
				n := ScanInt()
				div := FindDivisors(n);
				for _, d := range div {fmt.Fprintln(writer, d)}
				writer.Flush()
			},

			"D": func() {
				var x, y, a, b int
				fmt.Scan(&x, &y, &a, &b)
				cnt := 0
				for {
					if y/a < x {break}
					if x*a >= y {break}
					if x*a > x+b {break}
					x *= a; cnt++
				}
				fmt.Println(cnt+(y-x-1)/b)
			},

			"E": func() {
				n := ScanInt()
				x, y, z := make([]int, n), make([]int, n), make([]int, n)
				for i := 0; i < n; i++ {
					x[i], y[i], z[i] = ScanInt(), ScanInt(), ScanInt()
				}
				dist := make([][]int, n); for i := 0; i < n; i++ {dist[i] = make([]int, n)}
				for i := 0; i < n; i++ {
					for j := 0; j < n; j++ {
						dist[i][j] = AbsInt(x[j]-x[i])+AbsInt(y[j]-y[i])+MaxInt(0, z[j]-z[i])
					}
				}
				dp := make([][]int, 1<<n);
				for i := 0; i < 1<<n; i++ {
					dp[i] = make([]int, n)
					for j := 0; j < n; j++ {
						dp[i][j] = Inf
					}
				}
				dp[0][0] = 0;
				for s := 0; s < 1<<n; s++ {
					for i := 0; i < n; i++ {
						for t,j := s|1<<i,0; j < n; j++ {dp[t][i] = MinInt(dp[t][i], dp[s][j]+dist[j][i])}
					}
				}
				fmt.Println(dp[1<<n-1][0])
			},

			"F": func() {
				var n, m, l int; fmt.Scan(&n, &m, &l)
				cn := Combinatorics{}; cn.Init(n, Mod)
				path, cycle := make([]int, n+1), make([]int, n+1)
				path[1], path[2] = 1, 1
				for i := 3; i < n+1; i++ {path[i] = path[i-1]*i%Mod}
				for i := 2; i < n+1; i++ {cycle[i] = path[i-1]}

				f := func (l int) int {
					dp := make([][]int, n+1)
					for i := 0; i < n+1; i++ {dp[i] = make([]int, m+1)}
					dp[0][0] = 1
					for  i := 0; i < n; i++ {
						for j := 0; j < m+1; j++ {
							for k := 1; k <= MinInt(l, n-i, m-j+1); k++ {
								dp[i+k][j+k-1] += dp[i][j]*cn.ChooseMod(n-i-1, k-1)%Mod*path[k]%Mod
								dp[i+k][j+k-1] %= Mod
							}
							for k := 2; k <= MinInt(l, n-i, m-j); k++ {
								dp[i+k][j+k] += dp[i][j]*cn.ChooseMod(n-i-1, k-1)%Mod*cycle[k]%Mod
								dp[i+k][j+k] %= Mod
							}
						}
					}
					return dp[n][m]
				}
				fmt.Println(((f(l)-f(l-1))%Mod+Mod)%Mod)
			},
		},
	},
}



func main() {
	scanner.Buffer([]byte{}, Inf)
	scanner.Split(bufio.ScanWords)

	AtCoder.contests["ABC050"]["A"]()

}
