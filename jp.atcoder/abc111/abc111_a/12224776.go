package main

import (
  "fmt"
)

func swapRunes(s string, a, b rune) string {
  runes := []rune(s)
  for i := 0; i < len(runes); i++ {
    if runes[i] == a {
      runes[i] = b
    } else {
      runes[i] = a
    }
  }
  return string(runes)
}

func main() {
  var n string
  fmt.Scan(&n)
  fmt.Println(swapRunes(n, '1', '9'))

}
