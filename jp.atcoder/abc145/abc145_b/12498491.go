package main

import (
  "fmt"
)

func main() {
  res := "Yes"
  var n int
  var s string
  fmt.Scan(&n, &s)
  if n & 1 == 1 {
    res = "No"
  } else {
    t := s[:n/2]
    if t + t != s {
      res = "No"
    }
  }
  fmt.Println(res)

}
