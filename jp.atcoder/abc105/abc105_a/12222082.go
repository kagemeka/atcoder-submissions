package main

import (
  "fmt"
)

func main() {
  var n, k int
  fmt.Scan(&n, &k)
  ans := 0
  if n % k != 0 {
    ans = 1
  }
  fmt.Println(ans)
}
