package main

import (
  "fmt"
  "sort"
)

func reverseSortIntSlice(a []int) {sort.Sort(sort.Reverse(sort.IntSlice(a)))}

func main() {
  var n int 
  fmt.Scan(&n)
  a := make([]int, n)
  for i := 0; i < n; i++ {
    fmt.Scan(&a[i])
  }
  reverseSortIntSlice(a)
  m := a[0]
  for i := 1; i < n; i++ {
    if a[i] < m {
      m = a[i]
      break
    }
  }
  fmt.Println(m)
}