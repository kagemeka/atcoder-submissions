package main

import (
  "fmt"
)

func main() {
  var s string
  fmt.Scan(&s)
  ans := "Good"
  for i := 0; i < 3; i++ {
    if s[i] == s[i+1] {
      ans = "Bad"
      break
    }
  }
  fmt.Println(ans)
}
