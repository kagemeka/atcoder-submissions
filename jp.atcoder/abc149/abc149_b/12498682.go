package main

import (
  "fmt"
)

func maxInt(a ...int) int {m := a[0]; for _, x := range a {if x > m {m = x}}; return m}
func minInt(a ...int) int {m := a[0]; for _, x := range a {if x < m {m = x}}; return m}

func main() {
  var a, b, k int
  fmt.Scan(&a, &b, &k)
  if a >= k {
    a -= k
  } else {
    k -= a
    a = 0
    b = maxInt(0, b - k)
  }
  fmt.Println(a, b)

}
