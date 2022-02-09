package main

import (
  "fmt"
)

var cand = map[int]int{7:0, 5:0, 3:0}

func main() {
  var x int
  fmt.Scan(&x)
  ans := "NO"
  if _, ok := cand[x]; ok {ans = "YES"}
  fmt.Println(ans)

}
