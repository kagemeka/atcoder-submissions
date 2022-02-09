package main


import (
	"fmt"
)


import (
	"bufio"
	"os"
	"strconv"
)


type IO struct {
	Scanner *bufio.Scanner
	Reader *bufio.Reader
	Writer *bufio.Writer
}


const MaxBuffer = 1 << 20


func (
	io *IO,
) SetScanner() {
	scanner := bufio.NewScanner(
		os.Stdin,
	)
	scanner.Buffer(
		[]byte{},
		MaxBuffer,
	)
	scanner.Split(
		bufio.ScanWords,
	)
	io.Scanner = scanner
}


func (
	io *IO,
) SetReader() {
	reader := bufio.NewReader(
		os.Stdin,
	)
	io.Reader = reader
}


func(
	io *IO,
) SetWriter() {
	writer := bufio.NewWriter(
		os.Stdout,
	)
	io.Writer = writer
}


func (
	io *IO,
) Init() {
	if io.Scanner == nil {
		io.SetScanner()
	}
	if io.Reader == nil {
		io.SetReader()
	}
	if io.Writer == nil {
		io.SetWriter()
	}
}


func (
	io *IO,
) Scan() String {
	scanner := io.Scanner
	scanner.Scan()
	s := String(scanner.Text())
	return s
}


func (
	io *IO,
) ScanInt() Int {
	s := string(io.Scan())
	v, _ := strconv.Atoi(s)
	return Int(v)
}



type Int int


func (
	i *Int,
) BitLength() (
	l Int,
){
	n := *i
	l = 0
	for n > 0 {
		l++
		n >>= 1
	}
	return
}


func (
	i *Int,
) BitCount() (
	cnt Int,
){
	cnt = 0
	n := *i
	for n > 0 {
		cnt += n & 1
		n >>= 1
	}
	return
}


func (
	i Int,
) Pow(n Int) (
	Int,
){
	if n == 0 {
		return 1
	}
	a := i.Pow(n >> 1)
	a *= a
	if n & 1 == 1 {
		a *= i
	}
	return a
}



type String string



type Bool bool


func (
	b Bool,
) Int() (
	Int,
) {
	if b {return 1}
	return 0
}



type Solver interface{
	Init()
	Prepare()
	Solve()
}


func Run(s Solver) {
	s.Init()
	s.Prepare()
	s.Solve()
}



type Problem struct {
	io *IO
	m Int
}


func (
	p *Problem,
) Init() {
	io := new(IO)
	io.Init()
	p.io = io
}


func (
	p *Problem,
) Prepare() {
	io := p.io
	m := io.ScanInt()
	p.m = m
}


func (
	p *Problem,
) Solve() {
	m := p.m
	var vv Int
	if m < 100 {
		vv = 0
	} else
	if m <= 5_000 {
		vv = m * 10
	} else
	if m <= 30_000 {
		vv = m + 50 * 1000
	} else
	if m <= 70_000 {
		vv =
			(m - 30 * 1000) /
			5 + 80 * 1000
	} else {
		vv = 89_000
	}

	vv /= 1000
	fmt.Printf(
		"%02d\n",
		vv,
	)
}



func main() {
	p := new(Problem)
	Run(p)
}
