package main

import (
	"fmt"
)

func main() {

	var a, b, c, x int
	fmt.Scan(&a, &b, &c, &x)

	var tot int
	var cnt int = 0
	for i := 0; i <= a; i++ {
		for j := 0; j <= b; j++ {
			for k := 0; k <= c; k++ {
				tot = 500*i + 100*j + 50*k
				if tot == x {
					cnt++
				}
			}
		}
	}
	fmt.Println(cnt)
}
