package main

import (
  "fmt"
  "sort"
)

func ReverseSortInt(a []int) {sort.Sort(sort.Reverse(sort.IntSlice(a)))}

func main() {
  var a [3]int
  for i := 0; i < 3; i++ {fmt.Scan(&a[i])}
  b := a
  ReverseSortInt(b[:])
  res := make(map[int]int)
  for i, s := range b {res[s] = i + 1}
  for _, s := range a {fmt.Println(res[s])}
}
