package main

import (
  "fmt"
  "math"
)

func main() {
  var n float64
  fmt.Scan(&n)
  fmt.Println(int(math.Pow(math.Floor(math.Sqrt(n)), 2)))
}
