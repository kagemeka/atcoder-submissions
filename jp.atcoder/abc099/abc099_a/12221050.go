package main

import (
  "fmt"
)

func main() {
  var n int
  fmt.Scan(&n)
  ans := "ABD"
  if n < 1000 {
    ans = "ABC"
  }
  fmt.Println(ans)
}
