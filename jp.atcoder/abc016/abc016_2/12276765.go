package main

import (
  "fmt"
)

func main() {
  var a, b, c int
  fmt.Scan(&a, &b, &c)
  var bl1, bl2 bool
  bl1 = a + b == c
  bl2 = a - b == c
  var ans string
  if bl1 {
    if bl2 {
      ans = "?"
    } else {
      ans = "+"
    }
  } else {
    if bl2 {
      ans = "-"
    } else {
      ans = "!"
    }
  }
  fmt.Println(ans)
}
