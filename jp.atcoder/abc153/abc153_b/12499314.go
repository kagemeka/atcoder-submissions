package main

import (
  "fmt"
)

func main() {
  var h, n int
  fmt.Scan(&h, &n)
  s := 0
  for i := 0; i < n; i++ {
    var a int
    fmt.Scan(&a)
    s += a
  }
  res := "No"
  if s >= h {res = "Yes"}
  fmt.Println(res)
}
