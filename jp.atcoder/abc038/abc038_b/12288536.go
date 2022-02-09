package main

import (
  "fmt"
)

func main() {
  var d [2][2]int
  for i := 0; i < 2; i++ {
    for j := 0; j < 2; j++ {
      fmt.Scan(&d[i][j])
    }
  }

  ans := "NO"
  for i := 0; i < 2; i++ {
    for j := 0; j < 2; j++ {
      if d[0][i] == d[1][j] {
        ans = "YES"
        break
      }
    }
  }
  fmt.Println(ans)

}
