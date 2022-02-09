package main

import (
  "fmt"
)

func strongness(x int) int {return (x + 11) % 13}

func main() {
  var a, b int; fmt.Scan(&a, &b)
  a, b = strongness(a), strongness(b)
  var ans string
  if a > b {
    ans = "Alice"
  } else if a < b {
    ans = "Bob"
  } else {
    ans = "Draw"
  }
  fmt.Println(ans)
}
