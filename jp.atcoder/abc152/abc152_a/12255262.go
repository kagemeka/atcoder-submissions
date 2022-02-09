package main

import (
  "fmt"
)

func main() {
  var n, m int
  fmt.Scan(&n, &m)
  ans := "No"
  if n == m {ans = "Yes"}
  fmt.Println(ans)
}
