package main

import (
  "fmt"
)

func main() {
  var l, h, n int
  fmt.Scan(&l, &h, &n)
  for i := 0; i < n; i++ {
    var a int
    fmt.Scan(&a)
    ans := -1
    if a <= l {
      ans = l - a
    } else if a <= h {
      ans = 0
    }
    fmt.Println(ans)
  }
}
