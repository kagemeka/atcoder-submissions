package main

import (
  "fmt"
)


func maxInt(a ...int) int {m := a[0]; for _, x := range a {if x > m {m = x}}; return m}
func minInt(a ...int) int {m := a[0]; for _, x := range a {if x < m {m = x}}; return m}

func main() {
  var x, t int
  fmt.Scan(&x, &t)
  fmt.Println(maxInt(0, x - t))
}
