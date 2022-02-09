package main

import (
  "fmt"
)

func main() {
  var s string
  fmt.Scan(&s)
  ans := "TBD"
  if s[6] <= '4' {ans = "Heisei"}
  fmt.Println(ans)
}
