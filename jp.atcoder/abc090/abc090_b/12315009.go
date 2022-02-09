package main

import (
  "fmt"
  "strconv"
)

func main() {
  var a, b int
  fmt.Scan(&a, &b)
  cnt := 0
  for i := a; i <= b; i++ {
    j := strconv.Itoa(i)
    flag := true
    for k := 0; k < 2; k++ {
      if j[k] == j[4-k] {continue}
      flag = false; break
    }
    if flag {
      cnt++
    }
  }
  fmt.Println(cnt)
}
