package main

import (
  "fmt"
)

var lucas = make([]int, 87)
func createLucas() {
  lucas[0] = 2
  lucas[1] = 1
  for i := 2; i < 87; i++ {
    lucas[i] = lucas[i-1] + lucas[i-2]
  }
}

func main() {
  createLucas()
  var n int
  fmt.Scan(&n)
  fmt.Println(lucas[n])

}
