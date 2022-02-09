package main

import (
  "fmt"
)

func main() {
  var n int
  fmt.Scan(&n)
  a := make([]int, n)
  for i := 0; i < n; i++ {
    fmt.Scan(&a[i]); a[i]--
  }
  now := 0
  for i := 0; i < n; i++ {
    if now == 1 {
      fmt.Println(i)
      return
    }
    now = a[now]
  }
  fmt.Println(-1)
}
