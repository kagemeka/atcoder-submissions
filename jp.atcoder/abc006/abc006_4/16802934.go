package main

import (
	"fmt"
	"bufio"
	"os"
	"sort"
	"strconv"
	"strings"
	"math"
)



type contest map[string]func()
type proconSite struct {
	contests map[string]contest
	problems map[string]func()
}

type RuneSlice []rune
func (p RuneSlice) Len() int { return len(p) }
func (p RuneSlice) Less(i, j int) bool { return p[i] < p[j] }
func (p RuneSlice) Swap(i, j int) {p[i], p[j] = p[j], p[i]}

type ByteSlice []byte
func (p ByteSlice) Len() int { return len(p) }
func (p ByteSlice) Less(i, j int) bool { return p[i] < p[j] }
func (p ByteSlice) Swap(i, j int) {p[i], p[j] = p[j], p[i]}

type PairInt struct{
	x, y int
}

type PairIntSlice []PairInt



func ReversedString(s string) (t string) {
	for _, c := range s {t = string(c) + t}
	return
}
func AbsInt(x int) int {if x < 0 {x *= -1}; return x}
func AbsFloat(x float64) float64 {if x < 0 {x *= -1}; return x}
func MaxInt(a ...int) int {m := a[0]; for _, x := range a {if x > m {m = x}}; return m}
func MinInt(a ...int) int {m := a[0]; for _, x := range a {if x < m {m = x}}; return m}
func Divmod(a, b int) (int, int) {return a / b, a % b}
func Gcd(a, b int) int {if (b == 0) {return AbsInt(a)}; return Gcd(b, a % b)}
func Lcm(a, b int) int {return AbsInt(a / Gcd(a, b) * b)}
func BisectLeft(a []int, x int) int {
	return sort.SearchInts(a, x)
}

func BisectRight(a []int, x int) int {
	return sort.Search(len(a), func(i int) bool {return a[i] > x})
}



var scanner = bufio.NewScanner(os.Stdin)
var reader = bufio.NewReader(os.Stdin)


var atCoder = proconSite{
	contests: map[string]contest{
		"ABC001": contest{
			"A": func() {
				var a, b int; fmt.Scan(&a, &b)
				fmt.Println(a - b)
			},

			"B": func() {

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
					a -= 1; b -= 1
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
							cnt += 1
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
					n -= 1
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
					fmt.Scan(&c[i])
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


	},
}


func main() {
	atCoder.contests["ABC006"]["D"]()
}

// sort := func(ps PairIntSlice) {
// 	sort.SliceStable(ps, func(i, j int) bool {
// 		return ps[i].x < ps[j].x
// 	})
// }
