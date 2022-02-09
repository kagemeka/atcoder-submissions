package main

import (
  "fmt"
)

const (
  mod = 1e9 + 7
  eps = 1e-13
  inf = 1 << 63 - 1
)

func absInt(x int) int {if x < 0 {x *= -1}; return x}

func dist(x1, y1, x2, y2 int) int {
  return absInt(x2 - x1) + absInt(y2 - y1)
}

func main() {
  var n, m int
  fmt.Scan(&n, &m)
  a := make([]int, n)
  b := make([]int, n)
  c := make([]int, m)
  d := make([]int, m)
  for i := 0; i < n; i++ {
    fmt.Scan(&a[i], &b[i])
  }
  for i := 0; i < m; i++ {
    fmt.Scan(&c[i], &d[i])
  }
  for i := 0; i < n; i++ {
    d1 := inf
    var res int
    for j := 0; j < m; j++ {
      d2 := dist(a[i], b[i], c[j], d[j])
      if d2 < d1 {
        d1 = d2
        res = j + 1
      }
    }
    fmt.Println(res)
  }
}
