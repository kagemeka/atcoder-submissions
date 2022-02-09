package main

import (
  "fmt"
)

func main() {
  var a, b, c, d, e, f float64
  fmt.Scan(&a, &b, &c, &d)
  e, f = b / a, d / c
  var ans string
  if e > f {
    ans = "TAKAHASHI"
  } else if e == f {
    ans = "DRAW"
  } else {
    ans = "AOKI"
  }
  fmt.Println(ans)
}
