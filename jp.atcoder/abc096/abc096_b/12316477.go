package main

import (
  "fmt"
  "sort"
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
  a := make([]int, 3)
  var k int
  for i := 0; i < 3; i++ {
    fmt.Scan(&a[i])
  }
  fmt.Scan(&k)
  sort.Ints(a)
  res := a[0] + a[1] + a[2] * pow(2, k)
  fmt.Println(res)

}
