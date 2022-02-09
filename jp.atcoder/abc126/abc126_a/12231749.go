package main

import (
  "fmt"
  "unicode"
)

func main() {
  var n, k int
  var s string
  fmt.Scan(&n, &k, &s)
  runes := []rune(s)
  runes[k-1] = unicode.ToLower(runes[k-1])
  fmt.Println(string(runes))
}
