package main

import (
  "fmt"
)

func main() {
  var k, x int
  fmt.Scan(&k, &x)
  ans := "No"
  if 500*k >= x {ans = "Yes"}
  fmt.Println(ans)
}
