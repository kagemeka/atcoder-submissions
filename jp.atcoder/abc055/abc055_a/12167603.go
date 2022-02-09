package main

import (
  "fmt"
)

func main() {
  var n int; fmt.Scan(&n)
  fmt.Println(800 * n - 200 * (n / 15))
}
