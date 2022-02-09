package main


import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
)



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







type Problem struct {
	io *IO
	n int
	points []Point
	dist Float
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
	points := make([]Point, n)
	for i := 0; i < n; i++ {
		x := io.ReadInt()
		y := io.ReadInt()
		points[i] = Point{x, y}
	}
	p.n = n
	p.points = points
}


func (
	p *Problem,
) Solve() {
	p.dist = 0
	p.calcDist()
	io := p.io
	io.Write(p.dist)
}


func (
	p *Problem,
) calcDist() {
	n := p.n
	for i := 0; i < n - 1; i++ {
		p.i = i
		p.calcDistSupport()
	}
}


func (
	p *Problem,
) calcDistSupport() {
	i := p.i
	points := p.points
	u := points[i]
	n := p.n
	for j := i + 1; j < n; j++ {
		v := points[j]
		p.dist =  Max(
			p.dist,
			Float(u.Dist(&v)),
		).(Float)
	}
}



type Float float64


func (
	x Float,
) Less(
	y interface{},
) bool {
	return x < y.(Float)
}


type Point struct {
	x, y int
}


func (
	u *Point,
) Dist(
	v *Point,
) (
	d float64,
) {
	dx := float64(v.x - u.x)
	dy := float64(v.y - u.y)
	d = dx * dx + dy * dy
	d = math.Sqrt(d)
	return
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



type Comparable interface {
	Less(interface{}) bool
}


func GE(
	a, b Comparable,
) bool {
	return !LT(a, b)
}


func GT(
	a, b Comparable,
) bool {
	return !LE(a, b)
}


func LE(
	a, b Comparable,
) bool {
	return a.Less(b)
}


func LT(
	a, b Comparable,
) bool {
	return LE(a, b) || a == b
}


func Max(
	a ...Comparable,
) Comparable {
	v := a[0]
	for _, x := range a {
		if LE(x, v) {
			continue
		}
		v = x
	}
	return v
}



func Min(
	a ...Comparable,
) Comparable {
	v := a[0]
	for _, x := range a {
		if GE(x, v) {
			continue
		}
		v = x
	}
	return v
}
