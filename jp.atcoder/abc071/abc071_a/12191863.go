package main

import (
  "fmt"
)

func absInt(x int) int {if x >= 0 {return x}; return -x}

func main() {
  var x, a, b int
  fmt.Scan(&x, &a, &b)
  ans := "A"
  if absInt(a - x) > absInt(b - x) {ans = "B"}
  fmt.Println(ans)

}
