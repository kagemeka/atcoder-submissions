package main

import (
  "fmt"
)

func main() {
  var n int
  fmt.Scan(&n)
  a := make([]float64, n)
  for i := 0; i < n; i++ {
    fmt.Scan(&a[i])
  }
  denom := 0.0
  for _, x := range a {denom += 1 / x}
  fmt.Println(1 / denom)
}
