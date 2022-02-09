package main

import (
  "fmt"
)

func main() {
  var a, b int; fmt.Scan(&a, &b)
  ans := "Odd"
  if a * b % 2 == 0 {ans = "Even"}
  fmt.Println(ans)
}
