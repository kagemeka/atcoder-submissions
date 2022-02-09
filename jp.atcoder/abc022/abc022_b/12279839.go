package main

import (
  "fmt"
)

func main() {
  var n int
  fmt.Scan(&n)
  res := make(map[int]int)
  for i := 0; i < n; i++ {
    var a int
    fmt.Scan(&a)
    res[a]++
  }
  tot := 0
  for _, v := range res {
    tot += v - 1
  }
  fmt.Println(tot)
}
