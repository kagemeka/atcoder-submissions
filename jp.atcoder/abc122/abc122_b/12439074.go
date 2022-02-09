package main

import (
  "fmt"
)

func maxInt(a ...int) int {m := a[0]; for _, x := range a {if x > m {m = x}}; return m}
func minInt(a ...int) int {m := a[0]; for _, x := range a {if x < m {m = x}}; return m}


var cand = map[rune]bool{
  'A': true,
  'C': true,
  'G': true,
  'T': true,
}

func main() {
  var s string
  fmt.Scan(&s)
  s += "$"

  res := 0
  cnt := 0
  for _, c := range s {
    if _, ok := cand[c]; ok {
      cnt++
    } else {
      res = maxInt(res, cnt)
      cnt = 0
    }
  }
  fmt.Println(res)
}
