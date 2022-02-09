package main

import (
  "fmt"
)

var group = []int{1, 3, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1}

func main() {
  var x, y int; fmt.Scan(&x, &y)
  ans := "No"; if group[x-1] == group[y-1] {ans = "Yes"}
  fmt.Println(ans)
}
