package main

import (
  "fmt"
)

func main() {
  var x, y string; fmt.Scan(&x, &y)
  var ans string
  if x < y {
    ans = "<"
  } else if x == y {
    ans = "="
  } else {
    ans = ">"
  }
  fmt.Println(ans)
}
