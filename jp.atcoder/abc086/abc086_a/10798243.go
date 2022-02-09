package main

import (
	"fmt"
)

func main() {
	var a, b int
	fmt.Scan(&a, &b)
	c := a * b
	var res string
	if c & 1 == 1 {
		res = "Odd"
	} else {
		res = "Even"
	}
	fmt.Println(res)
}
