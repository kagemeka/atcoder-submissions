package main

import (
  "fmt"
)

func main() {
  var n int
  fmt.Scan(&n)
  m := (n + 1) / 2
  fmt.Println(float64(m) / float64(n))
}
