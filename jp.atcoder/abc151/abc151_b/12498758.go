package main

import (
  "fmt"
)

func sumInt(a ...int) int {s := 0; for _, v := range a {s += v}; return s}

func main() {
  var n, k, m int
  fmt.Scan(&n, &k, &m)
  border := m * n
  a := make([]int, n-1)
  for i := 0; i < n-1; i++ {
    fmt.Scan(&a[i])
  }
  s := sumInt(a...)
  b := border - s
  if b > k {
    fmt.Println(-1)
  } else {
    if b < 0 {b = 0}
    fmt.Println(b)
  }


}
