package main

import (
  "fmt"
  "sort"
)
func biL(a []int, x int) int {return sort.SearchInts(a, x)}
func biR(a []int, x int) int {return sort.Search(len(a), func(i int) bool {return a[i] > x})}

func main() {
  var n int
  fmt.Scan(&n)
  cand := []int{105, 165, 195, 135, 189}
  sort.Ints(cand)
  fmt.Println(biR(cand, n))
}
