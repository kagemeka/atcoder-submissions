package main

import (
  "fmt"
  "sort"
)

func main() {
  var a = make([]int, 3)
  for i := 0; i < 3; i++ {fmt.Scan(&a[i])}
  sort.Ints(a)
  var ans int
  if a[0] == a[1] {
    ans = a[2]
  } else {
    ans = a[0]
  }
  fmt.Println(ans)
}
