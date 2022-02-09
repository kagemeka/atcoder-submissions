package main

import (
  "fmt"
)

func main() {
  var n, q int
  fmt.Scan(&n, &q)
  a := make([]int, n)
  for i := 0; i < q; i++ {
    var l, r, t int
    fmt.Scan(&l, &r, &t)
    l--; r--
    for j := l; j < r + 1; j++ {
      a[j] = t
    }
  }
  for i := 0; i < n; i++ {
    fmt.Println(a[i])
  }
}
