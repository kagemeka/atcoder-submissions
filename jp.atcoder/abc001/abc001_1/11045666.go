package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var sc = bufio.NewScanner(os.Stdin)

func readline() string {
	sc.Scan()
	return sc.Text()
}

func atoi(s string) int {
	i, _ := strconv.Atoi(s)
	return i
}

func main() {
	var a, b int
	a = atoi(readline())
	b = atoi(readline())
	ans := a - b
	fmt.Println(ans)
}
