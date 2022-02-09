package main

import (
  "fmt"
  "sort"
)

func main() {
  var n, k int
  fmt.Scan(&n, &k)
  h := make([]int, n)
  for i := 0; i < n; i++ {
    fmt.Scan(&h[i])
  }
  sort.Ints(h)
  res := n - sort.SearchInts(h, k)
  fmt.Println(res)
}
