package main

import (
  "fmt"
  "sort"
)

func main() {
  a := make([]int, 3)
  for i := 0; i < 3; i++ {
    fmt.Scan(&a[i])
  }
  sort.Sort(sort.Reverse(sort.IntSlice(a)))
  fmt.Println(a[0]*10 + a[1] + a[2])
}
