package main

import (
  "fmt"
)

func main() {
  var n, a int; fmt.Scan(&n, &a)
  n %= 500
  ans := "No";
  if a >= n {ans = "Yes"}
  fmt.Println(ans)
}
