package main

import (
  "fmt"
)

func maxInt(a ...int) int {m := a[0]; for _, x := range a {if x > m {m = x}}; return m}
func minInt(a ...int) int {m := a[0]; for _, x := range a {if x < m {m = x}}; return m}

func main() {
  var k, s int
  fmt.Scan(&k, &s)

  cnt := 0
  for x := 0; x <= minInt(k, s); x++ {
    t := s - x
    if t <= k {
      cnt += t + 1
    } else if t <= k * 2 {
      cnt += k - (t - k) + 1
    }
  }
  fmt.Println(cnt)
}
