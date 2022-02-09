package main

import (
  "fmt"
)

func main() {
  var n int
  fmt.Scan(&n)
  m := n
  s := 0
  for n > 0 {
    s += n % 10
    n /= 10
  }
  ans := "No"
  if m % s == 0 {
    ans = "Yes"
  }
  fmt.Println(ans)
}
