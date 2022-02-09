package main

import (
  "fmt"
)

func main() {
  var n, x int
  fmt.Scan(&n, &x)
  a := make([]int, n)
  for i := 0; i < n; i++ {
    fmt.Scan(&a[i])
  }
  tot := 0
  for i := uint(0); i < uint(n); i++ {
    if x >> i & 1 == 1 {
      tot += a[i]
    }
  }
  fmt.Println(tot)
}
