package main

import (
  "fmt"
  "strconv"
)

func f(s string) int {
  tot := 0
  for _, d := range s {
    tot += int(d - '0')
  }
  return tot
}

func main() {
  var n int
  fmt.Scan(&n)
  ans := "No"
  if n % f(strconv.Itoa(n)) == 0 {
    ans = "Yes"
  }
  fmt.Println(ans)
}
