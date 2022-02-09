package main

import (
  "fmt"
)

func absInt(x int) int {if x < 0 {x *= -1}; return x}

func main() {
  var n, l int
  fmt.Scan(&n, &l)
  s := (n - 1) * n / 2 + l * n
  m := 1001
  var res int
  for i := 0; i < n; i++ {
    a := absInt(l + i)
    if a < m {
      m = a
      res = l + i
    }
  }
  fmt.Println(s - res)

}
