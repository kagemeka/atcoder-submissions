package main

import (
  "fmt"
)

func main() {
  var n int
  var s string
  fmt.Scan(&n, &s)
  if n & 1 == 0 {
    fmt.Println(-1)
    return
  }
  m := (n - 1) / 2
  verdict := []rune{'c', 'a', 'b'}
  i := 2 - m % 3
  for _, c := range s {
    if c == verdict[i] {
      i = (i + 1) % 3
      continue
    }
    fmt.Println(-1)
    return
  }
  fmt.Println(m)
}
