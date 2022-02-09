package main

import (
  "fmt"
)

func main() {
  var a, b, c, d int
  fmt.Scan(&a, &b, &c, &d)
  e := c - (d - b)
  f := d + (c - a)
  g := e - (f - d)
  h := f + (e - c)
  fmt.Println(e, f, g, h)
}
