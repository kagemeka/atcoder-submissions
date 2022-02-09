package main

import (
  "fmt"
  "strconv"
)

func absInt(x int) int {if x < 0 {x *= -1}; return x}

// argument type must be []rune, not string.
func substr(rs []rune, l, r int) string {
  if l < 0 {l = 0}
  if r > len(rs) {r = len(rs)}
  if l >= r {return ""}
  return string(rs[l:r])
}

func maxInt(a ...int) int {m := a[0]; for _, x := range a {if x > m {m = x}}; return m}
func minInt(a ...int) int {m := a[0]; for _, x := range a {if x < m {m = x}}; return m}

func main() {
  var s string
  fmt.Scan(&s)
  n := len(s)
  rs := []rune(s)
  res := 1001
  for i := 0; i < n - 2; i++  {
    d, _ := strconv.Atoi(substr(rs, i, i + 3))
    res = minInt(res, absInt(753 - d))
  }
  fmt.Println(res)
}
