package main

import (
  "fmt"
)

func main() {
  var r, g, b int; fmt.Scan(&r, &g, &b)
  ans := "NO"
  if d := 10*g + b; d % 4 == 0 {ans = "YES"}
  fmt.Println(ans)
}
