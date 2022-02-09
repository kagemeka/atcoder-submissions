package main

import (
	"fmt"
	"sort"
)
func maxInt(a ...int) int {m := a[0]; for _, x := range a {if x > m {m = x}}; return m}
func minInt(a ...int) int {m := a[0]; for _, x := range a {if x < m {m = x}}; return m}

func main() {
	var s string; var k int
	fmt.Scan(&s, &k)

	n := len(s)
	res := make(map[string]bool)
	for i := 0; i < n; i++ {
		for j := 1; j < minInt(k, n - i) + 1; j++ {
			res[string(s[i:i+j])] = true
		}
	}
	a := make([]string, len(res))
	i := 0
	for t := range res {
		a[i] = t; i++
	}
	sort.Strings(a)
	fmt.Println(a[k-1])
}
