package main

import (
  "fmt"
)

func main() {
  res := make(map[string]int)
  var n int
  fmt.Scan(&n)
  for i := 0; i < n; i++ {
    var s string
    fmt.Scan(&s)
    res[s]++
  }
  m := 0
  var ans string
  for name, c := range res {
    if c > m {
      m = c
      ans = name
    }
  }
  fmt.Println(ans)
}
