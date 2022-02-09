package main

import (
  "fmt"
)

func maxInt(a ...int) int {m := a[0]; for _, x := range a {if x > m {m = x}}; return m}
func minInt(a ...int) int {m := a[0]; for _, x := range a {if x < m {m = x}}; return m}

func main() {
  var n int
  var s string
  fmt.Scan(&n, &s)
  x := 0
  res := x
  for _, c := range s {
    if c == 'I' {
      x++
      res = maxInt(res, x)
    } else {
      x--
    }
  }
  fmt.Println(res)

}
