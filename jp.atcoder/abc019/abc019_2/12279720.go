package main

import (
  "fmt"
  "strconv"
)

func main() {
  var s string
  fmt.Scan(&s)
  n := len(s)
  s += "$"
  prev := s[0]
  cnt := 0
  res := ""
  for i := 0; i < n + 1; i++ {
    if s[i] == prev {
      cnt++
    } else {
      res += string(prev) + strconv.Itoa(cnt)
      cnt = 1
    }
    prev = s[i]
  }
  fmt.Println(res)
}
