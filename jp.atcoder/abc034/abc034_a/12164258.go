package main

import (
  "fmt"
)

func main() {
  var x, y int
  fmt.Scan(&x, &y)
  ans := "Worse"; if x < y {ans = "Better"}
  fmt.Println(ans)
}
