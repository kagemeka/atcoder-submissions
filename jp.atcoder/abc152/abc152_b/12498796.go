package main

import (
  "fmt"
  "strings"
  "strconv"
)

func main() {
  var a, b int
  fmt.Scan(&a, &b)
  var res string
  if a <= b {
    res = strings.Repeat(strconv.Itoa(a), b)
  } else {
    res = strings.Repeat(strconv.Itoa(b), a)
  }

  fmt.Println(res)

}
