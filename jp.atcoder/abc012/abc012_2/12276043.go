package main

import (
  "fmt"
  "strings"
  "strconv"
)

func divmod(a, b int) (int, int) {return a / b, a % b}

func main() {
  var n int
  fmt.Scan(&n)
  res := make([]int, 3)
  res[0] = n / 3600
  n %= 3600
  res[1], res[2] = divmod(n, 60)
  res2 := make([]string, 3)
  for i := 0; i < 3; i++ {
    res2[i] = strconv.Itoa(res[i])
    for len(res2[i]) < 2 {
      res2[i] = "0" + res2[i]
    }
  }
  fmt.Println(strings.Join(res2, ":"))
}
