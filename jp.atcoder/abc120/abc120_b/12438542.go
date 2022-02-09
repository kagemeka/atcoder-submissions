package main

import (
  "fmt"
  "sort"
  "math"
)

func divisors(n int) []int {
  res := make([]int, 0)
  for i := 1; i < int(math.Sqrt(float64(n)))+1; i++ {
    if n % i == 0 {
      res = append(res, i)
      if n / i != i {
        res = append(res, n/i)
      }
    }
  }
  sort.Ints(res)
  return res
}

func absInt(x int) int {if x >= 0 {return x}; return -x}
func gcd(a, b int) int {if (b == 0) {return absInt(a)}; return gcd(b, a % b)}
func lcm(a, b int) int {return absInt(a / gcd(a, b) * b)}

func main() {
  var a, b, k int
  fmt.Scan(&a, &b, &k)
  cand := divisors(gcd(a, b))
  fmt.Println(cand[len(cand)-k])

}
