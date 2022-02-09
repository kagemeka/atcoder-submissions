package main

import (
  "fmt"
)

func f(n int) int {
  s := 0
  for n > 0 {
    s += n % 10
    n /= 10
  }
  return s
}

func main() {
  var n, a, b int
  fmt.Scan(&n, &a, &b)
  tot := 0
  for i := 1; i < n + 1; i++ {
    if s := f(i); s >= a && s <= b {
      tot += i
    }
  }
  fmt.Println(tot)
}
