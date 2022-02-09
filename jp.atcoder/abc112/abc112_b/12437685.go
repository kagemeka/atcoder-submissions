package main

import (
  "fmt"
  "sort"
)

type pairIntSlice [][2]int
func (p pairIntSlice) Len() int {return len(p)}
func (p pairIntSlice) Less(i, j int) bool {return p[i][0] <= p[j][0]}
func (p pairIntSlice) Swap(i, j int) {p[i], p[j] = p[j], p[i]}

func main() {
  var n, t int
  fmt.Scan(&n, &t)
  ct := make(pairIntSlice, n)
  for i := 0; i < n; i++ {
    fmt.Scan(&ct[i][0], &ct[i][1])
  }
  // sort.Slice(ct, func(i, j int) bool {return ct[i][0] <= ct[j][0]})
  sort.Sort(ct)
  for i := 0; i < n; i++ {
    if ct[i][1] <= t {
      fmt.Println(ct[i][0])
      return
    }
  }
  fmt.Println("TLE")
}
