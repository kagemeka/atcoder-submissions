package main

import (
  "fmt"
)

func main() {
  var n int
  fmt.Scan(&n)
  res := "APPROVED"
  for i := 0; i < n; i++ {
    var a int
    fmt.Scan(&a)
    if a & 1 == 1 {continue}
    if a % 3 != 0 && a % 5 != 0 {
      res = "DENIED"
    }
  }
  fmt.Println(res)
}
