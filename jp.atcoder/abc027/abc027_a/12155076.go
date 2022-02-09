package main

import (
  "fmt"
  "sort"
)

func main() {
  var l [3]int
  for i := 0; i < 3; i++ {fmt.Scan(&l[i])}
  sort.Ints(l[:])
  a := l[0]
  if l[0] == l[1] {a = l[2]}
  fmt.Println(a)
}
