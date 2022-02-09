package main


import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)


type Problem struct {
	io *IO
	n int
	b, a []int
	salary int
	i int
}


func (
	p *Problem,
) Init() {
	p.io = new(IO)
	p.io.Init()
}


func (
	p *Problem,
) Input() {
	io := p.io
	n := io.ReadInt()
	b := make([]int, n)
	for i := 1; i < n; i++ {
		b[i] = io.ReadInt() - 1
	}
	p.n, p.b = n, b
}


func (
	p *Problem,
) Solve() {
	p.makeChildTbl()
	p.dfs()
	p.io.Write(p.salary)
}

func (
	p *Problem,
) dfs() {
	i := p.i
	sals := make([]int, 0)
	s := 1
	n := p.n
	a := p.a[i]
	for i := 0; i < n; i++ {
		if ^a >> i & 1 == 1 {
			continue
		}
		p.i = i
		p.dfs()
		sals = append(
			sals,
			p.salary,
		)
	}
	n = len(sals)
	p.i = i
	if n == 0 {
		p.salary = s
		return
	}
	sort.Ints(sals)
	s += sals[0] + sals[n - 1]
	p.salary = s
}

func (
	p *Problem,
) makeChildTbl() {
	n := p.n
	a := make([]int, n)
	b := p.b
	for i, x := range b[1:] {
		a[x] |= 1 << (i + 1)
	}
	p.a = a
}


func main() {
	p := new(Problem)
	p.Init()
	// t := p.io.ReadInt()
	t := 1
	for i := 0; i < t; i++ {
		Run(p)
	}
}



type IO struct {
	r *Read
	w *Write
}


func (
	io *IO,
) Init() {
	r, w := new(Read), new(Write)
	r.Init()
	w.Init()
	io.r, io.w = r, w
}


func (
	io *IO,
) Read() (
	string,
) {
	return io.r.Str()
}


func (
	io *IO,
) ReadInt() (
	int,
) {
	return io.r.Int()
}


func (
	io *IO,
) Write(
	a ...interface{},
) {
	io.w.All(a...)
}



type Read struct {
	sc *bufio.Scanner
}


func (
	r *Read,
) Init() {
	r.setScanner()
	const buf = 1 << 20
	r.setBuf(buf)
}


func (
	r *Read,
) Int() (
	int,
) {
	s := r.Str()
	i, _ := strconv.Atoi(s)
	return i
}


func (
	r *Read,
) setBuf(
	bufSize int,
) {
	r.sc.Buffer(
		[]byte{},
		bufSize,
	)
}


func (
	r *Read,
) setScanner() {
	sc := bufio.NewScanner(
		os.Stdin,
	)
	sc.Split(
		bufio.ScanWords,
	)
	r.sc = sc
}


func  (
	r *Read,
) Str() (
	string,
) {
	sc  := r.sc
	sc.Scan()
	return sc.Text()
}



type Solver interface {
	Init()
	Input()
	Solve()
}


func Run(
	s Solver,
) {
	s.Input()
	s.Solve()
}



type Write struct {
	writer *bufio.Writer
}


func (
	w *Write,
) All(
	a ...interface{},
) {
	writer := w.writer
	fmt.Fprintln(
		writer,
		a...,
	)
	writer.Flush()
}


func (
	w *Write,
) Init() {
	w.setWriter()
}


func (
	w *Write,
) setWriter() {
	w.writer = bufio.NewWriter(
		os.Stdout,
	)
}
