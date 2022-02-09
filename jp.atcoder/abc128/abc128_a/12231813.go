package main

import (
  "fmt"
)

func main() {
  var a, p int
  fmt.Scan(&a, &p)
  res := (3*a + p) / 2
  fmt.Println(res)
}
