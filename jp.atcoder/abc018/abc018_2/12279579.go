package main

import (
  "fmt"
)

func main() {
  var s string
  var n int
  fmt.Scan(&s, &n)
  runes := []rune(s)
  for i := 0; i < n; i ++ {
    var l, r int
    fmt.Scan(&l, &r)
    l--
    for j := 0; j < (r - l) / 2; j ++ {
      runes[l+j], runes[r-j-1] = runes[r-j-1], runes[l+j]
    }
  }
  fmt.Println(string(runes))
}
