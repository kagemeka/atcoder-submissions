package main

import (
  "fmt"
)

func main() {
  var a, b int
  fmt.Scan(&a, &b)
  c := a + b
  if c & 1 == 1 {
    fmt.Println("IMPOSSIBLE")
  } else {
    fmt.Println(c / 2)
  }
}
