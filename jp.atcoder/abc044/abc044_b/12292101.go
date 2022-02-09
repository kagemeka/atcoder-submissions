package main

import (
  "fmt"
)

func main() {
  var w string
  fmt.Scan(&w)
  res := make(map[rune]int)
  for _, c := range w {
    res[c] ^= 1
  }
  ans := "Yes"
  for _, v := range res {
    if v == 1 {
      ans = "No"
      break
    }
  }
  fmt.Println(ans)
}
