package main

import (
  "fmt"
  "strings"
)

func main() {
  var s string; fmt.Scan(&s)
  s = strings.Replace(s, ",", " ", -1)
  fmt.Println(s)
}
