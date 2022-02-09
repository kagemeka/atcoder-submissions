package main

import (
  "fmt"
)

func main() {
  var s, t, u string
  var a, b int
  fmt.Scan(&s, &t, &a, &b, &u)
  if u == s {
    a--
  } else {
    b--
  }
  fmt.Println(a, b)
}
