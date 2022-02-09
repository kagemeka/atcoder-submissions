package main

import (
  "fmt"
)

func main() {
  var s string
  fmt.Scan(&s)
  res := "Yes"
  for i, c := range s {
    if i & 1 == 0 {
      if c == 'L' {
        res = "No"
        break
      }
    } else {
      if c == 'R' {
        res = "No"
        break
      }
    }
  }
  fmt.Println(res)
}
