package main

import (
  "fmt"
  "sort"
)

type Person struct {
  Score, Index int
}

func main() {
  var res []Person
  for i := 0; i < 3; i++ {
    var s int
    fmt.Scan(&s)
    res = append(res, Person{s, i + 1})
  }
  sort.Slice(res, func(i, j int) bool {return res[i].Score > res[j].Score})
  for i := 0; i < 3; i++ {
    fmt.Println(res[i].Index)
  }
}
