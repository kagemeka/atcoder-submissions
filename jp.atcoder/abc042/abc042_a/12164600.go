package main

import (
  "fmt"
  "sort"
)

func main() {
  var s [3]int;
  for i := 0; i < 3; i++ {fmt.Scan(&s[i])}
  sort.Ints(s[:])
  ans := "NO"
  if s[0] == 5 && s[1] == 5 && s[2] == 7 {ans = "YES"}
  fmt.Println(ans)
}
