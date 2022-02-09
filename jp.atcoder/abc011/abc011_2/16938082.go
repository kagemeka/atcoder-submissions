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

// Edge .
type Edge struct{cap, weight int}
// Graph .
type Graph struct{
	n int
	edges map[int]map[int]*Edge
	level []int
}
// InitLevel .
func (g *Graph) InitLevel() {
	g.level = make([]int, g.n)
	for i := 0; i < g.n; i++ {
		g.level[i] = -1
	}
}

// Init .
func (g *Graph) Init(n int) {
	g.n = n
	g.edges = make(map[int]map[int]*Edge)
	g.level = make([]int, n)
	for i := 0; i < n; i++ {
		g.edges[i] = make(map[int]*Edge)
		g.level[i] = -1
	}
}

// MaximumFlowDinic .
func (g *Graph) MaximumFlowDinic(s, t int) int {
	bfs := func() {
		g.InitLevel()
		g.level[s] = 0
		q := []int{s}
		for len(q) > 0 {
			u := q[0]; q = q[1:]
			for v, edge := range g.edges[u] {
				if edge.cap == 0 {continue}
				if g.level[v] >= 0 {continue}
				g.level[v] = g.level[u]+1
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
			if g.level[v] <= g.level[u] {continue}
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
		if g.level[t] == -1 {return flow}
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
		},


	},
}


func main() {
	AtCoder.contests["ABC011"]["B"]()

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
