package main

import (
  "fmt"
)

func main() {
  var s string
  fmt.Scan(&s)
  res := make(map[rune]int)
  for _, c := range s {
    res[c]++
  }
  cand := "ABCDEF"
  for _, c := range cand {
    fmt.Print(res[c])
    tail := " "
    if c == 'F' {tail = "\n"}
    fmt.Print(tail)
  }
}
