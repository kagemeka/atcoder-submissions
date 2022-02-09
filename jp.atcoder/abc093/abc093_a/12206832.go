package main

import (
  "fmt"
  "sort"
)

type runeSlice []rune
func (p runeSlice) Len() int           { return len(p) }
func (p runeSlice) Less(i, j int) bool { return p[i] < p[j] }
func (p runeSlice) Swap(i, j int)      { p[i], p[j] = p[j], p[i] }
func sortedString(s string) string {
  runes := runeSlice([]rune(s))
  sort.Sort(runes)
  return string(runes)
}

func main() {
  var s string; fmt.Scan(&s)
  ans := "No"
  if sortedString(s) == "abc" {ans = "Yes"}
  fmt.Println(ans)
}
