package main

import (
  "fmt"
)

func sumInt(a ...int) int {s := 0; for _, v := range a {s += v}; return s}
func maxInt(a ...int) int {m := a[0]; for _, x := range a {if x > m {m = x}}; return m}
func minInt(a ...int) int {m := a[0]; for _, x := range a {if x < m {m = x}}; return m}

func main() {
  var n, x int
  fmt.Scan(&n, &x)
  m := make([]int, n)
  for i := 0; i < n; i++ {
    fmt.Scan(&m[i])
  }
  cnt := n
  x -= sumInt(m...)
  cnt += x / minInt(m...)
  fmt.Println(cnt)

}
