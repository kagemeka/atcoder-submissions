package main


import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)


type Int int


func (
	x Int,
) BitCnt() (
	c int,
) {
	n := int(x)
	for n > 0 {
		c += n & 1
		n >>= 1
	}
	return
}


type Problem struct {
	io *IO
	n, m int
	a, b []int
	relations []int
	cnts []int
	i int
}


func (
	p *Problem,
) countUp() {
	n := p.n
	p.cnts = make([]int, n)
	for i := 0; i < n; i++ {
		p.i = i
		p.countUpSupport()
	}
}


func (
	p *Problem,
) countUpSupport() {
	i := p.i
	rel := p.relations
	s := 0
	t := rel[i]
	n := p.n
	for i := 0; i < n; i++ {
		if ^t >> i & 1 == 1 {
			continue
		}
		s |= rel[i]
	}
	s &= ^rel[i]
	p.cnts[i] = Int(s).BitCnt()
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
	p.n = io.ReadInt()
	m := io.ReadInt()
	a := make([]int, m)
	b := make([]int, m)
	for i := 0; i < m; i++ {
		a[i] = io.ReadInt() - 1
		b[i] = io.ReadInt() - 1
	}
	p.m = m
	p.a, p.b = a, b
}


func (
	p *Problem,
) makeRelations() {
	n := p.n
	rel := make([]int, n)
	for i := 0; i < n; i++ {
		rel[i] |= 1 << i
	}
	m, a, b := p.m, p.a, p.b
	for i := 0; i < m; i++ {
		a, b := a[i], b[i]
		rel[a] |= 1 << b
		rel[b] |= 1 << a
	}
	p.relations = rel
}


func (
	p *Problem,
) Solve() {
	io := p.io
	p.makeRelations()
	p.countUp()
	for _, c := range p.cnts {
		io.Write(c)
	}
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
