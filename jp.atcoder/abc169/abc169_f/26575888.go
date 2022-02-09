package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)


type StdIO struct {
	scanner *bufio.Scanner
	writer *bufio.Writer
}


func NewStdIO() *StdIO {
	const maxBuffer = 1 << 20
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Buffer([]byte{}, maxBuffer)
	scanner.Split(bufio.ScanWords)
	return &StdIO{
		scanner: scanner,
		writer: bufio.NewWriter(os.Stdout),
	}
}


func (io *StdIO) Scan() string {
	io.scanner.Scan()
	return io.scanner.Text()
}

func (io *StdIO) ScanInt() int {
	v, _ := strconv.Atoi(io.Scan())
	return v
}

func (io *StdIO) Write(a ...interface{}) {
	fmt.Fprintln(io.writer, a...)
	io.writer.Flush()
}


func main() {
	const MOD int = 998_244_353
	io := NewStdIO()
	n, s := io.ScanInt(), io.ScanInt()
	a := make([]int, n)
	for i := 0; i < n; i++ { a[i] = io.ScanInt() }

	dp := make([]int, s  + 1)
	dp[0] = 1
	for _, x := range a {
		for j := s; j > -1; j-- {
			dp[j] *= 2
			if j > x - 1 { dp[j] += dp[j - x] }
			dp[j] %= MOD
		}
	}
	io.Write(dp[s])
}
