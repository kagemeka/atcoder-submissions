package main

import (
  "fmt"
)

func main() {
  var m, d int
  fmt.Scan(&m, &d)
  ans := "NO"
  if m % d == 0 {ans = "YES"}
  fmt.Println(ans)
}
