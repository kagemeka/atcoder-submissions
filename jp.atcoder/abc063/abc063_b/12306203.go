package main

import (
  "fmt"
)

func main() {
  var s string
  fmt.Scan(&s)
  res := make(map[rune]bool)
  for _, c := range s {
    res[c] = true
  }
  ans := "no"
  if len(res) == len(s) {
    ans = "yes"
  }
  fmt.Println(ans)
}
