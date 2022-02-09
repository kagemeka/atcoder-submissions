package main

import (
  "fmt"
)

func main() {
  var n string; fmt.Scan(&n)
  ans := "No"
  if n[1] == n[2] {
    if n[0] == n[1] || n[2] == n[3] {
      ans = "Yes"
    }
  }
  fmt.Println(ans)
}
