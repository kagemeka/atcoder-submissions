package main

import (
  "fmt"
  "math"
)

func maxInt(a ...int) int {m := a[0]; for _, x := range a {if x > m {m = x}}; return m}
func minInt(a ...int) int {m := a[0]; for _, x := range a {if x < m {m = x}}; return m}

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
  var x int
  fmt.Scan(&x)
  y := int(math.Sqrt(float64(x)))
  res := 1
  for b := 2; b < y + 1; b++ {
    for p := 2; ; p++ {
      if pow(b, p) > x {
        res = maxInt(res, pow(b, p - 1))
        break
      }
    }
  }
  fmt.Println(res)
}
