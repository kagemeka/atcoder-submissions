package main

import (
  "fmt"
)

func main() {
  var a, b int; var op string
  fmt.Scan(&a, &op, &b)
  var c int
  if op == "+" {c = a + b} else {c = a - b}
  fmt.Println(c)
}
