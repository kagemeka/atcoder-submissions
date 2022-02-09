package main

import (
  "fmt"
  "strings"
)

func main() {
  res := ""
  for i := 0; i < 3; i++ {
    var s string; fmt.Scan(&s)
    res += strings.ToUpper(string(s[0]))
  }
  fmt.Println(res)
}
