package main

import (
  "fmt"
)

func main() {
  var a, b int; fmt.Scan(&a, &b)
  if a + b < 10 {fmt.Println(a + b)} else {fmt.Println("error")}
}
