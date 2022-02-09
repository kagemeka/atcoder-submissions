package main

import (
  "fmt"
)

func main() {
  var board [4][4]string
  for i := 0; i < 4; i++ {
    for j := 0; j < 4; j++ {
      fmt.Scan(&board[i][j])
    }
  }
  for i := 3; i > -1; i-- {
    for j := 3; j > -1; j-- {
      fmt.Print(board[i][j])
      tail := " "
      if j == 0 {tail = "\n"}
      fmt.Print(tail)
    }
  }
}
