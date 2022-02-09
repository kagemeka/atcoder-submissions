package main

import (
	"fmt"
)

func divmod(a, b int) (int, int) {return a / b, a % b}

func main() {
	var x int; fmt.Scan(&x)
	q, r := divmod(x, 100)
	ans := 0
	if r <= q * 5 {ans = 1}
	fmt.Println(ans)


}
