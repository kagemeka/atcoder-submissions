package main

import (
  "fmt"
)

func main() {
  var vowel = make(map[rune]bool)
  for _, c := range "aeiou" {
    vowel[c] = true
  }
  var w string
  fmt.Scan(&w)
  s := ""
  for _, c := range w {
    if _, ok := vowel[c]; ok {
      continue
    }
    s += string(c)
  }
  fmt.Println(s)
}
