package main

import (
  "fmt"
  "math"
)

const (
  e = 1e-6
)

func main() {
  var y float64
  fmt.Scan(&y)
  x := y
  for i := 0; i < 100; i++ {
    x -= (math.Pow(x, 4) - y) / (4 * math.Pow(x, 3))
  }
  fmt.Println(x)
}
