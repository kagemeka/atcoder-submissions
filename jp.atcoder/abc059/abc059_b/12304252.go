package main

import (
  "fmt"
)

func main() {
  var a, b string
  fmt.Scan(&a, &b)
  var ans string
  if a > b {
    ans = "GREATER"
  } else if a < b {
    ans = "LESS"
  } else {
    ans = "EQUAL"
  }
  fmt.Println(ans)
}
