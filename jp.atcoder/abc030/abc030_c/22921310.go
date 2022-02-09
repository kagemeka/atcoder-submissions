package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)



// type Comparable interface {
// 	Less(interface{}) bool
// }


// func GE(
// 	a, b Comparable,
// ) bool {
// 	return !LT(a, b)
// }


// func GT(
// 	a, b Comparable,
// ) bool {
// 	return !LE(a, b)
// }


// func LE(
// 	a, b Comparable,
// ) bool {
// 	return a.Less(b)
// }


// func LT(
// 	a, b Comparable,
// ) bool {
// 	return LE(a, b) || a == b
// }



// type BisectFunc func(
// 	i int,
// 	x interface{},
// ) bool




type Ints []int


func (
	a Ints,
) BisectLeft(
	x int,
) int {
	f := func(
		i int,
	) bool {
		return a[i] >= x
	}
	n := len(a)
	return sort.Search(n, f)
}



func (
	a Ints,
) BisectRight(
	x int,
) int {
	f := func(
		i int,
	) bool {
		return a[i] > x
	}
	n := len(a)
	return sort.Search(n, f)
}



// type BisectIF interface {
// 	Get(i int) interface{}
// 	Len() int
// }




// type Bisect struct {
// 	data BisectIF
// 	x Comparable
// }


// func (
// 	a Bisect,
// ) Left(
// 	x Comparable,
// ) int {
// 	a.x = x
// 	return sort.Search(
// 		a.data.Len(),
// 		a.leftFunc,
// 	)
// }


// func (
// 	a Bisect,
// ) leftFunc(
// 	i int,
// ) bool {
// 	return GE(
// 		a.data.Get(i).(Comparable),
// 		a.x,
// 	)
// }


// func (
// 	a Bisect,
// ) Right(
// 	x Comparable,
// ) int {
// 	a.x = x
// 	return sort.Search(
// 		a.data.Len(),
// 		a.rightFunc,
// 	)
// }


// func (
// 	a Bisect,
// ) rightFunc(
// 	i int,
// ) bool {
// 	return GT(
// 		a.data.Get(i).(Comparable),
// 		a.x,
// 	)
// }


// func (
// 	a Bisect,
// ) Set(
// 	data BisectIF,
// ) {
// 	a.data = data
// }


// type Int int

// func (
// 	x Int,
// ) Less(
// 	otyer interface{},
// ) bool {
// 	y := other.(Int)
// }


type Problem struct {
	io *IO
	n, m, x, y int
	a, b Ints
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
	m := io.ReadInt()
	p.x = io.ReadInt()
	p.y = io.ReadInt()
	a := make(Ints, n)
	b := make(Ints, m)
	for i := 0; i < n; i++ {
		a[i] = io.ReadInt()
	}
	for i := 0; i < m; i++ {
		b[i] = io.ReadInt()
	}
	p.n, p.a = n, a
	p.m, p.b = m, b
}


func (
	p *Problem,
) Solve() {

	n, a, x := p.n, p.a, p.x
	m, b, y := p.m, p.b, p.y

	t := 0
	for
	i := 0; i < n + m + 1; i++ {
		a := a
		x := x
		n := n
		if i & 1 == 1 {
			a = b
			x = y
			n = m
		}
		j := a.BisectLeft(t)
		if j == n {
			p.io.Write(i / 2)
			return
		}
		t = a[j] + x
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
