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
  var n string; fmt.Scan(&n)
  ans := "No"
  if n == reversedString(n) {ans = "Yes"}
  fmt.Println(ans)
}
