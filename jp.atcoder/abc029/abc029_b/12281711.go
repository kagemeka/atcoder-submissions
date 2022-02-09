package main

import (
  "fmt"
  "strings"
)

func main() {
  cnt := 0
  for i := 0; i < 12; i++ {
    var s string
    fmt.Scan(&s)
    if strings.Index(s, "r") == -1 {continue}
    cnt++
  }
  fmt.Println(cnt)
}
