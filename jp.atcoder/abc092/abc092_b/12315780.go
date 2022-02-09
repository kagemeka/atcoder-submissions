package main

import (
  "fmt"
)

func main() {
  var n, d, x int
  fmt.Scan(&n, &d, &x)
  for i := 0; i < n; i++ {
    var a int
    fmt.Scan(&a)
    x += 1 + (d - 1) / a
  }
  fmt.Println(x)
}
