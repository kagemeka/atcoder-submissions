package main

import (
  "fmt"
)

func main() {
  var n int
  fmt.Scan(&n)
  s := 0
  for i := 1; i <= n; i++ {
    if i % 3 != 0 && i % 5 != 0 {
      s += i
    }
  }
  fmt.Println(s)
}
