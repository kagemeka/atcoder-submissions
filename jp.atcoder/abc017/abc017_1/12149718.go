package main

import (
  "fmt"
)

func main() {
  var tot int = 0
  for i := 0; i < 3; i++ {
    var s, c int
    fmt.Scan(&s, &c)
    tot += s / 10 * c
  }
  fmt.Println(tot)
}
