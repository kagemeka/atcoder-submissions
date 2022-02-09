package main

import (
  "fmt"
)

func maxInt(a ...int) int {m := a[0]; for _, x := range a {if x > m {m = x}}; return m}
func minInt(a ...int) int {m := a[0]; for _, x := range a {if x < m {m = x}}; return m}

func main() {
  var n int
  fmt.Scan(&n)
  cnt := 30
  for i := 0; i < n; i++ {
    var a int
    fmt.Scan(&a)
    tmp := 0
    for a % 2 == 0 {
      a /= 2
      tmp++
    }
    cnt = minInt(cnt, tmp)
  }
  fmt.Println(cnt)
}
