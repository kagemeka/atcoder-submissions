package main

import (
  "fmt"
  "math"
  "sort"
)

func main() {
  var n int
  fmt.Scan(&n)
  r := make([]float64, n + 1)
  for i := 1; i < n + 1; i++ {
    fmt.Scan(&r[i])
  }
  sort.Float64s(r)
  s := make([]float64, n + 1)
  for i := 0; i < n + 1; i ++ {
    s[i] = math.Pi * math.Pow(r[i], 2)
  }
  tot := 0.0
  for i := n; i > 0; i -= 2 {
    tot += s[i] - s[i-1]
  }
  fmt.Println(tot)
}
