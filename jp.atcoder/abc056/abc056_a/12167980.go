package main

import (
  "fmt"
)

func convert(s string) int {
  if s == "H" {return 1}
  return 0
}

func main() {
  var a, b string; fmt.Scan(&a, &b)
  ans := "H"; if convert(a) ^ convert(b) == 1 {ans = "D"}
  fmt.Println(ans)
}
