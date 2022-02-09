package main

import (
  "fmt"
)

func main() {
  var n, m, c int
  fmt.Scan(&n, &m, &c)
  b := make([]int, m)
  for i := 0; i < m; i++ {
    fmt.Scan(&b[i])
  }

  cnt := 0
  for i := 0; i < n; i++ {
    a := make([]int, m)
    for j := 0; j < m; j++ {
      fmt.Scan(&a[j])
    }
    s := c
    for j := 0; j < m; j++ {
      s += a[j] * b[j]
    }
    if s > 0 {cnt++}
  }
  fmt.Println(cnt)
}
