package main

import (
  "fmt"
)

func sumInt(a ...int) int {s := 0; for _, v := range a {s += v}; return s}

func main() {
  var n int
  fmt.Scan(&n)
  t := make([]int, n)
  for i := 0; i < n; i++ {
    fmt.Scan(&t[i])
  }
  tot := sumInt(t...)
  var m int
  fmt.Scan(&m)
  for i := 0; i < m; i++ {
    var p, x int
    fmt.Scan(&p, &x)
    fmt.Println(tot + (x - t[p-1]))
  }

}
