package main

import (
  "fmt"
)

func main() {
  var a, b int
  fmt.Scan(&a, &b)
  var fee int
  if a > 12 {
    fee = b
  } else if a > 5 {
    fee = b / 2
  } else {
    fee = 0
  }
  fmt.Println(fee)
}
