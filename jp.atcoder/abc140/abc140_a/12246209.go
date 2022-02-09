package main

import (
  "fmt"
)

func pow(args ...int) int {
  x, y := args[0], args[1]
  res := 1
  if len(args) == 3 {
    mod := args[2]
    for y != 0 {
      if y & 1 == 1 {res = res * x % mod}
      y >>= 1
      x = x * x % mod
    }
  }  else {
    for y != 0 {
      if y & 1 == 1 {res *= x}
      y >>= 1
      x *= x
    }
  }
  return res
}

func main() {
  var n int
  fmt.Scan(&n)
  fmt.Println(pow(n, 3))
}