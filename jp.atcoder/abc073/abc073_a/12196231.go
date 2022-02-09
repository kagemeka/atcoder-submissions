package main

import (
  "fmt"
  "strings"
)

func main() {
  var n string
  fmt.Scan(&n)
  i := strings.Index(n, "9")
  ans := "Yes"; if i == -1 {ans = "No"}
  fmt.Println(ans)

}
