package main

import (
  "fmt"
)

func main() {
  var n int
  fmt.Scan(&n)
  res := 0
  v := make([]int, n)
  c := make([]int, n)
  for i := 0; i < n; i++ {
    fmt.Scan(&v[i])
  }
  for i := 0; i < n; i++ {
    fmt.Scan(&c[i])
  }
  for i := 0; i < n; i++ {
    if v[i] > c[i] {
      res += v[i] - c[i]
    }
  }
  fmt.Println(res)
}
