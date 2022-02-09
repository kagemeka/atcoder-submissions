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
  ans := "Yes"
  if len(res) == 1 {
    ans = "No"
  }
  fmt.Println(ans)
}
