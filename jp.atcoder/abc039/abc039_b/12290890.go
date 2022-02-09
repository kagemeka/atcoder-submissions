package main

import (
  "fmt"
  "math"
)

const (
  e = 1e-13
)

func nthRoot(y, n float64) float64 {
  x := y
  for math.Abs(math.Pow(x, n) - y) > e {
    x -= (math.Pow(x, n) - y) / (n * math.Pow(x, n - 1))
  }
  return x
}

func main() {
  var x float64
  fmt.Scan(&x)
  fmt.Println(nthRoot(x, 4))
}
