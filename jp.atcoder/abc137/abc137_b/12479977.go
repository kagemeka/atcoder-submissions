package main

import (
  "fmt"
)

func maxInt(a ...int) int {m := a[0]; for _, x := range a {if x > m {m = x}}; return m}
func minInt(a ...int) int {m := a[0]; for _, x := range a {if x < m {m = x}}; return m}

func main() {
  var k, x int
  fmt.Scan(&k, &x)
  l := maxInt(-1e6, x - (k - 1))
  r := minInt(1e6, x + (k - 1))
  for i := l; i < r + 1; i++ {
    fmt.Print(i)
    tail := " "
    if i == r {tail = "\n"}
    fmt.Print(tail)
  }
}
