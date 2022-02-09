package main

import (
  "fmt"
)

func sumInt(a ...int) int {s := 0; for _, v := range a {s += v}; return s}

func main() {
  var n int
  fmt.Scan(&n)
  a := make([]int, n)
  for i := 0; i < n; i++ {fmt.Scan(&a[i])}
  tot := sumInt(a...)
  if tot % n != 0 {
    fmt.Println(-1)
    return
  }
  unit := tot / n
  tmp := 0
  bridges := 0
  cnt := 0
  for _, p := range a {
    tmp += p
    cnt++
    if tmp % cnt == 0 && tmp / cnt == unit {
      tmp = 0
      cnt = 0
    } else {
      bridges++
    }
  }
  fmt.Println(bridges)
}
