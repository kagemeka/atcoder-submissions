package main

import (
  "fmt"
)

func pow(args ...int) int {
  x, y := args[0], args[1]
  res := 1
  if len(args) == 3 {
    mod := args[2]
    for y != 0 {
      if y & 1 == 1 {res = res * x % mod}
      y >>= 1
      x = x * x % mod
    }
  }  else {
    for y != 0 {
      if y & 1 == 1 {res *= x}
      y >>= 1
      x *= x
    }
  }
  return res
}

const mod = 1e9 + 7
func makeTables(n, r, p int) ([]int, []int, []int) {
  fac, ifac, nChoose := make([]int, r + 1), make([]int, r + 1), make([]int, r + 1)
  fac[0] = 1; for i := 0; i < r; i++ {fac[i+1] = fac[i] * (i + 1) % p}
  ifac[r] = pow(fac[r], p - 2, p); for i := r; i > 0; i-- {ifac[i-1] = ifac[i] * i % p}
  nChoose[0] = 1; for i := 0; i < r; i++ {nChoose[i+1] = nChoose[i] * (n - i) % p}
  for i := 0; i < r + 1; i++ {nChoose[i] = nChoose[i] * ifac[i] % p}
  return fac, ifac, nChoose
}
var fac, ifac, nChoose = makeTables(1e9, 1e7, mod)
func choose(n, r int) int {
  if r > n || r < 0 {return 0}
  var p int = mod
  return fac[n] * ifac[n-r] % p * ifac[r] % p
}

func main() {
  var n int
  fmt.Scan(&n)
  fmt.Println(fac[n])
}
