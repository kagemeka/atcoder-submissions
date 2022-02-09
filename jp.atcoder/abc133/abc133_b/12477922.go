package main

import (
  "fmt"
  "math"
)

func dist(a, b []float64, d int) float64 {
  res := 0.0
  for i := 0; i < d; i++ {
    res += math.Pow(a[i] - b[i], 2)
  }
  res = math.Sqrt(res)
  return res
}

func main() {
  var n, d int
  fmt.Scan(&n, &d)
  x := make([][]float64, n)
  for i := 0; i < n; i++ {
    x[i] = make([]float64, d)
    for j := 0; j < d; j++ {
      fmt.Scan(&x[i][j])
    }
  }
  cnt := 0
  for i := 0; i < n - 1; i++ {
    for j := i + 1; j < n; j++ {
      d := dist(x[i], x[j], d)
      if d == math.Floor(d) {cnt++}
    }
  }
  fmt.Println(cnt)
}
