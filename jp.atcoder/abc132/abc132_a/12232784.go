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
  for _, v := range res {
    if v != 2 {
      ans = "No"
      break
    }
  }
  fmt.Println(ans)
}
