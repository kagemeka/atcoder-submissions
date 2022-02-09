package main

import (
  "fmt"
)

func absInt(x int) int {if x >= 0 {return x}; return -x}
func gcd(a, b int) int {if (b == 0) {return absInt(a)}; return gcd(b, a % b)}
func lcm(a, b int) int {return absInt(a / gcd(a, b) * b)}

func main() {
  var a, b, c int
  fmt.Scan(&a, &b, &c)
  g := gcd(a, b)
  ans := "NO"
  if c % g == 0 {ans = "YES"}
  fmt.Println(ans)
}
