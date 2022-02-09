package main

import (
  "fmt"
  "math"
)

func main() {
  var n float64
  fmt.Scan(&n)
  fmt.Println(math.Pow(2, math.Floor(math.Log2(n))))
}
