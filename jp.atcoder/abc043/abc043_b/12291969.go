package main

import (
  "fmt"
)

func maxInt(a ...int) int {m := a[0]; for _, x := range a {if x > m {m = x}}; return m}
func minInt(a ...int) int {m := a[0]; for _, x := range a {if x < m {m = x}}; return m}

func main() {
  var s string
  fmt.Scan(&s)
  var res []rune
  for _, c := range s {
    if c == 'B' {
      res = res[:maxInt(0, len(res) - 1)]
    } else {
      res = append(res, c)
    }
  }
  fmt.Println(string(res))
}
