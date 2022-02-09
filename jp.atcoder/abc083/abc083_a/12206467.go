package main

import (
  "fmt"
)

func main() {
  var a, b, c, d int
  fmt.Scan(&a, &b, &c, &d)
  l, r := a + b, c + d
  var ans string
  if l == r {
    ans = "Balanced"
  } else if l > r {
    ans = "Left"
  } else {
    ans = "Right"
  }
  fmt.Println(ans)
}
