package main

import (
  "fmt"
)

func main() {
  var c [3]string
  for i := 0; i < 3; i++ {fmt.Scan(&c[i])}
  res := ""
  for i := 0; i < 3; i++ {res += string(c[i][i])}
  fmt.Println(res)
}
