package main

import (
  "fmt"
)

func main() {
  var o, e string
  fmt.Scan(&o, &e)
  res := make([]byte, len(o) + len(e))
  for i := 0; i < len(o); i++ {
    res[2*i] = o[i]
  }
  for i := 0; i < len(e); i++ {
    res[1+2*i] = e[i]
  }
  fmt.Println(string(res))
}
