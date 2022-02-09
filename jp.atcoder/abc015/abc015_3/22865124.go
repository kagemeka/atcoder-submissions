package main


import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)


type Message struct {
	Ok, Ng string
}


type Problem struct {
	io *IO
	msg Message
	n, k int
	t [][]int
	a []int
	i int
}


func (
	p *Problem,
) Init() {
	p.io = new(IO)
	p.io.Init()
	p.msg = Message{
		"Nothing",
		"Found",
	}
}


func (
	p *Problem,
) Input() {
	io := p.io
	n := io.ReadInt()
	k := io.ReadInt()
	t := make([][]int, n)
	for i := 0; i < n; i++ {
		t[i] = make([]int, k)
		for j := 0; j < k; j++ {
			t[i][j] = io.ReadInt()
		}
	}
	p.n, p.k, p.t = n, k, t
}


func (
	p *Problem,
) Solve() {
	p.a = []int{0}
	n := p.n
	for i := 0; i < n; i++ {
		p.i = i
		p.calcXor()
	}
	io := p.io
	msg := p.msg
	for _, x := range p.a {
		if x != 0 { continue }
		io.Write(msg.Ng)
		return
	}
	io.Write(msg.Ok)
}


func (
	p *Problem,
) calcXor() {
	t := p.t[p.i]
	a := p.a
	b := make([]int, 0)
	for _, x := range a {
		for _, y := range t {
			b = append(b, x ^ y)
		}
	}
	p.a = b
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
