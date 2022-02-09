package main

import (
  "fmt"
)


func main() {
  var s string
  fmt.Scan(&s)
  ans := "No"
  if s[2] == s[3] && s[4] == s[5] {
    ans = "Yes"
  }
  fmt.Println(ans)
}
