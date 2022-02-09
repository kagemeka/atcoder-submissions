package main

import (
  "fmt"
)

func main() {
  var n int
  fmt.Scan(&n)
  d := make([]int, n)
  for i := 0; i < n; i++ {
    fmt.Scan(&d[i])
  }
  for i := 0; i < n-1; i++ {d[i+1] += d[i]}
  res := 0
  for i := n-1; i > 0; i-- {
    res += (d[i] - d[i-1]) * d[i-1]
  }
  fmt.Println(res)
}
