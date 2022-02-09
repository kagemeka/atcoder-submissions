package main

import (
  "fmt"
)

func main() {
  var a, b, c string
  fmt.Scan(&a, &b, &c)
  res := make(map[rune][]rune)
  res['a'] = []rune(a)
  res['b'] = []rune(b)
  res['c'] = []rune(c)
  nxt := 'a'
  for {
    p := nxt
    if len(res[p]) == 0 {
      fmt.Println(string(p - 32))
      return
    }
    nxt = res[p][0]
    res[p] = res[p][1:]
  }
}
