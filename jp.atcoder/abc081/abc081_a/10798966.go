package main

import (
	"fmt"
	"strings"
)

func main() {
	var s string
	fmt.Scanln(&s)
	res := strings.Count(s, "1")

	fmt.Println(res)

}
