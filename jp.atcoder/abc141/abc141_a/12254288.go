package main

import (
  "fmt"
)

func stringIndex(ss []string, s string) int {
  i := -1
  for j := 0; j < len(ss); j++ {
    if ss[j] == s {
      i = j
      break
    }
  }
  return i
}

func main() {
  w := []string{
    "Sunny",
    "Cloudy",
    "Rainy",
  }
  var s string
  fmt.Scan(&s)
  fmt.Println(w[(stringIndex(w, s)+1)%3])
}
