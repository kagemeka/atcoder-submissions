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
	n Int,
) BitLen() (
	l Int,
){
	for n > 0 {
		l++
		n >>= 1
	}
	return
}


func (
	n Int,
) BitCnt() (
	cnt Int,
){
	for n > 0 {
		cnt += n & 1
		n >>= 1
	}
	return
}


func (
	x Int,
) Pow(n Int) (
	Numeric,
){
	return Int(
		Float(x).
		Pow(n).
		(Float),
	)
}


func (
	x Int,
) Abs() (
	Numeric,
) {
	return Int(
		Float(x).
		Abs().
		(Float),
	)
}


func (
	x Int,
) Add(
	other Numeric,
) (
	Numeric,
) {
	res :=
		Float(x).
		Add(other).
		(Float)
	switch other.(type) {
	case Int:
		return Int(res)
	}
	return res
}


func (
	x Int,
) Neg() (
	Numeric,
) {
	return -x
}


func (
	x Int,
) Sub(
	other Numeric,
) (
	Numeric,
) {
	res :=
		Float(x).
		Sub(other).
		(Float)
	switch other.(type) {
	case Int:
		return Int(res)
	}
	return res
}


func (
	x Int,
) Mul(
	other Numeric,
) (
	Numeric,
) {
	res :=
		Float(x).
		Mul(other).
		(Float)
	switch other.(type) {
	case Int:
		return Int(res)
	}
	return res
}


func (
	x Int,
) Root(
	n Int,
) (
	root Float,
) {
	return Float(x).Root(n)
}



type Float float64


func (
	x Float,
) Abs() (
	Numeric,
) {
	if x < 0 {
		return -x
	}
	return x
}


func (
	x *Float,
) IAdd(
	other Numeric,
) {
	var y Float
	switch other.(type) {
	case Int:
		y = Float(other.(Int))
	case Float:
		y = other.(Float)
	}
	*x += y
}


func (
	x Float,
) Add(
	other Numeric,
) (
	Numeric,
) {
	x.IAdd(other)
	return x
}


func (
	x Float,
) Neg() (
	Numeric,
) {
	return -x
}


func (
	x *Float,
) ISub(
	other Numeric,
) {
	x.IAdd(other.Neg())
}


func (
	x Float,
) Sub(
	other Numeric,
) (
	Numeric,
) {
	x.ISub(other)
	return x
}


func (
	x *Float,
) IMul(
	other Numeric,
) {
	var y Float
	switch other.(type) {
	case Int:
		y = Float(other.(Int))
	case Float:
		y = other.(Float)
	}
	*x *= y
}


func (
	x Float,
) Mul(
	other Numeric,
) (
	Numeric,
) {
	x.IMul(other)
	return x
}


func (
	x Float,
) Pow(n Int) (
	Numeric,
){
	if n == 0 {
		return Float(1)
	}
	a := x.Pow(n >> 1).(Float)
	a *= a
	if n & 1 == 1 {
		a *= x
	}
	return a
}


func (
	x Float,
) Root(
	n Int,
) (
	root Float,
) {
	y := x
	f := func(
		x Float,
	) (Float) {
		return x.Pow(n).(Float) - y
	}
	root = Newton(f, 1)
	return
}



type Numeric interface {
	Abs() Numeric
	Pow(Int) Numeric
	Add(Numeric) Numeric
	Neg() Numeric
	Sub(Numeric) Numeric
	Mul(Numeric) Numeric
	Root(Int) Float
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



type NewtonFunc func(
	x Float,
) (Float)


func (
	f NewtonFunc,
) Derivative(
	x Float,
) (
	d Float,
) {
	const dx = 1e-8
	d = (f(x + dx) - f(x)) / dx
	return
}


func Newton(
	f NewtonFunc,
	x0 Float,
) (x Float) {
	x = x0
	const maxIter = 100
	for
	i := 0;
	i < maxIter;
	i++ {
		x -= f(x) /
			f.Derivative(x)
	}
	return
}



type Vector2D struct {
	X, Y Numeric
}

func (
	v Vector2D,
) Norm() (
	Float,
) {
	x2 := v.X.Pow(2)
	y2 := v.Y.Pow(2)
	return x2.Add(y2).Root(2)
}


func (
	v Vector2D,
) Add(
	other Vector2D,
) (
	Vector2D,
) {
	return Vector2D{
		v.X.Add(other.X),
		v.Y.Add(other.Y),
	}
}


func (
	v Vector2D,
) Neg() (
	Vector2D,
) {
	return Vector2D{
		v.X.Neg(),
		v.Y.Neg(),
	}
}


func (
	v Vector2D,
) Sub(
	other Vector2D,
) (
	Vector2D,
) {
	return v.Add(other.Neg())
}


func (
	v Vector2D,
) Cross(
	other Vector2D,
) (
	Numeric,
) {
	a := v.X.Mul(other.Y)
	b := v.Y.Mul(other.X)
	return a.Sub(b)
}



type Triangle2D struct {
	p0, p1, p2 Vector2D
}


func (
	t Triangle2D,
) SignedArea() (
	area Float,
) {
	p1 := t.p1.Sub(t.p0)
	p2 := t.p2.Sub(t.p0)
	cross := p1.Cross(p2)
	switch cross.(type) {
	case Int:
		area = Float(
			cross.(Int),
		) / 2
	case Float:
		area = cross.(Float) / 2
	}
	return
}


func (
	t Triangle2D,
) Area() (
	Float,
) {
	s :=
		t.SignedArea().
		Abs().
		(Float)
	return s
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
	x0, y0, x1, y1, x2, y2 Int
}


func (
	p *Problem,
) Init() {
	io := new(IO)
	io.Init()
	const bufSize = 1 << 7
	io.SetScanBuf(bufSize)
	p.io = io
}


func (
	p *Problem,
) Prepare() {
	io := p.io
	p.x0 = io.ScanInt()
	p.y0 = io.ScanInt()
	p.x1 = io.ScanInt()
	p.y1 = io.ScanInt()
	p.x2 = io.ScanInt()
	p.y2 = io.ScanInt()
}


func (
	p *Problem,
) Solve() {
	io := p.io
	p0 := Vector2D{p.x0, p.y0}
	p1 := Vector2D{p.x1, p.y1}
	p2 := Vector2D{p.x2, p.y2}
	t := Triangle2D{p0, p1, p2}
	s := t.Area()
	io.Write(s)
}


func main() {
	p := new(Problem)
	Run(p)
}
