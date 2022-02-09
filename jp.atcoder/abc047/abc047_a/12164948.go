package main

import (
  "fmt"
  "sort"
)

func sumInt(a []int) int {
  s := 0
  for _, v := range a {s += v}
  return s
}

func main() {
  var c [3]int
  for i := 0; i < 3; i++ {fmt.Scan(&c[i])}
  sort.Ints(c[:])
  ans := "No"; if sumInt(c[:2]) == c[2] {ans = "Yes"}
  fmt.Println(ans)
}
