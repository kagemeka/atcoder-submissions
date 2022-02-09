package main

import (
  "fmt"
)

func main() {
  var s string
  fmt.Scan(&s)
  res := make(map[rune]bool)
  for _, c := range s {res[c] = true}
  ans := "None"
  for i := 'a'; i < 'z' + 1; i++ {
    if _, ok := res[i]; !ok {
      ans = string(i)
      break
    }
  }
  fmt.Println(ans)
}
