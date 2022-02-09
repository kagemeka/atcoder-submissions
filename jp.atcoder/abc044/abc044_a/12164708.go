package main

import (
  "fmt"
)

func main() {
  var n, k, x, y int
  fmt.Scan(&n, &k, &x, &y)
  var fee int
  if n <= k {fee = x * n} else {fee = x*k + y*(n-k)}
  fmt.Println(fee)
}
