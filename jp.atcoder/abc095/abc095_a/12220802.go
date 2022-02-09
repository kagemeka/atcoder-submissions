package main

import (
  "fmt"
  "strings"
)

func main() {
  var s string
  fmt.Scan(&s)
  fmt.Println(700 + 100*strings.Count(s, "o"))
}
