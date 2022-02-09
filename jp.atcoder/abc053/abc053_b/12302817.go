package main

import (
  "fmt"
  "strings"
)

func main() {
  var s string
  fmt.Scan(&s)
  res := strings.LastIndex(s, "Z") - strings.Index(s, "A") + 1
  fmt.Println(res)
}
