package main

import (
  "fmt"
  "strconv"
)

func main() {
  var s string
  fmt.Scan(&s)
  ans := "TBD"
  m, _ := strconv.Atoi(string([]rune(s)[5:7]))
  if m <= 4 {ans = "Heisei"}
  fmt.Println(ans)
}
