package main

import (
  "fmt"
  "math"
)

func main() {
  var n, m float64
  fmt.Scan(&n, &m)
  m *= 6
  n = 30.0 * (float64(int(n) % 12) + m / 360.0)
  d := math.Abs(n - m)
  fmt.Println(math.Min(d, 360.0 - d))
}
