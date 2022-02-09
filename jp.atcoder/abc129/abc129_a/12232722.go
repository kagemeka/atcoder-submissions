package main

import (
  "fmt"
)

func maxInt(a ...int) int {m := a[0]; for _, x := range a {if x > m {m = x}}; return m}
func minInt(a ...int) int {m := a[0]; for _, x := range a {if x < m {m = x}}; return m}

func sumInt(a []int) int {
  s := 0
  for _, v := range a {s += v}
  return s
}

func main() {
  t := make([]int, 3)
  for i := 0; i < 3; i++ {
    fmt.Scan(&t[i])
  }
  fmt.Println(sumInt(t) - maxInt(t...))
}
