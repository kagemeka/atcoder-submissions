package main

import (
  "fmt"
  "sort"
)

func main() {
  var res [][]int
  for i := 0; i < 3; i++ {
    var s int
    fmt.Scan(&s)
    res = append(res, []int{s, i + 1})
  }
  sort.Slice(res, func(i, j int) bool {return res[i][0] > res[j][0]})
  for i := 0; i < 3; i++ {
    fmt.Println(res[i][1])
  }
}
