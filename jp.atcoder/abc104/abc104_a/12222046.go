package main

import (
  "fmt"
)

func main() {
  var r int
  fmt.Scan(&r)
  var ans string
  if r < 1200 {
    ans = "ABC"
  } else if r < 2800 {
    ans = "ARC"
  } else {
    ans = "AGC"
  }
  fmt.Println(ans)
}
