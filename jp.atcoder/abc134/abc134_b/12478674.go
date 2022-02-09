package main

import (
  "fmt"
)

func main() {
  var n, d int
  fmt.Scan(&n, &d)
  fmt.Println((n + 2*d) / (2*d + 1))
}
