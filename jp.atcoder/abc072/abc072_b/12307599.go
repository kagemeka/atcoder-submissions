package main

import (
  "fmt"
)

func main() {
  var s string
  fmt.Scan(&s)
  res := make([]byte, 0)
  for i := 0; i < len(s); i += 2 {
    res = append(res, s[i])
  }
  fmt.Println(string(res))
}
