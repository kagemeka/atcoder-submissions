package main

import (
	"fmt"
)

func main() {
	var n, a, b, k int; fmt.Scan(&n, &a, &b, &k)
	res := make(map[int]bool)
	res[a], res[b] = true, true
	for i := 0; i < k; i++ {
		var p int; fmt.Scan(&p)
		res[p] = true
	}
	ans := "NO"; if len(res) == k + 2 {ans = "YES"}
	fmt.Println(ans)

}
