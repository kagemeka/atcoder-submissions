package main

import (
  "fmt"
  "strconv"
)

func main() {
  var h, w int
  fmt.Scan(&h, &w)

  grid := make([]string, h)
  for i := 0; i < h; i++ {
    fmt.Scan(&grid[i])
  }
  var cnt [51][51]int
  for i := 0; i < h; i++ {
    for j := 0; j < w; j++ {
      if grid[i][j] == '.' {continue}
      for dy := -1; dy < 2; dy++ {
        for dx := -1; dx < 2; dx++ {
          y, x := i + dy, j + dx
          if y < 0 || x < 0 {continue}
          cnt[y][x]++
        }
      }
    }
  }
  for i := 0; i < h; i++ {
    for j := 0; j < w; j++ {
      if grid[i][j] == '#' {
        fmt.Print("#")
      } else {
        fmt.Print(strconv.Itoa(cnt[i][j]))
      }
    }
    fmt.Print("\n")
  }
}
