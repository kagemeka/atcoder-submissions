package main

import (
  "fmt"
)

func MaxInt(a ...int) int {m := a[0]; for _, x := range a {if x > m {m = x}}; return m}
func MinInt(a ...int) int {m := a[0]; for _, x := range a {if x < m {m = x}}; return m}

func main() {
  var x, y int
  fmt.Scan(&x, &y)
  fmt.Println(MaxInt(x, y))
}
