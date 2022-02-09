package main

import (
  "fmt"
)

func maxInt(a ...int) int {m := a[0]; for _, x := range a {if x > m {m = x}}; return m}
func minInt(a ...int) int {m := a[0]; for _, x := range a {if x < m {m = x}}; return m}

func main() {
  var a, b, k int
  fmt.Scan(&a, &b, &k)
  if k * 2 >= b - a + 1 {
    for i := a ; i < b + 1; i ++ {
      fmt.Println(i)
    }
  } else {
    for i := a; i < a + k; i++ {
      fmt.Println(i)
    }
    for i := b - k + 1; i < b + 1; i++ {
      fmt.Println(i)
    }
  }
}
