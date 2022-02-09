package main

import (
  "fmt"
  "sort"
)

func main() {
  res := make(map[int]int)
  var a [3]int
  for i := 0; i < 3; i++ {
    fmt.Scan(&a[i])
    res[a[i]] = i + 1
  }
  b := a[:3]
  sort.Sort(sort.Reverse(sort.IntSlice(b)))
  for _, s := range b {
    fmt.Println(res[s])
  }
}
