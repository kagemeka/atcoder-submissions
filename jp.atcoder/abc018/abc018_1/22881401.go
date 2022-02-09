package main


import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)


type Result struct {
	id int
	score int
}


type Results []Result


func (
	a Results,
) Len() int {
	return len(a)
}


func (
	a Results,
) Less(
	i, j int,
) bool {
	x, y := a[i], a[j]
	return x.score > y.score
}


func (
	a Results,
) Swap(
	i, j int,
) {
	a[i], a[j] = a[j], a[i]
}


type Problem struct {
	io *IO
	n int
	a []int
	results Results
}


func (
	p *Problem,
) Init() {
	p.io = new(IO)
	p.io.Init()
	p.n = 3
}


func (
	p *Problem,
) Input() {
	n := p.n
	io := p.io
	a := make([]int, n)
	for i := 0; i < n; i++ {
		a[i] = io.ReadInt()
	}
	p.a = a
}


func (
	p *Problem,
) Solve() {
	p.makeResults()
	n, res := p.n, p.results
	sort.Sort(res)
	ord := make([]int, n)
	for i := 0; i < n; i++ {
		ord[res[i].id] = i + 1
	}
	io := p.io
	for _, i := range ord {
		io.Write(i)
	}
}


func (
	p *Problem,
) makeResults() {
	n, a := p.n, p.a
	res := make(Results, n)
	for i := 0; i < n; i++ {
		res[i] = Result{i, a[i]}
	}
	p.results = res
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
