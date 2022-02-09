package main


import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)



type IO struct {
	Scanner *bufio.Scanner
	Reader *bufio.Reader
	Writer *bufio.Writer
}


func (
	io *IO,
) SetScanner() {
	scanner := bufio.NewScanner(
		os.Stdin,
	)
	scanner.Split(
		bufio.ScanWords,
	)
	io.Scanner = scanner
}


func (
	io *IO,
) SetScanBuf(
	bufSize int,
) {
	io.Scanner.Buffer(
		[]byte{},
		bufSize,
	)
}


func(
	io *IO,
) SetWriter() {
	writer := bufio.NewWriter(
		os.Stdout,
	)
	io.Writer = writer
}


func (
	io *IO,
) Init() {
	io.SetScanner()
	io.SetWriter()
	const buf = 1 << 20
	io.SetScanBuf(buf)
}


func (
	io *IO,
) Str() string {
	scanner := io.Scanner
	scanner.Scan()
	return scanner.Text()
}


func (
	io *IO,
) Int() int {
	s := io.Str()
	i, _ := strconv.Atoi(s)
	return i
}


func (
	io *IO,
) Write(
	a ...interface{},
) {
	writer := io.Writer
	fmt.Fprintln(
		writer,
		a...,
	)
	writer.Flush()
}



type Solver interface {
	Prepare()
	Solve()
}


func Run(
	s Solver,
) {
	s.Prepare()
	s.Solve()
}



type Problem struct {
	io *IO
	mod int
	n, m, k int
	a []int
	x, y []int
	g [][]int
}


func (
	p *Problem,
) Init() {
	io := new(IO)
	io.Init()
	p.io = io
	const mod = 1e9 + 7
	p.mod = mod
}


func (
	p *Problem,
) Prepare() {
	io := p.io
	n := io.Int()
	m := io.Int()
	k := io.Int()
	a := make([]int, n)
	for i := 0; i < n; i++ {
		a[i] = io.Int()
	}
	x := make([]int, m)
	y := make([]int, m)
	for i := 0; i < m; i++ {
		x[i] = io.Int() - 1
		y[i] = io.Int() - 1
	}
	p.n = n
	p.m = m
	p.k = k
	p.a = a
	p.x = x
	p.y = y
}


func (
	p *Problem,
) Solve() {
	p.makeGraph()
	p.doubling()
	g := p.g
	a := p.toMatrix(p.a)
	a = p.dot(g, a)
	n := p.n
	io := p.io
	for i := 0; i < n; i++ {
		io.Write(a[i][0])
	}
}


func (
	p *Problem,
) toMatrix(
	a []int,
) [][]int {
	n := len(a)
	b := make([][]int, n)
	for i := 0; i < n; i++ {
		b[i] = []int{a[i]}
	}
	return b
}


func (
	p *Problem,
) doubling() {
	g := p.g
	k := p.k
	g = p.matPow(g, k)
	p.g = g
}


func (
	p *Problem,
) dot(
	a, b [][]int,
) (
	c [][]int,
) {
	n := len(a)
	m := len(b[0])
	c = make([][]int, n)
	for i := 0; i < n; i++ {
		c[i] = make([]int, m)
	}
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			p.dotSupport(
				c, a, b, i, j,
			)
		}
	}
	return c
}


func (
	p *Problem,
) dotSupport(
	c, a, b [][]int,
	i, j int,
) {
	mod := p.mod
	x := 0
	n := len(b)
	for k := 0; k < n; k++ {
		a, b := a[i][k], b[k][j]
		x += a * b % mod
		x %= mod
	}
	c[i][j] = x
}


func (
	p *Problem,
) matPow(
	a [][]int,
	n int,
) [][]int {
	if n == 0 {
		return p.identity()
	}
	x := p.matPow(a, n >> 1)
	x = p.dot(x, x)
	if n & 1 == 1 {
		x = p.dot(x, a)
	}
	return x
}


func (
	p *Problem,
) identity() (
	[][]int,
) {
	n := p.n
	e := make([][]int, n)
	for i := 0; i < n; i++ {
		e[i] = make([]int, n)
		e[i][i] = 1
	}
	return e
}


func (
	p *Problem,
) makeGraph() {
	n := p.n
	g := make([][]int, n)
	for i := 0; i < n; i++ {
		g[i] = make([]int, n)
	}
	p.g = g
	p.fillDiagonal()
	p.smooth()
	p.toProbability()
}


func (
	p *Problem,
) toProbability() {
	g := p.g
	m := p.m
	a := p.inv(2 * m)
	n := p.n
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			g[i][j] *= a
		}
	}
}


func (
	p *Problem,
) pow(
	x, n int,
) int {
	if n == 0 {
		return 1
	}
	y := p.pow(x, n >> 1)
	mod := p.mod
	y = y * y % mod
	if n & 1 == 1 {
		y = y * x % mod
	}
	y = (y + mod) % mod
	return y
}


func (
	p *Problem,
) inv(
	n int,
) int {
	return p.pow(n, p.mod - 2)
}


func (
	p *Problem,
) smooth() {
	g := p.g
	x, y := p.x, p.y
	m := p.m
	for i := 0; i < m; i++ {
		x, y := x[i], y[i]
		g[x][x]--
		g[y][y]--
		g[x][y]++
		g[y][x]++
	}
}


func (
	p *Problem,
) fillDiagonal() {
	g := p.g
	n := p.n
	m := p.m
	for i := 0; i < n; i++ {
		g[i][i] = 2 * m
	}
}



func main() {
	p := new(Problem)
	p.Init()
	t := 1
	// t = p.io.Int()
	for i := 0; i < t; i++ {
		Run(p)
	}
}
