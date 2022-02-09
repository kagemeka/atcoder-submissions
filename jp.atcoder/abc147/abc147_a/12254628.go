package main

import (
  "fmt"
)

func sumInt(a ...int) int {s := 0; for _, v := range a {s += v}; return s}

func main() {
  a := make([]int, 3)
  for i := 0; i < 3; i++ {
    fmt.Scan(&a[i])
  }
  if sumInt(a...) < 22 {
    fmt.Println("win")
  } else {
    fmt.Println("bust")
  }
}
