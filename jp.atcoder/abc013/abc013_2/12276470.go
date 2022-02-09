package main

import (
  "fmt"
)

func maxInt(a ...int) int {m := a[0]; for _, x := range a {if x > m {m = x}}; return m}
func minInt(a ...int) int {m := a[0]; for _, x := range a {if x < m {m = x}}; return m}

func main() {
  var a, b int
  fmt.Scan(&a, &b)
  if a >= b {
    fmt.Println(minInt(a-b, 10-(a-b)))
  } else {
    fmt.Println(minInt(b-a, 10-(b-a)))
  }
}
