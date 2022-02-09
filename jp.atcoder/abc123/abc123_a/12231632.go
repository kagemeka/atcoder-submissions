package main

import (
  "fmt"
  "sort"
)

func main() {
  x := make([]int, 5)
  for i := 0; i < 5; i++ {
    fmt.Scan(&x[i])
  }
  var k int
  fmt.Scan(&k)
  sort.Ints(x)
  ans := ":("
  if x[4] - x[0] <= k {
    ans = "Yay!"
  }
  fmt.Println(ans)
}
