package main

import (
  "fmt"
)

func main() {
  var a, b, c, x int
  fmt.Scan(&a, &b, &c, &x)
  x /= 50
  cnt := 0
  for i := 0; i < a + 1; i++ {
    for j := 0; j < b + 1; j++ {
      k := x - 10*i - 2*j
      if k >= 0 && k <= c {cnt++}
    }
  }
  fmt.Println(cnt)


}
