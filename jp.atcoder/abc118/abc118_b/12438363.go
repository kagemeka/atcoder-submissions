package main

import (
  "fmt"
)

func main() {
  var n, m int
  fmt.Scan(&n, &m)
  res := 1 << uint(m) - 1
  for i := 0; i < n; i++ {
    var k int
    fmt.Scan(&k)
    like := 0
    for j := 0; j < k; j++ {
      var a uint
      fmt.Scan(&a); a--
      like |= 1 << a
    }
    res &= like
  }
  cnt := 0
  for i := uint(0); i < m; i++ {
    if res >> i & 1 == 1 {cnt++}
  }
  fmt.Println(cnt)

}
