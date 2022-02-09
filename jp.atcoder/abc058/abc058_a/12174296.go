package main

import (
  "fmt"
)

func main() {
  var a, b, c int; fmt.Scan(&a, &b, &c)
  ans := "NO"
  if b - a == c - b {ans = "YES"}
  fmt.Println(ans)
}
