package main

import (
  "fmt"
)

func main() {
  var x string
  fmt.Scan(&x)
  fmt.Println(x[0] - '0' + x[1] - '0')
}
