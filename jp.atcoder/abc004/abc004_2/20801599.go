package main


import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)



type Bool bool


func (
	b Bool,
) Int() (
	Int,
) {
	if b {return 1}
	return 0
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


func (
	x Int,
) LT(
	other Comparable,
) Bool {
	return x < other.(Int)
}


func (
	x Int,
) LE(
	other Comparable,
) Bool {
	return x <= other.(Int)
}


func (
	x Int,
) GE(
	other Comparable,
) Bool {
	return !x.LT(other)
}


func (
	x Int,
) GT(
	other Comparable,
) Bool {
	return !x.LE(other)
}



type IntSlice []Int


func (
	a IntSlice,
) Standard() (
	b []int,
) {
	n := len(a)
	b = make(
		[]int,
		n,
	)
	for i := 0; i < n; i++ {
		b[i] = int(a[i])
	}
	return
}


func (
	a IntSlice,
) IS() (
	b IS,
) {
	n := len(a)
	b = make(
		IS,
		n,
	)
	for i := 0; i < n; i++ {
		b[i] = a[i]
	}
	return
}


func (
	a IntSlice,
) String() string {
	n := len(a)
	return fmt.Sprintf(
		SliceFormat(n, " "),
		a.IS()...,
	)
}


func (
	a IntSlice,
) Max() (
	Int,
) {
	b := make(
		[]Comparable,
		len(a),
	)
	for i := range a {
		b[i] = a[i]
	}
	return Max(b...).(Int)
}


func (
	a IntSlice,
) Min() (
	Int,
) {
	b := make(
		[]Comparable,
		len(a),
	)
	for i := range a {
		b[i] = a[i]
	}
	return Min(b...).(Int)
}


func (
	a IntSlice,
) Sum() (
	Int,
) {
	b := make(
		[]Numeric,
		len(a),
	)
	for i := range a {
		b[i] = a[i]
	}
	return Sum(b...).(Int)
}


func (
	a IntSlice,
) Len() int {
	return len(a)
}


func (
	a IntSlice,
) Less(
	i, j int,
) bool {
	return a[i] < a[j]
}


func (
	a IntSlice,
) Swap(
	i, j int,
) {
	a[i], a[j] = a[j], a[i]
}


func (
	a IntSlice,
) Clone() (
	Slice,
) {
	n := len(a)
	s := make(IntSlice, n)
	copy(s, a)
	return s
}


func (
	a IntSlice,
) Reverse() {
	Reverse(a)
}


func (
	a IntSlice,
) Reversed() (
	s IntSlice,
) {
	s = a.Clone().(IntSlice)
	s.Reverse()
	return
}


func (
	a IntSlice,
) Sort() {
	sort.Sort(a)
}


func (
	a IntSlice,
) Sorted() (
	IntSlice,
) {
	a = a.Clone().(IntSlice)
	a.Sort()
	return a
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


func (
	x Float,
) LT(
	other Comparable,
) Bool {
	return x < other.(Float)
}


func (
	x Float,
) LE(
	other Comparable,
) Bool {
	return x <= other.(Float)
}


func (
	x Float,
) GE(
	other Comparable,
) Bool {
	return !x.LT(other)
}


func (
	x Float,
) GT(
	other Comparable,
) Bool {
	return !x.LE(other)
}



type FloatSlice []Float


func (
	a FloatSlice,
) Standard() (
	b []float64,
) {
	n := len(a)
	b = make(
		[]float64,
		n,
	)
	for i := 0; i < n; i++ {
		b[i] = float64(a[i])
	}
	return
}


func (
	a FloatSlice,
) IS() (
	b IS,
) {
	n := len(a)
	b = make(
		IS,
		n,
	)
	for i := 0; i < n; i++ {
		b[i] = a[i]
	}
	return
}


func (
	a FloatSlice,
) String() string {
	n := len(a)
	return fmt.Sprintf(
		SliceFormat(n, " "),
		a.IS()...,
	)
}


func (
	a FloatSlice,
) Max() (
	Float,
) {
	b := make(
		[]Comparable,
		len(a),
	)
	for i := range a {
		b[i] = a[i]
	}
	return Max(b...).(Float)
}


func (
	a FloatSlice,
) Min() (
	Float,
) {
	b := make(
		[]Comparable,
		len(a),
	)
	for i := range a {
		b[i] = a[i]
	}
	return Min(b...).(Float)
}


func (
	a FloatSlice,
) Sum() (
	Float,
) {
	b := make(
		[]Numeric,
		len(a),
	)
	for i := range a {
		b[i] = a[i]
	}
	return Sum(b...).(Float)
}


func (
	a FloatSlice,
) Len() int {
	return len(a)
}


func (
	a FloatSlice,
) Less(
	i, j int,
) bool {
	return a[i] < a[j]
}


func (
	a FloatSlice,
) Swap(
	i, j int,
) {
	a[i], a[j] = a[j], a[i]
}


func (
	a FloatSlice,
) Clone() (
	Slice,
) {
	n := len(a)
	s := make(FloatSlice, n)
	copy(s, a)
	return s
}


func (
	a FloatSlice,
) Reverse() {
	Reverse(a)
}


func (
	a FloatSlice,
) Reversed() (
	s FloatSlice,
) {
	s = a.Clone().(FloatSlice)
	s.Reverse()
	return
}


func (
	a FloatSlice,
) Sort() {
	sort.Sort(a)
}


func (
	a FloatSlice,
) Sorted() (
	FloatSlice,
) {
	a = a.Clone().(FloatSlice)
	a.Sort()
	return a
}



type String string


func (
	s String,
) RuneSlice() (
	a RuneSlice,
) {
	n := len(s)
	a = make(
		RuneSlice,
		n,
	)
	for i := 0; i < n; i++ {
		a[i] = Rune(s[i])
	}
	return
}


func (
	x String,
) LT(
	other Comparable,
) Bool {
	return x < other.(String)
}


func (
	x String,
) LE(
	other Comparable,
) Bool {
	return x <= other.(String)
}


func (
	x String,
) GE(
	other Comparable,
) Bool {
	return !x.LT(other)
}


func (
	x String,
) GT(
	other Comparable,
) Bool {
	return !x.LE(other)
}


func (
	s *String,
) Reverse() {
	a := s.RuneSlice()
	a.Reverse()
	*s = a.ToString()
}


func (
	s String,
) Reversed() (
	String,
) {
	s.Reverse()
	return s
}


func (
	s *String,
) Sort() {
	a := s.RuneSlice()
	a.Sort()
	*s = a.ToString()
}


func (
	s String,
) Sorted() (
	String,
) {
	s.Sort()
	return s
}



type StringSlice []String


func (
	a StringSlice,
) Standard() (
	b []string,
) {
	n := len(a)
	b = make(
		[]string,
		n,
	)
	for i := 0; i < n; i++ {
		b[i] = string(a[i])
	}
	return
}


func (
	a StringSlice,
) IS() (
	b IS,
) {
	n := len(a)
	b = make(
		IS,
		n,
	)
	for i := 0; i < n; i++ {
		b[i] = a[i]
	}
	return
}


func (
	a StringSlice,
) String() string {
	n := len(a)
	return fmt.Sprintf(
		SliceFormat(n, " "),
		a.IS()...,
	)
}


func (
	a StringSlice,
) Max() (
	String,
) {
	b := make(
		[]Comparable,
		len(a),
	)
	for i := range a {
		b[i] = a[i]
	}
	return Max(b...).(String)
}


func (
	a StringSlice,
) Min() (
	String,
) {
	b := make(
		[]Comparable,
		len(a),
	)
	for i := range a {
		b[i] = a[i]
	}
	return Min(b...).(String)
}


func (
	a StringSlice,
) Len() int {
	return len(a)
}


func (
	a StringSlice,
) Less(
	i, j int,
) bool {
	return a[i] < a[j]
}


func (
	a StringSlice,
) Swap(
	i, j int,
) {
	a[i], a[j] = a[j], a[i]
}


func (
	a StringSlice,
) Clone() (
	Slice,
) {
	n := len(a)
	s := make(StringSlice, n)
	copy(s, a)
	return s
}


func (
	a StringSlice,
) Reverse() {
	Reverse(a)
}


func (
	a StringSlice,
) Reversed() (
	s StringSlice,
) {
	s = a.Clone().(StringSlice)
	s.Reverse()
	return
}


func (
	a StringSlice,
) Sort() {
	sort.Sort(a)
}


func (
	a StringSlice,
) Sorted() (
	StringSlice,
) {
	a = a.Clone().(StringSlice)
	a.Sort()
	return a
}



type StringSlice2D [
]StringSlice


func (
	a StringSlice2D,
) Len() int {
	return len(a)
}


func (
	a StringSlice2D,
) Swap(
	i, j int,
) {
	a[i], a[j] = a[j], a[i]
}

func (
	a StringSlice2D,
) Clone() (
	Slice,
) {
	n := len(a)
	s := make(StringSlice2D, n)
	for i := 0; i < n; i++ {
		s[i] = (
			a[i].
			Clone().
			(StringSlice))
	}
	return s
}


func (
	a StringSlice2D,
) Reverse() {
	Reverse(a)
}


func (
	a StringSlice2D,
) Reversed() (
	s StringSlice2D,
) {
	s = (
		a.Clone().
		(StringSlice2D))
	s.Reverse()
	return
}



type Rune rune


func (
	x Rune,
) LT(
	other Comparable,
) Bool {
	return x < other.(Rune)
}


func (
	x Rune,
) LE(
	other Comparable,
) Bool {
	return x <= other.(Rune)
}


func (
	x Rune,
) GE(
	other Comparable,
) Bool {
	return !x.LT(other)
}


func (
	x Rune,
) GT(
	other Comparable,
) Bool {
	return !x.LE(other)
}



type RuneSlice []Rune


func (
	a RuneSlice,
) Standard() (
	b []rune,
) {
	n := len(a)
	b = make(
		[]rune,
		n,
	)
	for i := 0; i < n; i++ {
		b[i] = rune(a[i])
	}
	return
}


func (
	a RuneSlice,
) IS() (
	b IS,
) {
	n := len(a)
	b = make(
		IS,
		n,
	)
	for i := 0; i < n; i++ {
		b[i] = a[i]
	}
	return
}


func (
	a RuneSlice,
) String() (
	string,
) {
	n := len(a)
	return fmt.Sprintf(
		SliceFormat(n, " "),
		a.IS()...,
	)
}


func (
	a RuneSlice,
) ToString() (
	String,
) {
	b := a.Standard()
	return String(b)
}


func (
	a RuneSlice,
) Max() (
	Rune,
) {
	b := make(
		[]Comparable,
		len(a),
	)
	for i := range a {
		b[i] = a[i]
	}
	return Max(b...).(Rune)
}


func (
	a RuneSlice,
) Min() (
	Rune,
) {
	b := make(
		[]Comparable,
		len(a),
	)
	for i := range a {
		b[i] = a[i]
	}
	return Min(b...).(Rune)
}


func (
	a RuneSlice,
) Len() int {
	return len(a)
}


func (
	a RuneSlice,
) Less(
	i, j int,
) bool {
	return a[i] < a[j]
}


func (
	a RuneSlice,
) Swap(
	i, j int,
) {
	a[i], a[j] = a[j], a[i]
}


func (
	a RuneSlice,
) Clone() (
	Slice,
) {
	n := len(a)
	s := make(RuneSlice, n)
	copy(s, a)
	return s
}


func (
	a RuneSlice,
) Reverse() {
	Reverse(a)
}


func (
	a RuneSlice,
) Reversed() (
	s RuneSlice,
) {
	s = a.Clone().(RuneSlice)
	s.Reverse()
	return
}


func (
	a RuneSlice,
) Sort() {
	sort.Sort(a)
}


func (
	a RuneSlice,
) Sorted() (
	RuneSlice,
) {
	a = a.Clone().(RuneSlice)
	a.Sort()
	return a
}



type IS []interface{}


func SliceFormat(
	n int,
	sep string,
) (
	format string,
) {
	f := make(
		[]string,
		n,
	)
	for i := 0; i < n; i++ {
		f[i] = "%v"
	}
	format = strings.Join(
		f,
		sep,
	)
	return
}



type Comparable interface {
	LT(Comparable) Bool
	LE(Comparable) Bool
	GE(Comparable) Bool
	GT(Comparable) Bool
}


func Max(
	a ...Comparable,
) (
	mx Comparable,
) {
	mx = a[0]
	for _, x := range a {
		if x.LE(mx) {
			continue
		}
		mx = x
	}
	return
}


func Min(
	a ...Comparable,
) (
	mx Comparable,
) {
	mx = a[0]
	for _, x := range a {
		if x.GE(mx) {
			continue
		}
		mx = x
	}
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


func Abs(
	x Numeric,
) Numeric {
	return x.Abs()
}


func Sum(
	a ...Numeric,
) (
	s Numeric,
) {
	s = Int(0)
	for  _, x := range a {
		s = s.Add(x)
	}
	return
}



type Slice interface {
	Len() int
	Swap(i, j int)
	Clone() Slice
}


func Reverse(
	s Slice,
) {
	n := s.Len()
	for i := 0; i < n/2; i++ {
		s.Swap(i, n-i-1)
	}
}


func Reversed(
	s Slice,
) Slice {
	s = s.Clone()
	Reverse(s)
	return s
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


func (
	f NewtonFunc,
) Newton(
	x0 Float,
) (
	x Float,
) {
	x = x0
	const maxIter = 1 << 4
	for
	i := 0;
	i < maxIter;
	i++ {
		x -= f(x) /
			f.Derivative(x)
	}
	return
}


func Newton(
	f NewtonFunc,
	x0 Float,
) (
	Float,
) {
	return f.Newton(x0)
}



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
	c StringSlice2D
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
	const n = 4
	c := make(
		StringSlice2D,
		n,
	)
	for i := 0; i < n; i++ {
		c[i] = make(StringSlice, n)
	}
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			c[i][j] = io.Scan()
		}
	}
	p.c = c
}


func (
	p *Problem,
) Solve() {
	io := p.io
	c := p.c
	n := len(c)
	c.Reverse()
	for i := 0; i < n; i++{
		s := c[i].Reversed()
		io.Write(s.IS()...)
	}
}



func main() {
	p := new(Problem)
	Run(p)
}
