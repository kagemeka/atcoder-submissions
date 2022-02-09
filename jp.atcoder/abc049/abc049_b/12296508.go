package main

import (
  "fmt"
)

func main() {
  var h, w int
  fmt.Scan(&h, &w)
  for i := 0; i < h; i++ {
    var s string
    fmt.Scan(&s)
    for j := 0; j < 2; j++ {
      fmt.Println(s)
    }
  }
}
