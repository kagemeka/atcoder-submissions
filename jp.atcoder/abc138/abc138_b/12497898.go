package main

import (
  "fmt"
)

func main() {
  var n int
  fmt.Scan(&n)
  a := make([]int, n)
  for i := 0; i < n; i++ {
    fmt.Scan(&a[i])
  }
  enum := 1
  for _, x := range a {enum *= x}
  denom := 0
  for _, x := range a {denom += enum / x}
  fmt.Println(float64(enum) / float64(denom))

}
