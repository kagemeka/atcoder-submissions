package main

import (
  "fmt"
)

func main() {
  var n int
  fmt.Scan(&n)
  res := make(map[int]bool)
  for i := 0; i < n; i++ {
    var a int
    fmt.Scan(&a)
    res[a] = true
  }
  fmt.Println(len(res))
}
