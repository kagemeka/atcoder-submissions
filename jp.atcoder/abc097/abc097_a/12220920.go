package main

import (
  "fmt"
)

func absInt(x int) int {if x >= 0 {return x}; return -x}

func main() {
  var a, b, c, d int
  fmt.Scan(&a, &b, &c, &d)
  ans := "No"
  if absInt(c - a) <= d || (absInt(a - b) <= d && absInt(c - b) <= d) {
    ans = "Yes"
  }
  fmt.Println(ans)

}
