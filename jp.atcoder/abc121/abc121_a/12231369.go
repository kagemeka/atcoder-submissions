package main

import (
  "fmt"
)

func main() {
  var H, W, h, w int
  fmt.Scan(&H, &W, &h, &w)
  s := H * W - (H*w + h*W - h*w)
  fmt.Println(s)
}
