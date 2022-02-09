package main

import (
	"fmt"
	"bufio"
	"os"
)



type contest map[string]func()
type proconSite struct {
	contests map[string]contest
	problems map[string]func()
}

func absInt(x int) int {if x < 0 {x *= -1}; return x}
func absFloat(x float64) float64 {if x < 0 {x *= -1}; return x}
func maxInt(a ...int) int {m := a[0]; for _, x := range a {if x > m {m = x}}; return m}
func minInt(a ...int) int {m := a[0]; for _, x := range a {if x < m {m = x}}; return m}



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
				fmt.Println(maxInt(x, y))
			},

			"B": func() {
				var vowels = make(map[rune]bool)
				for _, c := range "aeiou" {
					vowels[c] = true
				}
				var s string; fmt.Scan(&s)
				var t string
				for _, c := range s {
					if _, has := vowels[c]; !has {t += string(c)}
				}
				fmt.Println(t)
			},

			"C": func() {
				triangleArea := func(x0, y0, x1, y1, x2, y2 float64) float64 {
					x1 -= x0; x2 -= x0; y1 -= y0; y2 -= y0
					return absFloat(x1*y2 - x2*y1) / 2
				}
				var x0, y0, x1, y1, x2, y2 float64
				fmt.Scan(&x0, &y0, &x1, &y1, &x2, &y2)
				fmt.Println(triangleArea(x0, y0, x1, y1, x2, y2))

			},

			"D": func() {

			},

		},


	},
}


func main() {
	atCoder.contests["ABC002"]["C"]()
}
