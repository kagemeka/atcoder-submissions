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

func main() {
	var a, b int
	a, _ = strconv.Atoi(readline())
	b, _ = strconv.Atoi(readline())
	ans := a - b
	fmt.Println(ans)
}
