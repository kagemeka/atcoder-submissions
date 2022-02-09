package main

import (
  "fmt"
)

func main() {
  var a, b int
  fmt.Scan(&a, &b)
  ans := ":("
  if a <= 8 && b <= 8 {
    ans = "Yay!"
  }
  fmt.Println(ans)
}
