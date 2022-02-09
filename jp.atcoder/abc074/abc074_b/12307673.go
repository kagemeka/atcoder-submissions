package main

import (
  "fmt"
)

func maxInt(a ...int) int {m := a[0]; for _, x := range a {if x > m {m = x}}; return m}
func minInt(a ...int) int {m := a[0]; for _, x := range a {if x < m {m = x}}; return m}

func main() {
  var n, k int
  fmt.Scan(&n, &k)
  tot := 0
  for i := 0; i < n; i++ {
    var x int
    fmt.Scan(&x)
    tot += minInt(x, k-x) * 2
  }
  fmt.Println(tot)
}
