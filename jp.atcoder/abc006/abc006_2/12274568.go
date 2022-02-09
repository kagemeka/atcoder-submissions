package main

import (
  "fmt"
)

const mod = 10007

var tribonacci[2e7]int
func create() {
  tribonacci[0] = 0
  tribonacci[1] = 0
  tribonacci[2] = 1
  for i := 3; i < 2e7; i++ {
    tribonacci[i] = tribonacci[i-1] + tribonacci[i-2] + tribonacci[i-3]
    tribonacci[i] %= mod
  }
}

func main() {
  create()
  var n int
  fmt.Scan(&n)
  fmt.Println(tribonacci[n-1])
}
