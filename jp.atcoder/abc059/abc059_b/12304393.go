package main

import (
  "fmt"
)

func main() {
  var a, b string
  fmt.Scan(&a, &b)

  var ans string
  if len(a) > len(b) {
    ans = "GREATER"
  } else if len(a) < len(b) {
    ans = "LESS"
  } else {
    if a > b {
      ans = "GREATER"
    } else if a < b {
      ans = "LESS"
    } else {
      ans = "EQUAL"
    }
  }

  fmt.Println(ans)
}
