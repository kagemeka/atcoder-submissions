package main

import (
  "fmt"
  "strings"
  "unicode"
)

func main() {
  var s string
  fmt.Scan(&s)
  res := "AC"
  if s[0] == 'A' {
    i := strings.Index(s, "C")
    if i == -1 || i == 1 || i == len(s) - 1 {
      res = "WA"
    } else {
      for j := 1; j < len(s); j++ {
        if j == i {continue}
        if rune(s[j]) != unicode.ToLower(rune(s[j])) {
          res = "WA"
          break
        }
      }
    }
  } else {
    res = "WA"
  }
  fmt.Println(res)
}
