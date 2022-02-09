package main

import (
	"fmt"
)


import (
	"bufio"
	"os"
	"strconv"
)

const MaxBuffer = 1 << 20

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
) Scan() string {
	scanner := io.Scanner
	scanner.Scan()
	return scanner.Text()
}


func (
	io *IO,
) ScanInt() int {
	s := io.Scan()
	v, _ := strconv.Atoi(s)
	return v
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



type ABC001A struct {
	io *IO
	h1 int
	h2 int
}


func (
	p *ABC001A,
) Init() {
	io := new(IO)
	io.Init()
	p.io = io
}


func (
	p *ABC001A,
) Prepare() {
	io := p.io
	h1 := io.ScanInt()
	h2 := io.ScanInt()
	p.h1, p.h2 = h1, h2
}

func (
	p *ABC001A,
) Solve() {
	d := p.h1 - p.h2
	fmt.Println(d)
}


func main() {
	p := new(ABC001A)
	Run(p)
}
