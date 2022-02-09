package main

import (
  "fmt"
)

func main() {
  var n, x int
  fmt.Scan(&n, &x)
  l := make([]int, n)
  for i := 0; i < n; i++ {fmt.Scan(&l[i])}
  d := 0
  for i := 0; i < n; i++ {
    d += l[i]
    if d > x {
      fmt.Println(i + 1)
      return
    }
  }
  fmt.Println(n + 1)
}
