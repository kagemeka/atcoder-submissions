package main

import (
  "fmt"
  "sort"
)

func biL(a []int, x int) int {return sort.SearchInts(a, x)}
func biR(a []int, x int) int {return sort.Search(len(a), func(i int) bool {return a[i] > x})}

func maxInt(a ...int) int {m := a[0]; for _, x := range a {if x > m {m = x}}; return m}
func minInt(a ...int) int {m := a[0]; for _, x := range a {if x < m {m = x}}; return m}

func main() {
  var n, m, x int
  fmt.Scan(&n, &m, &x)
  a := make([]int, m)
  for i := 0; i < m; i++ {
    fmt.Scan(&a[i])
  }
  i := biL(a, x)
  fmt.Println(minInt(i, m - i))
}
