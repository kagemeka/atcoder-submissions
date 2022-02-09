package main

import (
  "fmt"
)

func main() {
  var a, b int
  fmt.Scan(&a, &b)
  s := a*b - (a + b - 1)
  fmt.Println(s)
}
