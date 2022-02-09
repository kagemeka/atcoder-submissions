package main

import (
  "fmt"
)

func main() {
  var n int
  fmt.Scan(&n)
  a := make([]int, n)
  for i := 0; i < n; i++ {
    fmt.Scan(&a[i])
  }
  cnt := 0
  tot := 0
  for _, v := range a {
    if v == 0 {continue}
    cnt++
    tot += v
  }
  fmt.Println((tot + cnt - 1) / cnt)
}
