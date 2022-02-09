package main

import (
  "fmt"
  "sort"
  "strings"
)

func main() {
  var n, l int
  fmt.Scan(&n, &l)
  s := make([]string, n)
  for i := 0; i < n; i++ {
    fmt.Scan(&s[i])
  }
  sort.Sort(sort.StringSlice(s))
  fmt.Println(strings.Join(s, ""))
}
