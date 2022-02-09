package main

import (
  "fmt"
  "math"
)

func main() {
  var y float64
  fmt.Scan(&y)
  x := math.Round(math.Pow(y, 0.25))
  fmt.Println(x)
}
