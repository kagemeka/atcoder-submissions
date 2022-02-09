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


func (
	io *IO,
) SetScanner() {
	scanner := bufio.NewScanner(
		os.Stdin,
	)
	scanner.Split(
		bufio.ScanWords,
	)
	io.Scanner = scanner
}


func (
	io *IO,
) SetScanBuf(
	bufSize int,
) {
	io.Scanner.Buffer(
		[]byte{},
		bufSize,
	)
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


func (
	io *IO,
) Write(
	a ...interface{},
) {
	writer := io.Writer
	fmt.Fprintln(
		writer,
		a...,
	)
	writer.Flush()
}


func (
	io *IO,
) Writef(
	f string,
	a ...interface{},
) {
	writer := io.Writer
	fmt.Fprintf(
		writer,
		f,
		a...,
	)
	writer.Flush()
}



type Int int


func (
	i Int,
) BitLen() (
	l Int,
){
	for i > 0 {
		l++
		i >>= 1
	}
	return
}


func (
	i Int,
) BitCnt() (
	cnt Int,
){
	for i > 0 {
		cnt += i & 1
		i >>= 1
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
	vowels map[rune]bool
	w String
}


func (
	p *Problem,
) Init() {
	io := new(IO)
	io.Init()
	const bufSize = 1 << 7
	io.SetScanBuf(bufSize)
	p.io = io
	vowels := make(
		map[rune]bool,
	)
	for _, c := range "aeiou" {
		vowels[c] = true
	}
	p.vowels = vowels
}


func (
	p *Problem,
) Prepare() {
	io := p.io
	w := io.Scan()
	p.w = w
}


func (
	p *Problem,
) Solve() {
	io := p.io
	vowels := p.vowels
	w := p.w
	var s []rune
	for _, c := range w {
		if vowels[c] {
			continue
		}
		s = append(s, c)
	}
	io.Write(string(s))
}



func main() {
	p := new(Problem)
	Run(p)
}
