package main

import (
  "fmt"
  "sort"
)

func main() {
  c := make([]int, 3)
  for i := 0; i < 3; i++ {fmt.Scan(&c[i])}
  sort.Ints(c)
  fmt.Println(c[0] + c[1])
}
