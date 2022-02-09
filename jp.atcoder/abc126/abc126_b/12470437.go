package main

import (
  "fmt"
  "strconv"
)

func stoi(s string) int {
  d, _ := strconv.Atoi(s)
  return d
}

func main() {
  var s string
  fmt.Scan(&s)
  a, b := stoi(s[:2]), stoi(s[2:])
  fmt.Println(a, b)
  bl1 := a >= 1 && a <= 12
  bl2 := b >= 1 && b <= 12
  var res string
  if bl1 {
    if bl2 {
      res = "AMBIGUOUS"
    } else {
      res = "MMYY"
    }
  } else {
    if bl2 {
      res = "YYMM"
    } else {
      res = "NA"
    }
  }
  fmt.Println(res)
}
