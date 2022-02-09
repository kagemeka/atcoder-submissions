package main

import (
  "fmt"
  "sort"
)

func sumInt(a ...int) int {s := 0; for _, v := range a {s += v}; return s}

func main() {
  var n, m int
  fmt.Scan(&n, &m)
  a := make([]int, n)
  for i := 0; i < n; i++ {
    fmt.Scan(&a[i])
  }
  sort.Ints(a)
  s := sumInt(a...)
  ans := "No"
  if a[n-m] * 4*m >= s {
    ans = "Yes"
  }
  fmt.Println(ans)


}
