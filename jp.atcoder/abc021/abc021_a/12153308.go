package main

import (
  "fmt"
)

func main() {
  var n int; fmt.Scan(&n)
  var res []int
  for i := 0; i < 4; i++ {
    if n >> i & 1 == 1 {res = append(res, 1 << i)}
  }
  fmt.Println(len(res))
  for _, v := range res {fmt.Println(v)}
}
