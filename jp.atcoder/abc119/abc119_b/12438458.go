package main

import (
  "fmt"
)

func main() {
  var n int
  fmt.Scan(&n)
  tot := 0.0
  for i := 0; i < n; i++ {
    var x float64
    var u string
    fmt.Scan(&x, &u)
    if u == "BTC" {
      x *= 3.8e+5
    }
    tot += x
  }
  fmt.Println(tot)
}
