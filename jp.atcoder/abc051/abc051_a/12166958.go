package main

import (
  "fmt"
  "strings"
)

func main() {
  var s string; fmt.Scan(&s)
  s = strings.ReplaceAll(s, ",", " ")
  fmt.Println(s)
}
