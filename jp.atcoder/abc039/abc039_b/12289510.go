package main

import (
  "fmt"
  "math"
)

func main() {
  var y float64
  fmt.Scan(&y)
  x := math.Floor(math.Pow(y, 0.25) + 0.5)
  fmt.Println(x)
}
