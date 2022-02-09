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
    if strings.ContainsRune(s, 'r') {cnt++}
  }
  fmt.Println(cnt)
}
