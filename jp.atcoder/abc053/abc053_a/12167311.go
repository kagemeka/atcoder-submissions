package main

import (
  "fmt"
)

func main() {
  var x int; fmt.Scan(&x)
  var ans string = "ABC"
  if x >= 1200 {ans = "ARC"}
  fmt.Println(ans)
}
