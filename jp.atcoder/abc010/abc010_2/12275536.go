package main

import (
  "fmt"
)

func main() {
  var n int
  fmt.Scan(&n)
  tot := 0
  for i := 0; i < n; i++ {
    var a int
    fmt.Scan(&a)
    for a % 2 == 0 || a % 3 == 2 {
      a--
      tot++
    }
  }
  fmt.Println(tot)
}
