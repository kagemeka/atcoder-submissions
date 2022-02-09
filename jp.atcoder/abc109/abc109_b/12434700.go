package main

import (
  "fmt"
)

func main() {
  var n int
  fmt.Scan(&n)
  w := make([]string, n)
  for i := 0; i < n; i++ {
    fmt.Scan(&w[i])
  }
  used := make(map[string]bool)
  prev := w[0]
  used[prev] = true
  ans := "Yes"
  for i := 2; i < n; i++ {
    nxt := w[i]
    if nxt[0] != prev[len(prev)-1] {
      ans = "No"
      break
    }
    if _, ng := used[nxt]; ng {
      ans = "No"
      break
    }
    prev = nxt
    used[prev] = true
  }
  fmt.Println(ans)
}
