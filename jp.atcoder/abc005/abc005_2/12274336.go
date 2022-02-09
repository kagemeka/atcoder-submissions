package main

import (
  "fmt"
)

func maxInt(a ...int) int {m := a[0]; for _, x := range a {if x > m {m = x}}; return m}
func minInt(a ...int) int {m := a[0]; for _, x := range a {if x < m {m = x}}; return m}

func main() {
  var n int
  fmt.Scan(&n)
  var t = make([]int, n)
  for i := 0; i < n; i++ {
    fmt.Scan(&t[i])
  }
  fmt.Println(minInt(t...))
}
