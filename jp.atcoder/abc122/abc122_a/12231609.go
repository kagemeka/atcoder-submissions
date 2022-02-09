package main

import (
  "fmt"
)

func makePair() map[byte]byte {
  acgt := []byte("ACGT")
  pair := make(map[byte]byte)
  for i := 0; i < 4; i++ {
    pair[acgt[i]] = acgt[3-i]
  }
  return pair
}

func main() {
  pair := makePair()
  var b string
  fmt.Scan(&b)
  fmt.Println(string(pair[[]byte(b)[0]]))
}
