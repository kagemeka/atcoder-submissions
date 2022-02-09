package main

import (
  "fmt"
)

func main() {
  var n, m int
  fmt.Scan(&n, &m)
  board := make([]string, n)
  target := make([]string, m)
  for i := 0; i < n; i++ {
    fmt.Scan(&board[i])
  }
  for i := 0; i < m; i++ {
    fmt.Scan(&target[i])
  }

  for i := 0; i < n - m + 1; i++ {
    for j := 0; j < n - m + 1; j++ {
      flag := false
      for dy := 0; dy < m; dy++ {
        for dx := 0; dx < m; dx++ {
          if board[i+dy][j+dx] != target[dy][dx] {
            flag = true
            break
          }
        }
        if flag {break}
      }
      if flag {continue}
      fmt.Println("Yes")
      return
    }
  }
  fmt.Println("No")
}
