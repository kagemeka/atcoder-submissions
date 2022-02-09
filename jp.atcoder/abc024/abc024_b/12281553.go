package main

import (
  "fmt"
)

func maxInt(a ...int) int {m := a[0]; for _, x := range a {if x > m {m = x}}; return m}
func minInt(a ...int) int {m := a[0]; for _, x := range a {if x < m {m = x}}; return m}

func main() {
  var n, t int
  fmt.Scan(&n, &t)
  a := make([]int, n)
  for i := 0; i < n; i++ {
    fmt.Scan(&a[i])
  }
  tot := 0
  prev := a[0]
  for i := 1; i < n; i++ {
    tot += minInt(t, a[i] - prev)
    prev = a[i]
  }
  tot += t
  fmt.Println(tot)
}
