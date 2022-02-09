package main

import (
  "fmt"
)

func main() {
  var n string; fmt.Scan(&n)

  res := make(map[byte]int)
  for i := 0; i < 4; i++ {
    res[n[i]]++
  }
  ans := "SAME"; if len(res) > 1 {ans = "DIFFERENT"}
  fmt.Println(ans)
}
