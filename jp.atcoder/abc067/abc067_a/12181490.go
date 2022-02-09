package main

import (
  "fmt"
)

func main() {
  var a, b int; fmt.Scan(&a, &b)
  cand := []int{a, b, a + b}
  ans := "Impossible"
  for _, v := range cand {
    if v % 3 == 0 {
      ans = "Possible"
      break
    }
  }
  fmt.Println(ans)
}
