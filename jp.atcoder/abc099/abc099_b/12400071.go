package main

import (
  "fmt"
)

func main() {
  var a, b int
  fmt.Scan(&a, &b)
  n := b - a
  ans := (1 + n) * n / 2 - b
  fmt.Println(ans)
}
