package main

import (
	"fmt"
	"bufio"
	"os"
	"sort"
	"strconv"
	"strings"
	"math"
	"container/heap"
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
// PairStringInt .
type PairStringInt struct{S string; I int}

// ReversedString .
func ReversedString(s string) (t string) { for _, c := range s {t = string(c) + t}; return}
// AbsInt .
func AbsInt(x int) int {if x < 0 {x *= -1}; return x}
// AbsFloat .
func AbsFloat(x float64) float64 {if x < 0 {x *= -1}; return x}
// MaxInt .
func MaxInt(a ...int) int {m := a[0]; for _, x := range a {if x > m {m = x}}; return m}
// MinInt .
func MinInt(a ...int) int {m := a[0]; for _, x := range a {if x < m {m = x}}; return m}
// Divmod .
func Divmod(a, b int) (int, int) {return a / b, a % b}
// Gcd .
func Gcd(a, b int) int {if (b == 0) {return AbsInt(a)}; return Gcd(b, a % b)}
// Lcm .
func Lcm(a, b int) int {return AbsInt(a / Gcd(a, b) * b)}
// BisectLeft .
func BisectLeft(a []int, x int) int { return sort.SearchInts(a, x) }
// BisectRight .
func BisectRight(a []int, x int) int {return sort.Search(len(a), func(i int) bool {return a[i] > x})}
// Booltoi .
func Booltoi(b bool) int { if b {return 1}; return 0}
// GetBitLength .
func GetBitLength(x int) int {return int(math.Floor(math.Log2(float64(x)))+1)}


// Edge .
type Edge struct{cap, weight int}
// Graph .
type Graph struct{
	size int
	edges map[int]map[int]*Edge
	depth []int // only tree
	dist []int // only tree
	ancestors [][]int // only tree


}

// Init .
func (g *Graph) Init(n int) {
	g.size = n
	g.edges = make(map[int]map[int]*Edge)
	for i := 0; i < n; i++ {
		g.edges[i] = make(map[int]*Edge)
	}
}

// AddEdge .
func (g *Graph) AddEdge(u, v int, e *Edge) {
	if g.edges[u] == nil { g.edges[u] = make(map[int]*Edge)}
	g.edges[u][v] = e
}

// InitRoot of Tree.
func (g *Graph) InitRoot(root int) {
	n := g.size
	g.depth = make([]int, n)
	g.dist = make([]int, n)
	g.ancestors = make([][]int, 1)
	g.ancestors[0] = make([]int, n)
	g.ancestors[0][root] = root

	stack := []int{root}
	for len(stack) > 0 {
		u := stack[len(stack)-1]; stack = stack[:len(stack)-1]
		for v, edge := range g.edges[u] {
			if v == g.ancestors[0][u] {continue}
			g.depth[v] = g.depth[u] + 1
			g.dist[v] = g.dist[u] + edge.weight
			g.ancestors[0][v] = u
			stack = append(stack, v)
		}
	}
}

// FindAncestors . Doubling
func (g *Graph) FindAncestors() {
	n := g.size
	for i := 0; i < GetBitLength(MaxInt(g.depth...)); i++ {
		ancestor := g.ancestors[len(g.ancestors)-1]
		nxtAncestor := make([]int, n)
		for i := 0; i < n; i++ {
			nxtAncestor[i] = ancestor[ancestor[i]]
		}
		g.ancestors = append(g.ancestors, nxtAncestor)
	}
}

// FindDist . only tree
func (g *Graph) FindDist(u, v int) int {
	lca := g.FindLCA(u, v)
	return g.depth[u] + g.depth[v] - 2*g.depth[lca]
}

// FindLCA .
func (g *Graph) FindLCA(u, v int) int {
	du, dv := g.depth[u], g.depth[v]
	if du > dv {
		u, v = v, u
		du, dv = dv, du
	}
	d := dv - du
	for i := 0; i < GetBitLength(d); i++ {
		if d>>i & 1 == 1 {v = g.ancestors[i][v]}
	}
	if v == u {return u}
	for i := GetBitLength(du)-1; i > -1; i-- {
		nu, nv := g.ancestors[i][u], g.ancestors[i][v]
		if nu == nv {continue}
		u, v = nu, nv
	}
	return g.ancestors[0][u]
}

// FloydWarshall .
func (g *Graph) FloydWarshall() (*[][]int) {
	n := g.size
	shortestPath := make([][]int, n)
	for i := 0; i < n; i++ {
		shortestPath[i] = make([]int, n)
		for j := 0; j < n; j++ {
			shortestPath[i][j] = 1001001001001001
		}
	}
	for i := 0; i < n; i++ {
		shortestPath[i][i] = 0
	}
	for i, tmp := range g.edges {
		for j, edge := range tmp {
			shortestPath[i][j] = edge.weight
		}
	}
	for k := 0; k < n; k++ {
		for i := 0; i < n; i++ {
			for j := 0; j < n; j++ {
				shortestPath[i][j] = MinInt(
					shortestPath[i][j],
					shortestPath[i][k] + shortestPath[k][j],
				)
			}
		}
	}
	return &shortestPath

}

// MaximumFlowDinic .
func (g *Graph) MaximumFlowDinic(s, t int) int {
	var level []int
	n := g.size
	initLevel := func() {
		level = make([]int, n)
		for i := 0; i < n; i++ {level[i] = -1}
		level[s] = 0
	}
	bfs := func() {
		initLevel()
		q := []int{s}
		for len(q) > 0 {
			u := q[0]; q = q[1:]
			for v, edge := range g.edges[u] {
				if edge.cap == 0 {continue}
				if level[v] >= 0 {continue}
				level[v] = level[u]+1
				q = append(q, v)
			}
		}
	}
	var flowToSink func(u, flowIn int) int
	flowToSink = func(u, flowIn int) int {
		if u == t {return flowIn}
		flow := 0
		for v, edge := range g.edges[u] {
			if edge.cap == 0 {continue}
			if level[v] <= level[u] {continue}
			f := flowToSink(v, MinInt(flowIn, edge.cap))
			if f == 0 {continue}
			g.edges[u][v].cap -= f
			g.edges[v][u].cap += f
			flowIn -= f
			flow += f
		}
		return flow
	}
	flow := 0
	for {
		bfs()
		if level[t] == -1 {return flow}
		flow += flowToSink(s, math.MaxInt64)
	}
}


const (
	// Mod .
	Mod = 1e9 + 7
	// Eps .
	Eps = 1e-13
)

var scanner = bufio.NewScanner(os.Stdin)
var reader = bufio.NewReader(os.Stdin)

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
				triangleArea := func(x0, y0, x1, y1, x2, y2 float64) float64 {
					x1 -= x0; x2 -= x0; y1 -= y0; y2 -= y0
					return AbsFloat(x1*y2 - x2*y1) / 2
				}
				var x0, y0, x1, y1, x2, y2 float64
				fmt.Scan(&x0, &y0, &x1, &y1, &x2, &y2)
				fmt.Println(triangleArea(x0, y0, x1, y1, x2, y2))

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
					s := 0
					t := (1<<n) - 1
					for j := 0; j < n; j++ {
						if i>>j&1 == 1 {
							cnt++
							s |= 1<<j
							t &= relations[j] | 1<<j
						}
						if t&s == s {
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
				var m = 10007
				t := []int{0, 0, 1}
				for i := 0; i < n; i++ {
					l := len(t)
					t = append(t, t[l-3]+t[l-2]+t[l-1])
					t[l] %= m
				}
				fmt.Println(t[n-1])

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
				count := func(d int) (cnt int) {
					if d < 4 {
						cnt = d
					} else if d == 4 {
						cnt = 4
					} else if d < 9 {
						cnt = d - 1
					} else {
						cnt = 8
					}
					return cnt
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

				var res []PairStringInt
				for name, cnt := range numVotes {
					res = append(res, PairStringInt{name, cnt})
				}

				sortFunc := func(p []PairStringInt) {
					sort.SliceStable(p, func(i, j int) bool {
						return p[i].I > p[j].I
					})
				}
				sortFunc(res)
				fmt.Println(res[0].S)
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
				type coordinate struct {
					x, y int
				}
				type rectangle struct {
					x1, y1, x2, y2 int
				}

				xy := make([]coordinate, n)
				for i := 0; i < n; i++ {
					var x, y int
					fmt.Scan(&x, &y)
					xy[i] = coordinate{x, y}
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


				bitwiseDot := func(a, b [][]int) [][]int {
					h, w := len(a), len(b[0])
					c := make([][]int, h)
					for i := 0; i < h; i++ {
						c[i] = make([]int, w)
						for j := 0; j < w; j++ {
							for k := 0; k < len(b); k++ {
								c[i][j] ^= a[i][k] & b[k][j]
							}
						}
					}
					return c
				}

				var bitwiseMatPow func(a [][]int, n int) [][]int
				bitwiseMatPow = func(a [][]int, n int) [][]int {
					res := make([][]int, k)
					for i := 0; i < k; i++ {
						res[i] = make([]int, k)
						res[i][i] = mask
					}
					if n == 0 {return res}
					res = bitwiseMatPow(a, n/2)
					res = bitwiseDot(res, res)
					if n&1 == 1 {res = bitwiseDot(res, a)}
					return res
				}

				if m <= k {fmt.Println(a[m-1]); return}
				b := make([][]int, k)
				for i := 0; i < k; i++ {
					b[i] = []int{a[k-1-i]}
				}
				fmt.Println(bitwiseDot(bitwiseMatPow(d, m-k), b)[0][0])

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
				var n, g, e int
				fmt.Scan(&n, &g, &e)
				var graph *Graph = &Graph{}
				graph.Init(n+1)

				for i := 0; i < g; i++ {
					var p int
					fmt.Scan(&p)
					graph.edges[p][n] = &Edge{}
					graph.edges[n][p] = &Edge{}
					graph.edges[p][n].cap++
				}

				for i := 0; i < e; i++ {
					var a, b int
					fmt.Scan(&a, &b)
					graph.edges[a][b] = &Edge{}
					graph.edges[b][a] = &Edge{}
					graph.edges[a][b].cap++
					graph.edges[b][a].cap++
				}
				fmt.Println(graph.MaximumFlowDinic(0, n))
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
				g := &Graph{}; g.Init(n)
				for i := 0; i < m; i++ {
					l := make([]int, 3)
					for j := 0; j < 3; j++ {
						scanner.Scan()
						v, _ := strconv.Atoi(scanner.Text())
						l[j] = v
					}

					a, b, t := l[0], l[1], l[2]
					a--; b--
					g.AddEdge(a, b, &Edge{weight: t})
					g.AddEdge(b, a, &Edge{weight: t})
				}
				shortestPath := *g.FloydWarshall()

				maxDist := make([]int, n)
				for i := 0; i < n; i++ {
					for j := 0; j < n; j++ {
						maxDist[i] = MaxInt(maxDist[i], shortestPath[i][j])
					}
				}
				fmt.Println(MinInt(maxDist...))

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
				for i := 0; i < m; i++ {
					a[i] = ScanInt()
				}
				res := make([]int, n)
				for i := 0; i < n; i++ {res[i] = i}

				swap := func(i, j int) {
					res[i], res[j] = res[j], res[i]
				}
				for i := m-1; i > -1; i-- {
					swap(a[i]-1, a[i])
				}

				group := make([][]int, n)
				root := make([]int, n)
				for i := 0; i < n; i++ {root[i] = -1}
				indexInGroup := make([]int, n)
				for i := 0; i < n; i++ {indexInGroup[i] = -1}

				for i := 0; i < n; i++ {
					if root[i] != -1 { continue}
					j := i
					for c := 0; c < n; c++ {
						group[i] = append(group[i], j)
						root[j] = i
						indexInGroup[j] = c
						j = res[j]
						if j == i {break}
					}
				}
				for i := 0; i < n; i++ {
					g := group[root[i]]
					fmt.Println(g[(indexInGroup[i]+d)%len(g)] + 1)
				}
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
				graph := Graph{}
				graph.Init(n)
				for i := 0; i < n-1; i++ {
					x, y := ScanInt(), ScanInt()
					x--; y--
					graph.AddEdge(x, y, &Edge{weight: 1})
					graph.AddEdge(y, x, &Edge{weight: 1})
				}
				graph.InitRoot(0)
				graph.FindAncestors()
				q := ScanInt()
				for i := 0; i < q; i++ {
					a, b := ScanInt(), ScanInt()
					a--; b--
					fmt.Println(graph.FindDist(a, b) + 1)
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
				var w, n, k int
				fmt.Scan(&w, &n, &k)
				a, b := make([]int, n), make([]int, n)
				for i := 0; i < n; i++ {
					a[i] = ScanInt()
					b[i] = ScanInt()
				}

				dp := make([][][]int, n+1)
				for i := 0; i < n+1; i++ {
					dp[i] = make([][]int, k+1)
					for j := 0; j < k+1; j++ {
						dp[i][j] = make([]int, w+1)
					}
				}

				for i := 0; i < n; i++ {
					for j := k; j > -1; j-- {
						for l := 0; l < w+1; l++ {
							dp[i+1][j][l] = dp[i][j][l]
							if j == 0 || l < a[i] {continue}
							dp[i+1][j][l] = MaxInt(dp[i+1][j][l], dp[i][j-1][l-a[i]]+b[i])

						}
					}
				}
				fmt.Println(dp[n][k][w])
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

		},



	},
}


func main() {
	scanner.Split(bufio.ScanWords)
	AtCoder.contests["ABC016"]["B"]()

}


// change "Item, Less" according to problems.
// ABC009 C

// Item .
type Item struct { char rune; cost, index int }
// Heap .
type Heap []*Item

func(h Heap) Len() int {return len(h)}
func(h Heap) Swap(i, j int) {h[i], h[j] = h[j], h[i]}
func(h Heap) Less(i, j int) bool {
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
