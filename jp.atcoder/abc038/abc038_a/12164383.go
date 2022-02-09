package main

import (
  "fmt"
)

func main() {
  var s string; fmt.Scan(&s)
  ans := "NO"; if s[len(s)-1] == 'T' {ans = "YES"}
  fmt.Println(ans)
}
