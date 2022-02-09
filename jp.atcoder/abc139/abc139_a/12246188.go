package main

import (
  "fmt"
)

func main() {
  cnt := 0
  var s, t string
  fmt.Scan(&s, &t)
  for i := 0; i < 3; i++ {
    if s[i] == t[i] {cnt++}
  }
  fmt.Println(cnt)
}
