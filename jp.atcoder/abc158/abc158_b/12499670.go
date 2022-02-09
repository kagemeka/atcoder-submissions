package main

import (
  "fmt"
)

func divmod(a, b int) (int, int) {return a / b, a % b}
func maxInt(a ...int) int {m := a[0]; for _, x := range a {if x > m {m = x}}; return m}
func minInt(a ...int) int {m := a[0]; for _, x := range a {if x < m {m = x}}; return m}

func main() {
  var n, a, b int
  fmt.Scan(&n, &a, &b)
  q, r := divmod(n, a + b)
  res := a * q + minInt(r, a)
  fmt.Println(res)

}
