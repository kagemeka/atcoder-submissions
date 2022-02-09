package main

import (
	"fmt"
	"bufio"
	"os"
	"sort"
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

		},


	},
}


func main() {
	atCoder.contests["ABC005"]["A"]()
}

// sort := func(ps PairIntSlice) {
// 	sort.SliceStable(ps, func(i, j int) bool {
// 		return ps[i].x < ps[j].x
// 	})
// }
