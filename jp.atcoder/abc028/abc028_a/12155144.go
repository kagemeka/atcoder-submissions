package main

import (
  "fmt"
)

func main() {
  var n int; fmt.Scan(&n)
  var res string
  switch {
  case n < 60:
    res = "Bad"
  case n < 90:
    res = "Good"
  case n < 100:
    res = "Great"
  default:
    res = "Perfect"
  }
  fmt.Println(res)
}
