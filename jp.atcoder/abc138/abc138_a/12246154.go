package main

import (
  "fmt"
)

func main() {
  var a int; var s string
  fmt.Scan(&a, &s)
  if a < 3200 {
    s = "red"
  }
  fmt.Println(s)
}
