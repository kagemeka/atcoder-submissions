package main

import (
  "fmt"
)

func main() {
  var k int
  fmt.Scan(&k)
  x := k / 2
  fmt.Println(x * (k - x))
}
