package main

import (
  "fmt"
)

func main() {
  var n, m int
  fmt.Scan(&n, &m)
  res := make([]int, n)
  for i := 0; i < m; i++ {
    var a, b int
    fmt.Scan(&a, &b)
    a--; b--
    res[a]++; res[b]++
  }
  for i := 0; i < n; i++ {
    fmt.Println(res[i])
  }
}
