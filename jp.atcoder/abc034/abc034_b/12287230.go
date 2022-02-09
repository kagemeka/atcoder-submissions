package main

import (
  "fmt"
)

func main() {
  var n int
  fmt.Scan(&n)
  m := n + 1
  if n & 1 == 0 {
    m = n - 1
  }
  fmt.Println(m)
}
