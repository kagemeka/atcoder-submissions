package main

import (
  "fmt"
)

func main() {
  var a, d int; fmt.Scan(&a, &d)
  if a <= d {a++} else {d++}
  fmt.Println(a * d)

}
