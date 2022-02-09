package main

import (
  "fmt"
)

func areChained(s, t string) bool {return s[len(s)-1] == t[0]}

func main() {
  var a [3]string
  for i := 0; i < 3; i++ {fmt.Scan(&a[i])}
  ans := "YES"
  for i := 0; i < 2; i++ {
    if !areChained(a[i], a[i+1]) {
      ans = "NO"
      break
    }
  }
  fmt.Println(ans)
}
