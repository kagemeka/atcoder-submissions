package main

import (
  "fmt"
)

var comb = make(map[[2]int]int)
func choose(n, r int) int {
  if r > n || r < 0 {return 0}
  if r == 0 {return 1}
  k := [2]int{n, r}
  if v, ok := comb[k]; ok {return v}
  comb[k] = choose(n-1, r) + choose(n-1, r-1)
  return comb[k]
}


func main() {
  var n, m int
  fmt.Scan(&n, &m)
  fmt.Println(choose(n, 2) + choose(m, 2))
}
