package main

import (
  "fmt"
  "strings"
  "unicode"
)

func main() {
  var s string
  fmt.Scan(&s)
  s = strings.ToLower(s)
  r := []rune(s)
  r[0] = unicode.ToUpper(r[0])
  fmt.Println(string(r))

}
