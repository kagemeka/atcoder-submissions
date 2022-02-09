package main

import (
  "fmt"
  "strconv"
)

// argument type must be []rune, not string.
func substr(rs []rune, l, r int) string {
  if l < 0 {l = 0}
  if r > len(rs) {r = len(rs)}
  if l >= r {return ""}
  return string(rs[l:r])
}

func main() {
  var a, b int
  var s string
  fmt.Scan(&a, &b, &s)
  ans := "Yes"
  if s[a] == '-' {
    rs := []rune(s)
    if _, err := strconv.Atoi(substr(rs, 0, a)); err != nil {
      ans = "No"
    } else if _, err := strconv.Atoi(substr(rs, a+1, a+b+1)); err != nil {
      ans = "No"
    }
  } else {
    ans = "No"
  }
  fmt.Println(ans)
}
