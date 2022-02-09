package main

import (
  "fmt"
)

func main() {
  var w string
  fmt.Scan(&w)
  res := make(map[rune]int)
  for _, c := range w {
    res[c]++
  }
  ans := "Yes"
  for _, c := range res {
    if c & 1 == 1 {
      ans = "No"
      break
    }
  }
  fmt.Println(ans)
}
