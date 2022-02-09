package main

import (
  "fmt"
)

func main() {
  var q int
  fmt.Scan(&q)
  var ans string
  if q == 1 {ans = "ABC"} else {ans = "chokudai"}
  fmt.Println(ans)
}
