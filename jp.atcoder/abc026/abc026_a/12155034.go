package main

import (
  "fmt"
)

func main() {
  var a int
  fmt.Scan(&a)
  var x, y int
  x = a / 2; y = a - x
  fmt.Println(x * y)
}
