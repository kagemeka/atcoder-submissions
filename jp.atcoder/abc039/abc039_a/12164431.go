package main

import (
  "fmt"
)

func main() {
  var a, b, c int; fmt.Scan(&a, &b, &c)
  s := 2 * (a*b + b*c + c*a)
  fmt.Println(s)
}
