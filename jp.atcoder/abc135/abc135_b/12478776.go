package main

import (
  "fmt"
)

func main() {
  var n int
  fmt.Scan(&n)
  cnt := 0
  for i := 0; i < n; i++ {
    var x int
    fmt.Scan(&x)
    if x != i + 1 {cnt++}
  }
  ans := "NO"
  if cnt == 0 || cnt == 2 {ans = "YES"}
  fmt.Println(ans)
}
