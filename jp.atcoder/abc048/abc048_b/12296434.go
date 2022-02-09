package main

import (
  "fmt"
)
func main() {
  var a, b, x int
  fmt.Scan(&a, &b, &x)
  res := b / x - a / x
  if a % x == 0 {res++}
  fmt.Println(res)
}
