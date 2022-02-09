package main

import (
  "fmt"
)

func reversedString(s string) string {
  r := []rune(s)
  n := len(r)
  for i := 0; i < n / 2; i++ {
    r[i], r[n-1-i] = r[n-i-1], r[i]
  }
  return string(r)
}

func isPalindrome(s string) bool {
  return reversedString(s) == s
}

func main() {
  var s string
  fmt.Scan(&s)
  n := len(s)
  res := "No"
  if isPalindrome(s) && isPalindrome(s[:n/2]) {
    res = "Yes"
  }
  fmt.Println(res)
}
