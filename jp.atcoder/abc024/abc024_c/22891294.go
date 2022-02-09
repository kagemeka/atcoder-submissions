package main


import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)


func Max(
	x, y int,
) int {
	if x > y {
		return x
	}
	return y
}


func Min(
	x, y int,
) int {
	if x < y {
		return x
	}
	return y
}





type Problem struct {
	io *IO
	n, d, k int
	l, r, s, t []int
	res []int
	j int
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
	d := io.ReadInt()
	k := io.ReadInt()
	l := make([]int, d)
	r := make([]int, d)
	s := make([]int, k)
	t := make([]int, k)
	for i := 0; i < d; i++ {
		l[i] = io.ReadInt()
		r[i] = io.ReadInt()
	}
	for i := 0; i < k; i++ {
		s[i] = io.ReadInt()
		t[i] = io.ReadInt()
	}
	p.d, p.l, p.r = d, l, r
	p.k, p.s, p.t = k, s , t
}


func (
	p *Problem,
) moveAll() {
	j := p.j
	l, r := p.l[j], p.r[j]
	k, s, t := p.k, p.s, p.t
	res := p.res
	for i := 0; i < k; i++ {
		if s[i] < l || s[i] > r {
			continue
		}
		if s[i] == t[i] {
			continue
		}
		if s[i] < t[i] {
			s[i] = Min(t[i], r)
		} else {
			s[i] = Max(t[i], l)
		}
		if s[i] != t[i] {
			continue
		}
		res[i] = j + 1
	}
}



func (
	p *Problem,
) Solve() {
	d := p.d
	k := p.k
	res := make([]int, k)
	p.res = res
	for i := 0; i < d; i++ {
		p.j = i
		p.moveAll()
	}
	for _, x := range res {
		p.io.Write(x)
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
