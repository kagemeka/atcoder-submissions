package main

import (
  "fmt"
)

func main() {
  var s string
  fmt.Scan(&s)
  if s == "a" {
    fmt.Println(-1)
  } else {
    fmt.Println("a")
  }
}
