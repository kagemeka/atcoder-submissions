package main

import (
  "fmt"
)

func main() {
  var a, b, c, k, s, t int
  fmt.Scan(&a, &b, &c, &k, &s, &t)
  res := a*s + b*t
  if s + t >= k {res -= c * (s + t)}
  fmt.Println(res)
}
