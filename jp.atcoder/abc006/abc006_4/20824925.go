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
	x Int,
) Str() (
	Str,
) {
	s := strconv.Itoa(
		int(x),
	)
	return Str(s)
}


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
) Divmod(
	other Int,
) (
	q Int, r Int,
) {
	q = x / other
	r = x % other
	return
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
	b = make(IS, n)
	for i := 0; i < n; i++ {
		b[i] = a[i]
	}
	return
}


func (
	a IntSlice,
) CompSlice() (
	b CompSlice,
) {
	n := len(a)
	b = make(CompSlice, n)
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
		CompSlice,
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
		CompSlice,
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


func (
	a IntSlice,
) CumSum() (
	b IntSlice,
) {
	b = a.Clone().(IntSlice)
	n := len(a)
	for i := 0; i < n-1; i++ {
		b[i+1] += b[i]
	}
	return
}


func (
	a IntSlice,
) CumProd() (
	b IntSlice,
) {
	b = a.Clone().(IntSlice)
	n := len(a)
	for i := 0; i < n-1; i++ {
		b[i+1] *= b[i]
	}
	return
}


func (
	a IntSlice,
) CumMax() (
	b IntSlice,
) {
	b = a.Clone().(IntSlice)
	n := len(a)
	for i := 0; i < n-1; i++ {
		b[i+1] = Max(
			b[i+1],
			b[i],
		).(Int)
	}
	return
}


func (
	a IntSlice,
) BisectLeft(
	x Int,
) (
	i Int,
) {
	n := len(a)
	f := func(
		i int,
	) bool {
		return a[i] >= x
	}
	i = Int(sort.Search(n, f))
	return
}


func (
	a IntSlice,
) BisectRight(
	x Int,
) (
	i Int,
) {
	n := len(a)
	f := func(
		i int,
	) bool {
		return a[i] > x
	}
	i = Int(sort.Search(n, f))
	return
}


func (
	a IntSlice,
) LIS(
	inf Int,
) (
	lis IntSlice,
) {
	b := a.CompSlice()
	b = b.LIS(inf)
	lis = b.IntSlice()
	return
}



type IntMatrix []IntSlice


func (
	a IntMatrix,
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
	a IntMatrix,
) String() (
	string,
) {
	n := len(a)
	return fmt.Sprintf(
		SliceFormat(n, "\n"),
		a.IS()...,
	)
}


func (
	a IntMatrix,
) Make(n, m Int) (
	b IntMatrix,
) {
	b = make(IntMatrix, n)
	for i := Int(0); i < n; i++ {
		b[i] = make(IntSlice, m)
	}
	return
}


func (
	a IntMatrix,
) Shape() (
	n, m Int,
) {
	n = Int(len(a))
	m = Int(len(a[0]))
	return
}


func (
	a IntMatrix,
) Len() int {
	return len(a)
}


func (
	a IntMatrix,
) Swap(
	i, j int,
) {
	a[i], a[j] = a[j], a[i]
}


func (
	a IntMatrix,
) Clone() (
	Slice,
) {
	n := len(a)
	s := make(IntMatrix, n)
	for i := 0; i < n; i++ {
		s[i] = (
			a[i].
			Clone().
			(IntSlice))
	}
	return s
}


func (
	a IntMatrix,
) Reverse() {
	Reverse(a)
}


func (
	a IntMatrix,
) Reversed() (
	s IntMatrix,
) {
	s = (
		a.Clone().
		(IntMatrix))
	s.Reverse()
	return
}


func (
	a IntMatrix,
) CumSum() (
	b IntMatrix,
) {
	b = a.CumSum0().CumSum1()
	return
}


func (
	a IntMatrix,
) CumSum0() (
	b IntMatrix,
) {
	b = a.Clone().(IntMatrix)
	n := len(a)
	m := len(a[0])
	for i := 0; i < n-1; i++ {
		for j := 0; j < m; j++ {
			b[i+1][j] += b[i][j]
		}
	}
	return
}


func (
	a IntMatrix,
) CumSum1() (
	b IntMatrix,
) {
	b = a.Clone().(IntMatrix)
	n := len(a)
	m := len(a[0])
	for j := 0; j < m-1; j++ {
		for i := 0; i < n; i++ {
			b[i][j+1] += b[i][j]
		}
	}
	return
}


func (
	a IntMatrix,
) Modularize(
	mod Int,
) (
	b ModMatrix,
) {
	tmp := new(ModMatrix)
	n := Int(len(a))
	m := Int(len(a[0]))
	b = tmp.Make(n, m, mod)
	for i := Int(0); i < n; i++ {
		for
		j := Int(0); j < m; j++ {
			x := Modular{
				a[i][j],
				mod,
			}
			x.Init()
			b[i][j] = x
		}
	}
	return
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
	b = make(IS, n)
	for i := 0; i < n; i++ {
		b[i] = a[i]
	}
	return
}


func (
	a FloatSlice,
) CompSlice() (
	b CompSlice,
) {
	n := len(a)
	b = make(CompSlice, n)
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
		CompSlice,
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
		CompSlice,
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


func (
	a FloatSlice,
) BisectLeft(
	x Float,
) (
	i Int,
) {
	n := len(a)
	f := func(
		i int,
	) bool {
		return a[i] >= x
	}
	i = Int(sort.Search(n, f))
	return
}


func (
	a FloatSlice,
) BisectRight(
	x Float,
) (
	i Int,
) {
	n := len(a)
	f := func(
		i int,
	) bool {
		return a[i] > x
	}
	i = Int(sort.Search(n, f))
	return
}


func (
	a FloatSlice,
) LIS(
	inf Float,
) (
	lis FloatSlice,
) {
	b := a.CompSlice()
	b = b.LIS(inf)
	lis = b.FloatSlice()
	return
}



type Str string


func (
	s Str,
) Int() (
	Int,
) {
	i, _ := strconv.Atoi(
		string(s),
	)
	return Int(i)
}


func (
	s Str,
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
	s Str,
) Contains(
	t Str,
) (
	Bool,
) {
	bl := strings.Contains(
		string(s),
		string(t),
	)
	return Bool(bl)
}


func (
	x Str,
) LT(
	other Comparable,
) Bool {
	return x < other.(Str)
}


func (
	x Str,
) LE(
	other Comparable,
) Bool {
	return x <= other.(Str)
}


func (
	x Str,
) GE(
	other Comparable,
) Bool {
	return !x.LT(other)
}


func (
	x Str,
) GT(
	other Comparable,
) Bool {
	return !x.LE(other)
}


func (
	s *Str,
) Reverse() {
	a := s.RuneSlice()
	a.Reverse()
	*s = a.Str()
}


func (
	s Str,
) Reversed() (
	Str,
) {
	s.Reverse()
	return s
}


func (
	s *Str,
) Sort() {
	a := s.RuneSlice()
	a.Sort()
	*s = a.Str()
}


func (
	s Str,
) Sorted() (
	Str,
) {
	s.Sort()
	return s
}



type StrSlice []Str


func (
	a StrSlice,
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
	a StrSlice,
) IS() (
	b IS,
) {
	n := len(a)
	b = make(IS, n)
	for i := 0; i < n; i++ {
		b[i] = a[i]
	}
	return
}


func (
	a StrSlice,
) CompSlice() (
	b CompSlice,
) {
	n := len(a)
	b = make(CompSlice, n)
	for i := 0; i < n; i++ {
		b[i] = a[i]
	}
	return
}


func (
	a StrSlice,
) String() string {
	n := len(a)
	return fmt.Sprintf(
		SliceFormat(n, " "),
		a.IS()...,
	)
}


func (
	a StrSlice,
) Max() (
	Str,
) {
	b := make(
		CompSlice,
		len(a),
	)
	for i := range a {
		b[i] = a[i]
	}
	return Max(b...).(Str)
}


func (
	a StrSlice,
) Min() (
	Str,
) {
	b := make(
		CompSlice,
		len(a),
	)
	for i := range a {
		b[i] = a[i]
	}
	return Min(b...).(Str)
}


func (
	a StrSlice,
) Len() int {
	return len(a)
}


func (
	a StrSlice,
) Less(
	i, j int,
) bool {
	return a[i] < a[j]
}


func (
	a StrSlice,
) Swap(
	i, j int,
) {
	a[i], a[j] = a[j], a[i]
}


func (
	a StrSlice,
) Clone() (
	Slice,
) {
	n := len(a)
	s := make(StrSlice, n)
	copy(s, a)
	return s
}


func (
	a StrSlice,
) Reverse() {
	Reverse(a)
}


func (
	a StrSlice,
) Reversed() (
	s StrSlice,
) {
	s = a.Clone().(StrSlice)
	s.Reverse()
	return
}


func (
	a StrSlice,
) Sort() {
	sort.Sort(a)
}


func (
	a StrSlice,
) Sorted() (
	StrSlice,
) {
	a = a.Clone().(StrSlice)
	a.Sort()
	return a
}


func (
	a StrSlice,
) BisectLeft(
	x Str,
) (
	i Int,
) {
	n := len(a)
	f := func(
		i int,
	) bool {
		return a[i] >= x
	}
	i = Int(sort.Search(n, f))
	return
}


func (
	a StrSlice,
) BisectRight(
	x Str,
) (
	i Int,
) {
	n := len(a)
	f := func(
		i int,
	) bool {
		return a[i] > x
	}
	i = Int(sort.Search(n, f))
	return
}


func (
	a StrSlice,
) LIS(
	inf Str,
) (
	lis StrSlice,
) {
	b := a.CompSlice()
	b = b.LIS(inf)
	lis = b.StrSlice()
	return
}



type StrMatrix []StrSlice


func (
	a StrMatrix,
) Len() int {
	return len(a)
}


func (
	a StrMatrix,
) Swap(
	i, j int,
) {
	a[i], a[j] = a[j], a[i]
}

func (
	a StrMatrix,
) Clone() (
	Slice,
) {
	n := len(a)
	s := make(StrMatrix, n)
	for i := 0; i < n; i++ {
		s[i] = (
			a[i].
			Clone().
			(StrSlice))
	}
	return s
}


func (
	a StrMatrix,
) Reverse() {
	Reverse(a)
}


func (
	a StrMatrix,
) Reversed() (
	s StrMatrix,
) {
	s = (
		a.Clone().
		(StrMatrix))
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
	b = make(IS, n)
	for i := 0; i < n; i++ {
		b[i] = a[i]
	}
	return
}


func (
	a RuneSlice,
) CompSlice() (
	b CompSlice,
) {
	n := len(a)
	b = make(CompSlice, n)
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
) Str() (
	Str,
) {
	b := a.Standard()
	return Str(b)
}


func (
	a RuneSlice,
) Max() (
	Rune,
) {
	b := make(
		CompSlice,
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
		CompSlice,
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


func (
	a RuneSlice,
) BisectLeft(
	x Rune,
) (
	i Int,
) {
	n := len(a)
	f := func(
		i int,
	) bool {
		return a[i] >= x
	}
	i = Int(sort.Search(n, f))
	return
}


func (
	a RuneSlice,
) BisectRight(
	x Rune,
) (
	i Int,
) {
	n := len(a)
	f := func(
		i int,
	) bool {
		return a[i] > x
	}
	i = Int(sort.Search(n, f))
	return
}


func (
	a RuneSlice,
) LIS(
	inf Rune,
) (
	lis RuneSlice,
) {
	b := a.CompSlice()
	b = b.LIS(inf)
	lis = b.RuneSlice()
	return
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



type CompSlice []Comparable


func (
	a CompSlice,
) Make(
	n Int,
	v Comparable,
) (
	b CompSlice,
) {
	b = make(CompSlice, n)
	for i := Int(0); i < n; i++ {
		b[i] = v
	}
	return
}


func (
	a CompSlice,
) IntSlice() (
	b IntSlice,
) {
	n := len(a)
	b = make(IntSlice, n)
	for i := 0; i < n; i++ {
		b[i] = a[i].(Int)
	}
	return
}


func (
	a CompSlice,
) FloatSlice() (
	b FloatSlice,
) {
	n := len(a)
	b = make(FloatSlice, n)
	for i := 0; i < n; i++ {
		b[i] = a[i].(Float)
	}
	return
}


func (
	a CompSlice,
) StrSlice() (
	b StrSlice,
) {
	n := len(a)
	b = make(StrSlice, n)
	for i := 0; i < n; i++ {
		b[i] = a[i].(Str)
	}
	return
}


func (
	a CompSlice,
) RuneSlice() (
	b RuneSlice,
) {
	n := len(a)
	b = make(RuneSlice, n)
	for i := 0; i < n; i++ {
		b[i] = a[i].(Rune)
	}
	return
}


func BisectLeft(
	a CompSlice,
	x Comparable,
) (
	i Int,
) {
	n := len(a)
	f := func(
		i int,
	) bool {
		return bool(
			a[i].GE(x),
		)
	}
	i = Int(sort.Search(n, f))
	return
}


func BisectRight(
	a CompSlice,
	x Comparable,
) (
	i Int,
) {
	n := len(a)
	f := func(
		i int,
	) bool {
		return bool(
			a[i].GT(x),
		)
	}
	i = Int(sort.Search(n, f))
	return
}


func (
	a CompSlice,
) LIS(
	inf Comparable,
) (
	lis CompSlice,
) {
	n := Int(len(a))
	lis = lis.Make(n, inf)
	for _, x := range a {
		i := BisectLeft(lis, x)
		lis[i] = x
	}
	i := BisectLeft(lis, inf)
	lis = lis[:i]
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



type Modular struct {
	Value Int
	Mod Int
}


func (
	m *Modular,
) Init() {
	mod := m.Mod
	m.Value %= mod
	m.Value += mod
	m.Value %= mod
}


func (
	m Modular,
) String() string {
	return fmt.Sprint(m.Value)
}


func (
	m *Modular,
) Clone() (
	Modular,
) {
	return Modular(*m)
}


func (
	m *Modular,
) IAdd(
	other Modular,
) {
	m.Value += other.Value
	m.Init()
}


func (
	m Modular,
) Add(
	other Modular,
) Modular {
	m.IAdd(other)
	return m
}


func (
	m Modular,
) Neg() (
	Modular,
){
	m = Modular{
		Value: -m.Value,
		Mod: m.Mod,
	}
	m.Init()
	return m
}


func (
	m *Modular,
) ISub(
	other Modular,
) {
	negOther := other.Neg()
	m.IAdd(negOther)
}


func (
	m Modular,
) Sub(
	other Modular,
) (
	Modular,
) {
	m.ISub(other)
	return m
}


func (
	m *Modular,
) IMul(
	other Modular,
) {
	mod := m.Mod
	m.Value *= other.Value
	m.Value %= mod
}


func (
	m Modular,
) Mul(
	other Modular,
) (
	Modular,
) {
	m.IMul(other)
	return m
}


func (
	m *Modular,
) IDiv(
	other Modular,
) {
	invOther := other.Invert()
	m.IMul(invOther)
}


func (
	m Modular,
) Div(
	other Modular,
) (
	Modular,
) {
	m.IDiv(other)
	return m
}


func (
	m Modular,
) Pow(n Int) (
	Modular,
) {
	mod := m.Mod
	if n == 0 {
		return Modular{1, mod}
	}
	a := m.Pow(n >> 1)
	a.IMul(a)
	if n & 1 == 1 {
		a.IMul(m)
	}
	return a
}


func (
	m *Modular,
) IPow(n Int) {
	m.Value = m.Pow(n).Value
}


func (
	m Modular,
) Invert() (
	Modular,
) {
	return m.Pow(m.Mod - 2)
}


func (
	m Modular,
) Factorial() (
	fact []Modular,
) {
	n, mod := m.Value, m.Mod

	fact = make(
		[]Modular,
		n + 1,
	)
	e := Int(0)
	for i := e; i < n+1; i++ {
		fact[i] = Modular{i, mod}
	}
	fact[0] = Modular{1, mod}
	for i := e; i < n; i++ {
		fact[i+1].IMul(fact[i])
	}
	return
}


func (
	m Modular,
) InverseFactorial() (
	invFact []Modular,
) {
	n, mod := m.Value, m.Mod

	fact := m.Factorial()

	invFact = make(
		[]Modular,
		n + 1,
	)
	e := Int(0)
	invFact[n] = fact[n].Invert()
	for i := n; i > e; i-- {
		nx := Modular{i, mod}
		nx.IMul(invFact[i])
		invFact[i-1] = nx
	}
	return
}



type ModSlice []Modular



type ModMatrix []ModSlice


func (
	a ModMatrix,
) Shape() (
	n, m Int,
) {
	n = Int(len(a))
	m = Int(len(a[0]))
	return
}


func (
	a ModMatrix,
) Make(n, m, mod Int) (
	b ModMatrix,
) {
	b = make(
		ModMatrix,
		n,
	)
	for i := Int(0); i < n; i++ {
		b[i] = make(ModSlice, m)
		for
		j := Int(0); j < m; j++ {
			b[i][j] = Modular{0, mod}
		}
	}
	return
}


func (
	a ModMatrix,
) Identity(
	n Int,
) (
	e ModMatrix,
) {
	mod := a[0][0].Mod
	e = a.Make(n, n, mod)
	for i := Int(0); i < n; i++ {
		e[i][i] = Modular{1, mod}
	}
	return
}


func (
	a ModMatrix,
) Dot(
	b ModMatrix,
) (
	c ModMatrix,
) {
	n, _ := a.Shape()
	_, m := b.Shape()
	mod := a[0][0].Mod
	c = a.Make(n, m, mod)
	for i := Int(0); i < n; i++ {
		for
		j := Int(0);
		j < m;
		j++ {
			c.dotSupport(a, b, i, j)
		}
	}
	return
}


func (
	c ModMatrix,
) dotSupport(
	a, b ModMatrix,
	i, j Int,
) {
	l := len(b)
	for k := 0; k < l; k++ {
		c[i][j].IAdd(
			a[i][k].Mul(b[k][j]),
		)
	}
}


func (
	a ModMatrix,
) Pow(
	n Int,
) (
	ModMatrix,
) {
	m, _ := a.Shape()
	if n == 0 {
		return a.Identity(m)
	}
	b := a.Pow(n >> 1)
	b = b.Dot(b)
	if n & 1 == 1 {
		b = b.Dot(a)
	}
	return b
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
) Scan() Str {
	scanner := io.Scanner
	scanner.Scan()
	s := Str(scanner.Text())
	return s
}


func (
	io *IO,
) ScanInt() Int {
	s := io.Scan()
	return s.Int()
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
	n Int
	c IntSlice
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
	n := io.ScanInt()
	c := make(IntSlice, n)
	for i := Int(0); i < n; i++ {
		c[i] = io.ScanInt()
	}
	p.n, p.c = n, c
}


func (
	p *Problem,
) Solve() {
	io := p.io
	n, c := p.n, p.c
	const inf = 1 << 60
	lis := c.LIS(inf)
	l := n - Int(len(lis))
	io.Write(l)
}



func main() {
	p := new(Problem)
	Run(p)
}
