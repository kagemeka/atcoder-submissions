package main

import (
  "fmt"
)

func main() {
  var a, b int
  fmt.Scan(&a, &b)
  ans := "No"
  if a * b & 1 == 1 {
    ans = "Yes"
  }
  fmt.Println(ans)
}
