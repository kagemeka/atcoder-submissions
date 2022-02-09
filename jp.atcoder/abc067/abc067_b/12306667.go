package main

import (
  "fmt"
  "sort"
)

func sumInt(a ...int) int {s := 0; for _, v := range a {s += v}; return s}
func reverseSortIntSlice(a []int) {sort.Sort(sort.Reverse(sort.IntSlice(a)))}

func main() {
  var n, k int
  fmt.Scan(&n, &k)
  l := make([]int, n)
  for i := 0; i < n; i++ {
    fmt.Scan(&l[i])
  }
  reverseSortIntSlice(l)
  fmt.Println(sumInt(l[:k]...))
}
