package main

import (
  "fmt"
)

func main() {
  var h, w int
  fmt.Scan(&h, &w)
  ss := make([]string, h)
  for i := 0; i < h; i++ {
    fmt.Scan(&ss[i])
  }
  for _, s := range ss {
    for i := 0; i < 2; i++ {
      fmt.Println(s)
    }
  }
}
