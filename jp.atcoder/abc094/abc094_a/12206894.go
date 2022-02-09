package main

import (
  "fmt"
)

func main() {
  var a, b, x int
  fmt.Scan(&a, &b, &x)
  ans := "NO"
  if x >= a && x <= a + b {ans = "YES"}
  fmt.Println(ans)
}
