package main

import (
  "fmt"
)

func main() {
  var w, h int; fmt.Scan(&w, &h)
  ans := "16:9"; if w*3 == h*4 {ans = "4:3"}
  fmt.Println(ans)
}
