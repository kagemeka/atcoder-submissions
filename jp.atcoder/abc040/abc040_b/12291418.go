package main

import (
  "fmt"
  "math"
)

const inf = 1 << 63 - 1

func divmod(a, b int) (int, int) {return a / b, a % b}

func main() {
  var n int
  fmt.Scan(&n)
  m := int(math.Sqrt(float64(n)))
  d := n
  for i := 1; i < m + 1; i++ {
    j, r := divmod(n, i)
    if j - i + r < d {
      d = j - i + r
    }
  }
  fmt.Println(d)
}
