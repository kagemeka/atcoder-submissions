package main

import (
  "fmt"
)

func reversedString(s string) string {
  r := []rune(s)
  n := len(r)
  for i := 0; i < n / 2; i++ {
    r[i], r[n-1-i] = r[n-i-1], r[i]
  }
  return string(r)
}

func main() {
  var s, t string; fmt.Scan(&s, &t)
  ans := "NO"
  if s == reversedString(t) {ans = "YES"}
  fmt.Println(ans)
}
