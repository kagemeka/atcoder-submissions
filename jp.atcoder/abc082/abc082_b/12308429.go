package main

import (
  "fmt"
  "sort"
)

type runeSlice []rune
func (p runeSlice) Len() int           { return len(p) }
func (p runeSlice) Less(i, j int) bool { return p[i] < p[j] }
func (p runeSlice) Swap(i, j int)      { p[i], p[j] = p[j], p[i] }
func reverseSortRuneSlice(a []rune) {sort.Sort(sort.Reverse(runeSlice(a)))}

func main() {
  var s, t string
  fmt.Scan(&s, &t)
  rs := []rune(s)
  rt := []rune(t)
  reverseSortRuneSlice(rt)
  sort.Sort(runeSlice(rs))
  ans := "No"
  if string(rs) < string(rt) {ans = "Yes"}
  fmt.Println(ans)
}
