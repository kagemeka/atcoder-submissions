package main

import (
  "fmt"
)

func stringReplaceAtIndex(s string, r rune, i int) string {
  runes := []rune(s); runes[i] = r
  return string(runes)
}

func main() {
  var s string; fmt.Scan(&s)
  fmt.Println(stringReplaceAtIndex(s, '8', 3))
}
