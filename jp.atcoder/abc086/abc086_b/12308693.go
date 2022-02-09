package main

import (
  "fmt"
  "strconv"
  "math"
)

func main() {
  var a, b string
  fmt.Scan(&a, &b)
  c, _ := strconv.Atoi(a + b)
  d := float64(c)
  ans := "No"
  if math.Pow(math.Floor(math.Sqrt(d)), 2) == d {
    ans = "Yes"
  }
  fmt.Println(ans)
}
