package main

import (
  "fmt"
  "strings"
)

func main() {
  var s string
  fmt.Scan(&s)
  var r = strings.NewReader(s)
  x := make([]byte, 1)
  r.Read(x)
  fmt.Println(x[0] - 'A' + 1)
}
