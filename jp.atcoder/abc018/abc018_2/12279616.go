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
    l--; r--
    d := r - l + 1
    for j := 0; j < d / 2; j ++ {
      runes[l+j], runes[r-j] = runes[r-j], runes[l+j]
    }
  }
  fmt.Println(string(runes))
}
