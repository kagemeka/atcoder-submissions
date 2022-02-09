package main

import (
  "fmt"
)

func main() {
  var a, b int
  fmt.Scan(&a, &b)
  ans := b - a
  if b % a == 0 {ans = a + b}
  fmt.Println(ans)
}
