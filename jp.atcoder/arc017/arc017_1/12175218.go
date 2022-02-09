package main

import (
	"fmt"
	"math"
)

func sieveOfEratosthenes(n int) ([]bool, []int) {
	sieve := make([]bool, n + 1)
	for i := 2; i < n + 1; i++ {sieve[i] = true}
	m := int(math.Sqrt(float64(n))) + 1
	for i := 2; i < m; i++ {
		if sieve[i] {
			for j := i * 2; j < n + 1; j += i {
				sieve[j] = false
			}
		}
	}
	primeNumbers := []int{}
	for i := 2; i < n + 1; i++ {
		if sieve[i] {primeNumbers = append(primeNumbers, i)}
	}
	return sieve[:], primeNumbers
}
var isPrime, primeNumbers = sieveOfEratosthenes(3e7)
func primeFactorize(n int) map[int]int {
	res := make(map[int]int)
	if n < 2 {return res}
	m := int(math.Sqrt(float64(n)))
	for _, p := range primeNumbers {
		if p > m {break}
		for n % p == 0 {n /= p; res[p]++}
		if n == 1 {return res}
	}
	res[n] = 1; return res
}
func primeFactorizeFactorial(n int) map[int]int {
	res := make(map[int]int)
	for i := 1; i < n + 1; i++ {
		for p, c := range primeFactorize(i) {res[p] += c}
	}
	return res
}

func main() {
	var n int; fmt.Scan(&n)
	ans := "NO"; if isPrime[n] {ans = "YES"}
	fmt.Println(ans)
}
