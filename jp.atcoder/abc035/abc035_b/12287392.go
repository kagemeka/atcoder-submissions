package main

import (
  "fmt"
)

func absInt(x int) int {if x >= 0 {return x}; return -x}

func main() {
  var s string
  var t int
  fmt.Scan(&s, &t)
  dy, dx, cnt := 0, 0, 0
  for _, c := range s {
    if c == 'L' {
      dx--
    } else if c == 'R' {
      dx++
    } else if c == 'D' {
      dy--
    } else if c == 'U'{
      dy++
    } else {
      cnt++
    }
  }
  d := absInt(dx) + absInt(dy)
  if t == 1 {
    fmt.Println(d + cnt)
  } else {
    d -= cnt
    if d < 0 {
      d &= 1
    }
    fmt.Println(d)
  }
}
