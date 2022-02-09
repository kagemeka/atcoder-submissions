package main

import (
	"fmt"
)

func main() {
	var n, k int; fmt.Scan(&n, &k)
	a := make([]int, n)
	for i := 0; i < n; i++ {fmt.Scan(&a[i])}
	l := 0
	s := 0
	cnt := 0
	for r := 0; r < n; r++ {
		s += a[r]
		for s >= k {
			cnt += n - r
			s -= a[l]
			l++
		}
	}
	fmt.Println(cnt)
}
