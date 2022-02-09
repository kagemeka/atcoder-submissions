package main

import (
  "fmt"
  "strings"
)

func main() {
  var d int
  fmt.Scan(&d)
  ans := "Christmas"
  tail := " Eve"
  ans += strings.Repeat(tail, 25 - d)
  fmt.Println(ans)
}
