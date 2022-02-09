package main

import (
  "fmt"
)

func main() {
  var n rune
  var s string
  fmt.Scan(&n, &s)
  rs := []rune(s)
  for i := 0; i < len(s); i++ {
    rs[i] = (rs[i] - 'A' + n) % 26 + 'A'
  }
  fmt.Println(string(rs))
}
