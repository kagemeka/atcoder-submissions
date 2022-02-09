package main

import (
  "fmt"
)

func maxInt(a ...int) int {m := a[0]; for _, x := range a {if x > m {m = x}}; return m}
func minInt(a ...int) int {m := a[0]; for _, x := range a {if x < m {m = x}}; return m}

func main() {
  var n, a, b int
  fmt.Scan(&n, &a, &b)
  res := 0
  for i := 0; i < n; i++ {
    var s string
    var d int
    fmt.Scan(&s, &d)
    d = maxInt(minInt(d, b), a)
    if s == "East" {
      res += d
    } else {
      res -= d
    }
  }
  if res == 0 {
    fmt.Println(0)
    return
  }

  t := "East"
  if res < 0 {
    t = "West"
    res *= -1
  }
  fmt.Println(t, res)
}
