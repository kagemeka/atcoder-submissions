package main

import (
  "fmt"
)

func main() {
  var n int
  fmt.Scan(&n)
  var ans string
  if n % 3 == 0 {ans = "YES"} else {ans = "NO"}
  fmt.Println(ans)
}
