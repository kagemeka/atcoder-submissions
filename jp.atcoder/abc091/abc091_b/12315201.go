package main

import (
  "fmt"
)

func maxInt(a ...int) int {m := a[0]; for _, x := range a {if x > m {m = x}}; return m}
func minInt(a ...int) int {m := a[0]; for _, x := range a {if x < m {m = x}}; return m}

func main() {
  var n int
  fmt.Scan(&n)
  res := make(map[string]int)
  for i := 0; i < n; i++ {
    var s string
    fmt.Scan(&s)
    res[s]++
  }
  var m int
  fmt.Scan(&m)
  for i := 0; i < m; i++ {
    var t string
    fmt.Scan(&t)
    res[t]--
  }
  ans := 0
  for _, c := range res {
    ans = maxInt(ans, c)
  }
  fmt.Println(ans)
}
