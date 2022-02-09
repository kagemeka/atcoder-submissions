package main

import (
  "fmt"
)

func maxInt(a ...int) int {m := a[0]; for _, x := range a {if x > m {m = x}}; return m}
func minInt(a ...int) int {m := a[0]; for _, x := range a {if x < m {m = x}}; return m}

func main() {
  var w, a, b int
  fmt.Scan(&w, &a, &b)
  if a > b {a, b = b, a}
  fmt.Println(maxInt(0, b - (a + w)))
}
