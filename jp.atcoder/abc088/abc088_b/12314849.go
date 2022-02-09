package main

import (
  "fmt"
  "sort"
)

func main() {
  var n int
  fmt.Scan(&n)
  a := make([]int, n)
  for i := 0; i < n; i++ {
    fmt.Scan(&a[i])
  }

  sort.Ints(a)
  sa := 0
  sb := 0
  for i := n - 1; i > -1; i -= 2 {
    sa += a[i]
  }
  for i := n - 2; i > -1; i -= 2 {
    sb += a[i]
  }
  fmt.Println(sa - sb)
}
