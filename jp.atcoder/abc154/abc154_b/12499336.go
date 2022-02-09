package main

import (
  "fmt"
  "strings"
)

func main() {
  var s string
  fmt.Scan(&s)
  n := len(s)
  fmt.Println(strings.Repeat("x", n))
}
