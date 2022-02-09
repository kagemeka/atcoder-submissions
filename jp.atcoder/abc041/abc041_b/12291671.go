package main

import (
  "fmt"
)

const mod = 1e9+7

func main() {
  var a, b, c int
  fmt.Scan(&a, &b, &c)
  fmt.Println(a*b%mod*c%mod)
}
