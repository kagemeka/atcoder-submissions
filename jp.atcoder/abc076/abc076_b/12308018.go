package main

import (
  "fmt"
)

func main() {
  var n, k int
  fmt.Scan(&n, &k)
  res := 1
  for i := 0; i < n; i++ {
    if res <= k {
      res *= 2
    } else {
      res += k
    }
  }
  fmt.Println(res)
}
