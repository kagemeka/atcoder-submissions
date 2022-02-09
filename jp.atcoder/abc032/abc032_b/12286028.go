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
  res := make(map[string]bool)
  var s string
  var k int
  fmt.Scan(&s, &k)
  n := len(s)
  rs := []rune(s)
  for i := 0; i < n - k + 1; i++ {
    res[substr(rs, i, i + k)] = true
  }
  fmt.Println(len(res))
}
