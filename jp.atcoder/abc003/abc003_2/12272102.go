package main

import (
  "fmt"
)


var set = make(map[byte]bool)

func create(s string) {
  n := len(s)
  for i := 0; i < n; i++ {
    set[s[i]] = true
  }
}

func isOk(s, t byte) bool {
  if _, ok := set[t]; s == '@' && ok {
    return true
  }
  return false
}

func main() {
  create("atcoder")
  var s, t string
  fmt.Scan(&s, &t)
  n := len(s)
  ans := "You can win"
  for i := 0; i < n; i++ {
    if s[i] == t[i] {continue}
    if isOk(s[i], t[i]) || isOk(t[i], s[i]) {
      continue
    }
    ans = "You will lose"
    break
  }
  fmt.Println(ans)
}
