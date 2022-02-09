package main

import (
  "fmt"
)

func main() {
  var n, s, t, w int
  fmt.Scan(&n, &s, &t)
  w = 0
  best := func(w int) bool {
    return w >= s && w <= t
  }
  tot := 0
  for i := 0; i < n; i++ {
    var dw int; fmt.Scan(&dw)
    w += dw
    if best(w) {tot++}
  }
  fmt.Println(tot)
}
