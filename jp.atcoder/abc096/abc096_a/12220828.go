package main

import (
  "fmt"
)

func main() {
  var a, b int;
  fmt.Scan(&a, &b)
  ans := a; if a > b {ans--}
  fmt.Println(ans)
}
