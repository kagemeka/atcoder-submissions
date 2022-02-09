package main

import (
  "fmt"
  "strings"
)

func main() {
  var h, w int
  fmt.Scan(&h, &w)
  board := make([]string, h + 2)
  board[0] = strings.Repeat("#", w + 2)
  board[h+1] = strings.Repeat("#", w + 2)
  for i := 1; i < h + 1; i++ {
    var s string
    fmt.Scan(&s)
    board[i] = "#" + s + "#"
  }
  for _, s := range board {
    fmt.Println(s)
  }
}
