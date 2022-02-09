package main

import (
  "fmt"
)

func divmod(a, b int) (int, int) {return a / b, a % b}

func main() {
  var x int
  fmt.Scan(&x)
  q, r := divmod(x, 500)
  res := 1000 * q + r / 5 * 5
  fmt.Println(res)

}
