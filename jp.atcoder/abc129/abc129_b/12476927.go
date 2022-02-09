package main

import (
  "fmt"
)

func absInt(x int) int {if x < 0 {x *= -1}; return x}
func maxInt(a ...int) int {m := a[0]; for _, x := range a {if x > m {m = x}}; return m}
func minInt(a ...int) int {m := a[0]; for _, x := range a {if x < m {m = x}}; return m}

func main() {
  var n int
  fmt.Scan(&n)
  w := make([]int, n)
  s1, s2 := 0, 0
  for i := 0; i < n; i++ {
    fmt.Scan(&w[i])
    s2 += w[i]
  }
  res := s2
  for i := 0; i < n; i++ {
    s1 += w[i]
    s2 -= w[i]
    res = minInt(res, absInt(s1 - s2))

  }
  fmt.Println(res)


}
