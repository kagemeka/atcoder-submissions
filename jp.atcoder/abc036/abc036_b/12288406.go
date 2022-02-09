package main

import (
  "fmt"
  "strings"
)

func main() {
  var n int
  fmt.Scan(&n)
  board := make([][]string, n)
  for i := 0; i < n; i++ {
    var s string
    fmt.Scan(&s)
    board[i] = strings.Split(s, "")
  }
  newboard := make([][]string, n)
  for j := 0; j < n; j++ {
    for i := n - 1; i > -1; i-- {
      newboard[j] = append(newboard[j], board[i][j])
    }
  }
  for i := 0; i < n; i++ {
    fmt.Println(strings.Join(newboard[i], ""))
  }
}
