package main


import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)



type Int int


func (
	x Int,
) BitCnt() (
	cnt int,
) {
	n := int(x)
	for n > 0 {
		cnt += n & 1
		n >>= 1
	}
	return
}


type PI [2]int


type Cache map[PI]int


type Problem struct {
	io *IO
	n int
	b, c []int
	bits, flg int
	score int
	cache Cache
}


func (
	p *Problem,
) Init() {
	p.io = new(IO)
	p.io.Init()
	p.n = 9
}


func (
	p *Problem,
) Input() {
	const k = 6
	n := p.n
	b := make([]int, n)
	c := make([]int, n)
	io := p.io
	for i := 0; i < k; i++ {
		b[i] = io.ReadInt()
	}
	for i := 0; i < n - 1; i++ {
		if i % 3 == 2 { i++ }
		c[i] = io.ReadInt()
	}
	p.b, p.c = b, c
}


func (
	p *Problem,
) Solve() {
	p.cache = make(
		map[PI]int,
	)
	p.dfs()
	io := p.io
	b, c := p.b, p.c
	tot := 0
	n := p.n
	for i := 0; i < n; i++ {
		tot += b[i] + c[i]
	}
	sa := p.score
	sb := tot - sa
	io.Write(sa)
	io.Write(sb)
}



func (
	p *Problem,
) dfs() {
	n := p.n
	flg, bits := p.flg, p.bits
	cache := p.cache
	key := PI{flg, bits}
	if v, ok := cache[key]; ok {
		p.score = v
		return
	}
	bitCnt := Int(flg).BitCnt()
	if bitCnt == n	{
		p.calcScore()
		return
	}
	isOdd := bitCnt & 1 == 1
	scores := make([]int, 0)
	for i := 0; i < n; i++ {
		if flg >> i & 1 == 1 {
			continue
		}
		p.flg = flg | 1 << i
		if isOdd {
			p.bits = bits | 1 << i
		}
		p.dfs()
		scores = append(
			scores,
			p.score,
		)
	}
	p.flg, p.bits = flg, bits
	sort.Ints(scores)
	var score int
	if isOdd {
		score = scores[0]
	} else {
		n := len(scores)
		score = scores[n - 1]
	}
	cache[key] = score
	p.score = score
}



func (
	p *Problem,
) calcScore() {
	bits := p.bits
	score := 0
	b, c := p.b, p.c
	n := p.n
	for i := 0; i < 6; i++ {
		b1 := bits >> i & 1
		b2 := bits >> (i + 3) & 1
		if b1 == b2 {
			score += b[i]
		}
	}
	for i := 0; i < n - 1; i++ {
		if i % 3 == 2 { i++ }
		b1 := bits >> i & 1
		b2 := bits >> (i + 1) & 1
		if b1 == b2 {
			score += c[i]
		}
	}
	p.score = score
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
