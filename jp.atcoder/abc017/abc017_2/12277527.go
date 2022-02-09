package main

import (
  "fmt"
)

func substr(s string, l, r int) string {
  if l < 0 {l = 0}
  if r > len(s) {r = len(s)}
  if l >= r {return ""}
  runes := []rune(s)
  return string(runes[l:r])
}

func main() {
  choku := map[string]int{
    "ch": 0,
    "o": 0,
    "k": 0,
    "u": 0,
  }
  var x string
  fmt.Scan(&x)
  ans := "YES"
  for len(x) > 0 {
    n := len(x)
    if n >= 2 {
      if _, ok := choku[substr(x, n-2, n)]; ok {
        x = substr(x, 0, n-2)
        continue
      }
    }
    if _, ok := choku[string(x[n-1])]; ok {
      x = substr(x, 0, n-1)
      continue
    }
    ans = "NO"
    break
  }
  fmt.Println(ans)
}
