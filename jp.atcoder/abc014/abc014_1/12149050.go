package main

import (
  "fmt"
)

func main() {
  var a, b int
  fmt.Scan(&a, &b)
  c := (a + b - 1) / b * b - a
  fmt.Println(c)
}
