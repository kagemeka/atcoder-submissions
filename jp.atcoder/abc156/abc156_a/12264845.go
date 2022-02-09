package main

import (
  "fmt"
)

func maxInt(a ...int) int {m := a[0]; for _, x := range a {if x > m {m = x}}; return m}
func minInt(a ...int) int {m := a[0]; for _, x := range a {if x < m {m = x}}; return m}

func main() {
  var n, r int
  fmt.Scan(&n, &r)
  r += 100 * maxInt(0, 10 - n)
  fmt.Println(r)
}
