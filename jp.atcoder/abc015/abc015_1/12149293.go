package main

import (
  "fmt"
)

func main() {
  var a, b string
  fmt.Scan(&a, &b)
  var ans string
  if len(a) > len(b) {ans = a} else {ans = b}
  fmt.Println(ans)
}
