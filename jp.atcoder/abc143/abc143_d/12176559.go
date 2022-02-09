package main

import (
	"fmt"
	"sort"
)

func maxInt(a ...int) int {m := a[0]; for _, x := range a {if x > m {m = x}}; return m}
func minInt(a ...int) int {m := a[0]; for _, x := range a {if x < m {m = x}}; return m}

func main() {
	var n int; fmt.Scan(&n)
	l := make([]int, n)
	for i := 0; i < n; i++ {fmt.Scan(&l[i])}
	sort.Ints(l)

	cnt := 0
	for i := 0; i < n - 2; i++ {
		for j := i + 1; j < n - 1; j++ {
			k := sort.SearchInts(l, l[i] + l[j]) - 1
			cnt += maxInt(0, k - j)
		}
	}
	fmt.Println(cnt)
}
