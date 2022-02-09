package main

import (
  "fmt"
)

func main() {
  vowels := make(map[rune]bool)
  for _, c := range "aeiou" {vowels[c] = true}
  var c string; fmt.Scan(&c)
  var ans string
  if _, ok := vowels[rune(c[0])]; ok {ans = "vowel"} else {ans = "consonant"}
  fmt.Println(ans)
}
