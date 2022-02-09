package main

import (
  "fmt"
  "strings"
)

func main() {
  var n int
  var s string
  fmt.Scan(&n, &s)
  fmt.Println(strings.Count(s, "ABC"))
}
