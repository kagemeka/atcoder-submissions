package main

import (
  "fmt"
)

func main() {
  var n int
  fmt.Scan(&n)
  cand := []int{17, 13, 10, 9, 8, 6, 5, 3, 2, 1}
  ans := "Yes"
  for _, x := range cand {
    if n == x {
      ans = "No"
      break
    }
  }
  fmt.Println(ans)
}
