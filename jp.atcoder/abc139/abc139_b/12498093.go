package main

import (
  "fmt"
)

func main() {
  var a, b int
  fmt.Scan(&a, &b)
  res := (b - 1 + a - 1 - 1) / (a - 1)
  fmt.Println(res)
}
