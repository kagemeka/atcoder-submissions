package main

import (
  "fmt"
)

func main() {
  var n int
  fmt.Scan(&n)
  h := make([]int, n)
  for i := 0; i < n; i++ {
    fmt.Scan(&h[i])
  }
  m := 0
  cnt := 0
  for _, x := range h {
    if x >= m {
      cnt++
      m = x
    }
  }
  fmt.Println(cnt)
}
