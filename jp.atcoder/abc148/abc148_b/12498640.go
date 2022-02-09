package main

import (
  "fmt"
)

func main() {
  var n int
  var s, t string
  fmt.Scan(&n, &s, &t)
  res := ""
  for i := 0; i < n; i++ {
    res += string(s[i]) + string(t[i])
  }
  fmt.Println(res)
}
