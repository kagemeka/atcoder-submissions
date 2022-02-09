package main

import (
  "fmt"
)

func absInt(x int) int {if x >= 0 {return x}; return -x}
func gcd(a, b int) int {if (b == 0) {return absInt(a)}; return gcd(b, a % b)}
func lcm(a, b int) int {return a / gcd(a, b) * b}

func main() {
  var a, b, n int
  fmt.Scan(&a, &b, &n)
  l := lcm(a, b)
  fmt.Println((n + l - 1) / l * l)
}
