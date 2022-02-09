package main

import (
  "fmt"
)

func main() {
  res := ""
  for i := 0; i < 3; i++ {
    var s string; fmt.Scan(&s)
    res += string(s[0])
  }
  fmt.Println(res)
}
