package main

import (
  "fmt"
)

func main() {
  var x, a, b int;
  fmt.Scan(&x, &a, &b)
  y := -a + b
  var ans string
  if y <= 0 {
    ans = "delicious"
  } else if y <= x {
    ans = "safe"
  } else {
    ans = "dangerous"
  }
  fmt.Println(ans)
}
