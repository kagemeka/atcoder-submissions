package main

import (
  "fmt"
)

func main() {
  var n int
  fmt.Scan(&n)
  res := make(map[string]int)
  tot := 0
  for i := 0; i < n; i++ {
    var s string
    var p int
    fmt.Scan(&s, &p)
    tot += p
    res[s] = p
  }

  ans := "atcoder"
  for s, p := range res {
    if p > tot / 2 {
      ans = s
      break
    }
  }
  fmt.Println(ans)
}
