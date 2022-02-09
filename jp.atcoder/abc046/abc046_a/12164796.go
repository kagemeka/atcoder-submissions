package main

import (
  "fmt"
)

func main() {
  res := make(map[int]int)
  for i := 0; i < 3; i++ {
    var a int; fmt.Scan(&a)
    res[a]++
  }
  fmt.Println(len(res))
}
