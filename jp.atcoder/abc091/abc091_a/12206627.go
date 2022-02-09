package main

import (
  "fmt"
)

func main() {
  var a, b, c int
  fmt.Scan(&a, &b, &c)
  ans := "No"
  if a + b >= c {ans = "Yes"}
  fmt.Println(ans)
}
