package main

import (
  "fmt"
)
func maxInt(a ...int) int {m := a[0]; for _, x := range a {if x > m {m = x}}; return m}
func minInt(a ...int) int {m := a[0]; for _, x := range a {if x < m {m = x}}; return m}

func main() {
  res := 0
  m := 0
  for i := 0; i < 5; i++ {
    var a int
    fmt.Scan(&a)
    b := (a + 9) / 10 * 10
    res += b
    m = maxInt(m, b - a)
  }
  res -= m
  fmt.Println(res)
}
