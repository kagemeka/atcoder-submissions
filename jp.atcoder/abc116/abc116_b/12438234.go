package main

import (
  "fmt"
)

func main() {
  var n int
  fmt.Scan(&n)
  for i := 0; i < 1e6; i++ {
    if n == 1 || n == 2 || n == 4 {
      fmt.Println(i + 4)
      return
    }
    if n & 1 == 1 {
      n = 3*n + 1
    } else {
      n /= 2
    }
  }
}
