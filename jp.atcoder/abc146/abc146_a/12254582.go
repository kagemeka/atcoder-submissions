package main

import (
  "fmt"
  "strings"
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
  day := strings.Split("SUN, MON, TUE, WED, THU, FRI, SAT", ", ")
  var s string
  fmt.Scan(&s)
  fmt.Println(7 - stringIndex(day, s))
}
