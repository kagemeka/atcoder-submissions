package main

import (
  "fmt"
)

func main() {
  var s, t string
  fmt.Scan(&s, &t)
  rs := []rune(s)
  n := len(rs)
  ans := "No"
  for i := 0; i < n; i++ {
    if string(rs) == t {
      ans = "Yes"
      break
    }
    rs = append(rs[n-1:], rs[:n-1]...)
  }
  fmt.Println(ans)

}
