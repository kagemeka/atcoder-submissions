package main

import (
  "fmt"
)

func maxInt(a ...int) int {m := a[0]; for _, x := range a {if x > m {m = x}}; return m}
func minInt(a ...int) int {m := a[0]; for _, x := range a {if x < m {m = x}}; return m}

func main() {
  var a, b, c, d int
  fmt.Scan(&a, &b, &c, &d)
  res := maxInt(0, minInt(b, d) - maxInt(a, c))
  fmt.Println(res)
}
