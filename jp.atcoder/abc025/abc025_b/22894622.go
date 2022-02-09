package main


import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)


type Problem struct {
	io *IO
	n, a, b int
	s []string
	d []int
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
	p.a = io.ReadInt()
	p.b = io.ReadInt()
	s := make([]string, n)
	d := make([]int, n)
	for i := 0; i < n; i++ {
		s[i] = io.Read()
		d[i] = io.ReadInt()
	}
	p.n, p.s, p.d = n, s, d
}


func (
	p *Problem,
) Solve() {
	n, a, b := p.n, p.a, p.b
	s, d := p.s, p.d
	c := 0
	for i := 0; i < n; i++ {
		s, d := s[i], d[i]
		if d < a { d = a }
		if d > b { d = b }
		if s == "West" {
			d *= -1
		}
		c += d
	}
	io := p.io
	if c == 0 {
		io.Write(0)
		return
	}
	if c > 0 {
		io.Write("East", c)
		return
	}
	io.Write("West", -c)
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
