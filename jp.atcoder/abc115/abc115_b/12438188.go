package main

import (
  "fmt"
)

func maxInt(a ...int) int {m := a[0]; for _, x := range a {if x > m {m = x}}; return m}
func minInt(a ...int) int {m := a[0]; for _, x := range a {if x < m {m = x}}; return m}

func sumInt(a ...int) int {s := 0; for _, v := range a {s += v}; return s}

func main() {
  var n int
  fmt.Scan(&n)
  p := make([]int, n)
  for i := 0; i < n; i++ {
    fmt.Scan(&p[i])
  }
  res := sumInt(p...) - maxInt(p...) / 2
  fmt.Println(res)
}
