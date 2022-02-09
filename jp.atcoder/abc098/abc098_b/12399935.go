package main

import (
  "fmt"
)

func maxInt(a ...int) int {m := a[0]; for _, x := range a {if x > m {m = x}}; return m}
func minInt(a ...int) int {m := a[0]; for _, x := range a {if x < m {m = x}}; return m}

func main() {
  var n int
  var s string
  fmt.Scan(&n, &s)
  l := make([]int, n); l[0] |= 1 << uint(s[0] - 'a')
  r := make([]int, n); r[n-1] |= 1 << uint(s[n-1] - 'a')
  for i := 0; i < n - 1; i++ {
    l[i+1] = l[i] | (1 << uint(s[i+1] - 'a'))
  }
  for i := n - 1; i > 0; i-- {
    r[i-1] = r[i] | (1 << uint(s[i-1] - 'a'))
  }

  ans := 0
  for i := 0; i < n - 1; i++ {
    res := l[i] & r[i+1]
    cnt := 0
    for j := uint(0); j < 26; j++ {
      if res >> j & 1 == 1 {
        cnt++
      }
    }
    ans = maxInt(ans, cnt)
  }
  fmt.Println(ans)
}
