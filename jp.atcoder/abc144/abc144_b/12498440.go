package main

import (
  "fmt"
)

func main() {
  var n int
  fmt.Scan(&n)
  for i := 1; i < 10; i++ {
    j := n / i
    if j >= 1 && j < 10 && i * j == n {
      fmt.Println("Yes")
      return
    }
  }
  fmt.Println("No")
}
