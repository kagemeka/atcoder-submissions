package main

import (
  "fmt"
  "sort"
)

func main() {
  var n, m, X, Y int
  fmt.Scan(&n, &m, &X, &Y)
  x := make([]int, n)
  y := make([]int, m)
  for i := 0; i < n; i++ {
    fmt.Scan(&x[i])
  }
  for i := 0; i < m; i++ {
    fmt.Scan(&y[i])
  }
  x = append(x, X)
  y = append(y, Y)
  sort.Ints(x)
  sort.Ints(y)

  ans := "No War"
  if x[n] >= y[0] {
    ans = "War"
  }
  fmt.Println(ans)
}
