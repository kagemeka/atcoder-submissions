package main

import (
  "fmt"
)

// argument type must be []rune, not string.
func substr(rs []rune, l, r int) string {
  if l < 0 {l = 0}
  if r > len(rs) {r = len(rs)}
  if l >= r {return ""}
  return string(rs[l:r])
}

func main() {
  var s string
  fmt.Scan(&s)
  res := []rune(s)
  n := len(res)
  for l := n - 2; l > -1; l -= 2 {
    if substr(res, 0, l/2) == substr(res, l/2, l) {
      fmt.Println(l)
      return
    }
  }
}
