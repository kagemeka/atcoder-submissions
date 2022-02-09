package main

import (
  "fmt"
  "strings"
)

func main() {
  var n string
  fmt.Scan(&n)
  ans := "Yes"
  if strings.Index(n, "7") == -1 {
    ans = "No"
  }
  fmt.Println(ans)
}
