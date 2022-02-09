package main

import (
  "fmt"
)

func sumInt(a ...int) int {s := 0; for _, v := range a {s += v}; return s}
func maxInt(a ...int) int {m := a[0]; for _, x := range a {if x > m {m = x}}; return m}
func minInt(a ...int) int {m := a[0]; for _, x := range a {if x < m {m = x}}; return m}

func main() {
  var n, m int
  fmt.Scan(&n, &m)
  a := make([]int, m)
  for i := 0; i < m; i++ {
    fmt.Scan(&a[i])
  }
  s := sumInt(a...)
  res := -1
  res = maxInt(res, n - s)
  fmt.Println(res)
}
