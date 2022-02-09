package main

import (
  "fmt"
  "strconv"
)

func main() {
  var a, b string
  fmt.Scan(&a, &b)
  c, _ := strconv.Atoi(a + b)
  fmt.Println(c * 2)
}
