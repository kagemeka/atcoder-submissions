package main

import (
  "fmt"
  "sort"
)

func main() {
  var a [3]int
  for i := 0; i < 3; i++ {fmt.Scan(&a[i])}
  c := a
  b := c[:3]
  sort.Sort(sort.Reverse(sort.IntSlice(b)))
  res := make(map[int]int)
  for i, s := range b {res[s] = i + 1}
  for _, s := range a {fmt.Println(res[s])}
}
