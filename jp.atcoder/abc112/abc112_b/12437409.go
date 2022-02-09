package main

import (
  "fmt"
  "sort"
)

func main() {
  var n, t int
  fmt.Scan(&n, &t)
  ct := make([][2]int, n)
  for i := 0; i < n; i++ {
    fmt.Scan(&ct[i][0], &ct[i][1])
  }
  sort.Slice(ct, func(i, j int) bool {return ct[i][0] <= ct[j][0]})
  for i := 0; i < n; i++ {
    if ct[i][1] <= t {
      fmt.Println(ct[i][0])
      return
    }
  }
  fmt.Println("TLE")

}
