package main

import (
  "fmt"
)

func absInt(x int) int {if x < 0 {x *= -1}; return x}

func main() {
  var n, t, a int
  fmt.Scan(&n, &t, &a)
  a *= 1000
  t *= 1000
  h := make([]int, n)
  for i := 0; i < n; i++ {
    fmt.Scan(&h[i])
  }
  res := -1
  d := 1001001001
  for i, x := range h {
    diff := absInt(a - (t - x * 6))
    if diff < d {
      d = diff
      res = i + 1
    }
  }
  fmt.Println(res)
}
