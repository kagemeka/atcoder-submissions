package main

import (
  "fmt"
)

func maxInt(a ...int) int {m := a[0]; for _, x := range a {if x > m {m = x}}; return m}
func minInt(a ...int) int {m := a[0]; for _, x := range a {if x < m {m = x}}; return m}

func main() {
  var r, u, n int
  l, d := 0, 0
  fmt.Scan(&r, &u, &n)
  for i := 0; i < n; i++ {
    var x, y, a int
    fmt.Scan(&x, &y, &a)
    switch a {
    case 1: l = maxInt(l, x)
    case 2: r = minInt(r, x)
    case 3: d = maxInt(d, y)
    case 4: u = minInt(u, y)
    }
  }
  x := maxInt(r - l, 0)
  y := maxInt(u - d, 0)
  fmt.Println(y * x)
}
