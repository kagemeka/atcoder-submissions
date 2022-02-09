package main

import (
  "fmt"
  "strconv"
)

func main() {
  var m float64
  fmt.Scan(&m)
  m *= 0.001
  if m < 0.1 {
    m = 0
  } else if m <= 5 {
    m *= 10
  } else if m <= 30 {
    m += 50
  } else if m <= 70 {
    m = (m - 30) / 5 + 80
  } else {
    m = 89
  }

  res := strconv.Itoa(int(m))
  if len(res) == 1 {
    res = "0" + res
  }
  fmt.Println(res)
}
