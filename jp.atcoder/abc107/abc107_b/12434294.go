package main

import (
  "fmt"
)

func main() {
  var h, w int
  fmt.Scan(&h, &w)
  res := make([]string, 0)
  for i := 0; i < h; i++ {
    var s string
    fmt.Scan(&s)
    for j := 0; j < w; j++ {
      if s[j] == '#' {
        res = append(res, s)
        break
      }
    }
  }
  h = len(res)
  res2 := make([]string, 0)
  for j := 0; j < w; j++ {
    s := ""
    for i := 0; i < h; i++ {
      s += string(res[i][j])
    }
    for i := 0; i < h; i++ {
      if s[i] == '#' {
        res2 = append(res2, s)
        break
      }
    }
  }
  w = len(res2)
  for j := 0; j < h; j++ {
    for i := 0; i < w; i++ {
      fmt.Print(string(res2[i][j]))
    }
    fmt.Print("\n")
  }
}
