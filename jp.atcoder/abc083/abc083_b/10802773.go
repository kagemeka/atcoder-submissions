package main

import (
	"fmt"
	"math"
)

func divmod(a, b int) (int, int) {
	q := math.Floor(float64(a / b))
	r := a % b
	return int(q), r
}

func main() {

	var n, a, b int
	fmt.Scan(&n, &a, &b)

	var res, q, r, tot int
	for i := 1; i <= n; i++ {
		q = i
		tot = 0
		for q != 0 {
			q, r = divmod(q, 10)
			tot += r
		}
		if a <= tot && tot <= b {
			res += i
		}
	}
	fmt.Println(res)
}
