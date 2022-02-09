package main

import (
  "fmt"
)

func main() {
  var n int
  fmt.Scan(&n)
  a := make([]int, n)
  b := make([]int, n)
  c := make([]int, n-1)
  for i := 0; i < n; i++ {fmt.Scan(&a[i]); a[i]--}
  for i := 0; i < n; i++ {fmt.Scan(&b[i])}
  for i := 0; i < n-1; i++ {fmt.Scan(&c[i])}
  prev := -100
  res := 0
  for _, x := range a {
    res += b[x]
    if prev == x - 1 {res += c[prev]}
    prev = x
  }
  fmt.Println(res)
}
