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
  sort.Ints(a)
  fmt.Println(a[2] - a[0])
}
