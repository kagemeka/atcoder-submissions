package main

import (
  "fmt"
  "sort"
)

type data struct {
  s string
  v, id int
}

type datas []data

func (d datas) Len() int {return len(d)}
func (d datas) Less(i, j int) bool {
  if d[i].s == d[j].s {
    return d[i].v > d[j].v
  }
  return d[i].s < d[j].s
}
func (d datas) Swap(i, j int) {d[i], d[j] = d[j], d[i]}

func main() {
  var n int
  fmt.Scan(&n)
  d := make(datas, n)
  for i := 0; i < n; i++ {
    fmt.Scan(&d[i].s, &d[i].v)
    d[i].id = i + 1

  }
  sort.Sort(d)
  for i := 0; i < n; i++ {
    fmt.Println(d[i].id)
  }
}
