package main


import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)


type Reversible interface {
	Len() int
	Swap(i, j int)
}


func Reverse(
	a Reversible,
) {
	n := a.Len()
	for i := 0; i < n / 2; i++ {
		a.Swap(i, n - i - 1)
	}
}


type Str string


func (
	a Str,
) Len() int {
	return len(a)
}


// func (
// 	a *Str,
// ) Swap(
// 	i, j int,
// ) {
// 	b := Runes(*a)
// 	b.Swap(i, j)
// 	*a = Str(b)
// }


type Runes []rune


func (
	a Runes,
) Len() int {
	return len(a)
}


func (
	a Runes,
) Swap(
	i, j int,
) {
	a[i], a[j] = a[j], a[i]
}



type Problem struct {
	io *IO
	s string
	n int
	l, r []int
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
	p.s = io.Read()
	n := io.ReadInt()
	l := make([]int, n)
	r := make([]int, n)
	for i := 0; i < n; i++ {
		l[i] = io.ReadInt() - 1
		r[i] = io.ReadInt() - 1
	}
	p.n, p.l, p.r = n, l, r
}


func (
	p *Problem,
) Solve() {
	a := Runes(p.s)
	n, l, r := p.n, p.l, p.r
	for i := 0; i < n; i++ {
		Reverse(a[l[i]:r[i] + 1])
	}
	io := p.io
	s := string(a)
	io.Write(s)
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
