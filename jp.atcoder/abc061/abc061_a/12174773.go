package main

import (
  "fmt"
)

func main() {
  var a, b, c int; fmt.Scan(&a, &b, &c)
  ans := "No"
  if c >= a && c <= b {ans = "Yes"}
  fmt.Println(ans)
}
