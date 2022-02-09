package main

import (
  "fmt"
)

func main() {
  var a, b int
  fmt.Scan(&a, &b)
  if a > b {
    a, b = b, a
  }
  var res int
  if a == b {
    res = a + b
  } else {
    res = b * 2 - 1
  }
  fmt.Println(res)
}
