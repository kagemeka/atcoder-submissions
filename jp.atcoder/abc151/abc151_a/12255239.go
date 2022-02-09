package main

import (
  "fmt"
)

func main() {
  var s string
  fmt.Scan(&s)
  c := []rune(s)[0]
  fmt.Println(string(c + 1))
}
