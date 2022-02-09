package main

import (
  "fmt"
)

func main() {
  var n int
  fmt.Scan(&n)
  res := make(map[string]bool)
  for i := 0; i < n; i++ {
    var s string
    fmt.Scan(&s)
    res[s] = true
  }
  ans := "Three"
  if len(res) == 4 {
    ans = "Four"
  }
  fmt.Println(ans)
}
