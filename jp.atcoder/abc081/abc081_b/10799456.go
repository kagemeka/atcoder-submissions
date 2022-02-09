package main

import (
	"fmt"
)

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}
func main() {
	var n int
	fmt.Scan(&n)

	res := 1000000000
	for i := 0; i < n; i++ {
		var a int
		fmt.Scan(&a)

		var cnt int = 0
		for a&1 == 0 {
			a /= 2
			cnt++
		}
		res = min(res, cnt)
	}
	fmt.Println(res)
}
