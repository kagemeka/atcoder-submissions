package main


import (
	"bufio"
	"container/heap"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
	"unicode"
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



type BoolSlice []Bool


func (
	a BoolSlice,
) Make(
	n Int,
	v Bool,
) (
	b BoolSlice,
) {
	b = make(BoolSlice, n)
	for i := Int(0); i < n; i++ {
		b[i] = v
	}
	return
}


func (
	a BoolSlice,
) Any() (
	Bool,
) {
	for _, x := range a {
		if !x {
			continue
		}
		return true
	}
	return false
}


func (
	a BoolSlice,
) All() (
	Bool,
) {
	for _, x := range a {
		if x {
			continue
		}
		return false
	}
	return true
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
		Float(x).Pow(n).
		(Float))
}


func (
	x Int,
) Abs() (
	Numeric,
) {
	return Int(
		Float(x).Abs().
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
	if r * other >= 0 {
		return
	}
	q--
	r += other
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


func (
	i Int,
) NxtCmb() (
	j Int,
) {
	x := i & -i
	y := i + x
	j = i & ^y
	j /= x
	j >>= 1
	j |= y
	return
}


func (
	n Int,
) Divisors() (
	divs IntSlice,
) {
	for
	i := Int(1);
	i * i <= n;
	i++ {
		if n % i != 0 {
			continue
		}
		divs = append(divs, i)
		j := n / i
		if j == i {
			continue
		}
		divs = append(divs, j)
	}
	divs.Sort()
	return
}


func (
	i Int,
) GCD(
	j Int,
) (
	gcd Int,
) {
	if j == 0 {
		gcd = i.Abs().(Int)
		return
	}
	gcd = j.GCD(i % j)
	return
}


func (
	i Int,
) EGCD(
	j Int,
) (
	gcd, x, y Int,
) {
	if j == 0 {
		gcd = i.Abs().(Int)
		x = 1
		y = 0
		return
	}
	q, r := i.Divmod(j)
	gcd, y, x = j.EGCD(r)
	y -= q * x
	return
}


func (
	i Int,
) LCM(
	j Int,
) (
	lcm Int,
) {
	gcd := i.GCD(j)
	lcm = i / gcd * j
	lcm = lcm.Abs().(Int)
	return
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
) Make(
	n Int,
	v Int,
) (
	b IntSlice,
) {
	b = make(IntSlice, n)
	for i := Int(0); i < n; i++ {
		b[i] = v
	}
	return
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
		b[i + 1] += b[i]
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
		b[i + 1] *= b[i]
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
		b[i + 1] = Max(
			b[i + 1],
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


func (
	a *IntSlice,
) PushBack(x Int) {
	*a = append(*a, x)
}


func (
	a *IntSlice,
) PopFront() (
	x Int,
) {
	x = (*a)[0]
	*a = (*a)[1:]
	return
}


func (
	a IntSlice,
) BitMatrix() (
	b BitMatrix,
) {
	n := len(a)
	b = make(BitMatrix, n)
	for i := 0; i < n; i++ {
		b[i] = IntSlice{a[i]}
	}
	return
}


func (
	a IntSlice,
) Modularize(
	mod Int,
) (
	b ModSlice,
) {
	n := len(a)
	b = make(ModSlice, n)
	for i := 0; i < n; i++ {
		v := Modular{a[i], mod}
		v.Init()
		b[i] = v
	}
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
) Make(
	n, m Int,
	v Int,
) (
	b IntMatrix,
) {
	b = make(IntMatrix, n)
	for i := Int(0); i < n; i++ {
		b[i] = b[i].Make(m, v)
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
	a *IntMatrix,
) PushBack(x IntSlice) {
	*a = append(*a, x)
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
	for i := 0; i < n - 1; i++ {
		for j := 0; j < m; j++ {
			b[i + 1][j] += b[i][j]
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
	for j := 0; j < m - 1; j++ {
		for i := 0; i < n; i++ {
			b[i][j + 1] += b[i][j]
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
	n, _ := a.Shape()
	b = make(ModMatrix, n)
	for i := Int(0); i < n; i++ {
		b[i] = a[i].Modularize(mod)
	}
	return
}



type BitMatrix IntMatrix


func (
	a BitMatrix,
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
	a BitMatrix,
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
	a BitMatrix,
) Make(n, m Int) (
	b BitMatrix,
) {
	b = make(BitMatrix, n)
	for i := Int(0); i < n; i++ {
		b[i] = make(IntSlice, m)
	}
	return
}


func (
	a BitMatrix,
) Shape() (
	n, m Int,
) {
	n = Int(len(a))
	m = Int(len(a[0]))
	return
}


func (
	a BitMatrix,
) Len() int {
	return len(a)
}


func (
	a BitMatrix,
) Swap(
	i, j int,
) {
	a[i], a[j] = a[j], a[i]
}


func (
	a BitMatrix,
) Clone() (
	Slice,
) {
	n := len(a)
	s := make(BitMatrix, n)
	for i := 0; i < n; i++ {
		s[i] = (
			a[i].
			Clone().
			(IntSlice))
	}
	return s
}


func (
	a BitMatrix,
) Reverse() {
	Reverse(a)
}


func (
	a BitMatrix,
) Reversed() (
	s BitMatrix,
) {
	s = (
		a.Clone().
		(BitMatrix))
	s.Reverse()
	return
}


func (
	a BitMatrix,
) Identity(
	n Int,
) (
	e BitMatrix,
) {
	e = a.Make(n, n)
	for i := Int(0); i < n; i++ {
		e[i][i] = ^0
	}
	return
}


func (
	a BitMatrix,
) Dot(
	b BitMatrix,
) (
	c BitMatrix,
) {
	n, _ := a.Shape()
	_, m := b.Shape()
	c = a.Make(n, m)
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
	c BitMatrix,
) dotSupport(
	a, b BitMatrix,
	i, j Int,
) {
	l := len(b)
	for k := 0; k < l; k++ {
		p := a[i][k] & b[k][j]
		c[i][j] ^= p
	}
}


func (
	a BitMatrix,
) Pow(
	n Int,
) (
	BitMatrix,
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
	const x0 = 1e13
	root = Newton(f, x0)
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
) Make(
	n Int,
	v Float,
) (
	b FloatSlice,
) {
	b = make(FloatSlice, n)
	for i := Int(0); i < n; i++ {
		b[i] = v
	}
	return
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



type FloatMatrix []FloatSlice


func (
	a FloatMatrix,
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
	a FloatMatrix,
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
	a FloatMatrix,
) Make(
	n, m Int,
	v Float,
) (
	b FloatMatrix,
) {
	b = make(FloatMatrix, n)
	for i := Int(0); i < n; i++ {
		b[i] = b[i].Make(m, v)
	}
	return
}

func (
	a FloatMatrix,
) Shape() (
	n, m Int,
) {
	n = Int(len(a))
	m = Int(len(a[0]))
	return
}


func (
	a FloatMatrix,
) Len() int {
	return len(a)
}


func (
	a FloatMatrix,
) Swap(
	i, j int,
) {
	a[i], a[j] = a[j], a[i]
}


func (
	a FloatMatrix,
) Clone() (
	Slice,
) {
	n := len(a)
	s := make(FloatMatrix, n)
	for i := 0; i < n; i++ {
		s[i] = (
			a[i].
			Clone().
			(FloatSlice))
	}
	return s
}


func (
	a FloatMatrix,
) Reverse() {
	Reverse(a)
}


func (
	a FloatMatrix,
) Reversed() (
	s FloatMatrix,
) {
	s = (
		a.Clone().
		(FloatMatrix))
	s.Reverse()
	return
}


func (
	a FloatMatrix,
) CumSum() (
	b FloatMatrix,
) {
	b = a.CumSum0().CumSum1()
	return
}


func (
	a FloatMatrix,
) CumSum0() (
	b FloatMatrix,
) {
	b = a.Clone().(FloatMatrix)
	n := len(a)
	m := len(a[0])
	for i := 0; i < n - 1; i++ {
		for j := 0; j < m; j++ {
			b[i + 1][j] += b[i][j]
		}
	}
	return
}


func (
	a FloatMatrix,
) CumSum1() (
	b FloatMatrix,
) {
	b = a.Clone().(FloatMatrix)
	n := len(a)
	m := len(a[0])
	for j := 0; j < m - 1; j++ {
		for i := 0; i < n; i++ {
			b[i][j + 1] += b[i][j]
		}
	}
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
) Sub(
	l, r Int,
) (
	sub Str,
){
	a := s.RuneSlice()
	a = a[l:r]
	sub = a.Str()
	return
}


func (
	s Str,
) RuneSlice() (
	a RuneSlice,
) {
	a = RuneSlice(s)
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


func (
	s Str,
) Lower() (
	Str,
) {
	t := string(s)
	t = strings.ToLower(t)
	return Str(t)
}


func (
	s Str,
) Upper() (
	Str,
) {
	t := string(s)
	t = strings.ToUpper(t)
	return Str(t)
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
) Make(
	n Int,
	v Str,
) (
	b StrSlice,
) {
	b = make(StrSlice, n)
	for i := Int(0); i < n; i++ {
		b[i] = v
	}
	return
}


func (
	s StrSlice,
) Join(
	sep Str,
) (
	Str,
) {
	t := strings.Join(
		s.Standard(),
		string(sep),
	)
	return Str(t)
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



func (
	x Rune,
) Lower() (
	Rune,
) {
	y := rune(x)
	y = unicode.ToLower(y)
	return Rune(y)
}


func (
	x Rune,
) Upper() (
	Rune,
) {
	y := rune(x)
	y = unicode.ToUpper(y)
	return Rune(y)
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
) Make(
	n Int,
	v Rune,
) (
	b RuneSlice,
) {
	b = make(RuneSlice, n)
	for i := Int(0); i < n; i++ {
		b[i] = v
	}
	return
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



type RuneMatrix []RuneSlice


func (
	a RuneMatrix,
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
	a RuneMatrix,
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
	a RuneMatrix,
) Make(
	n, m Int,
	v Rune,
) (
	b RuneMatrix,
) {
	b = make(RuneMatrix, n)
	for i := Int(0); i < n; i++ {
		b[i] = b[i].Make(m, v)
	}
	return
}


func (
	a RuneMatrix,
) Shape() (
	n, m Int,
) {
	n = Int(len(a))
	m = Int(len(a[0]))
	return
}


func (
	a RuneMatrix,
) Len() int {
	return len(a)
}


func (
	a RuneMatrix,
) Swap(
	i, j int,
) {
	a[i], a[j] = a[j], a[i]
}


func (
	a RuneMatrix,
) Clone() (
	Slice,
) {
	n := len(a)
	s := make(RuneMatrix, n)
	for i := 0; i < n; i++ {
		s[i] = (
			a[i].
			Clone().
			(RuneSlice))
	}
	return s
}


func (
	a RuneMatrix,
) Reverse() {
	Reverse(a)
}


func (
	a RuneMatrix,
) Reversed() (
	s RuneMatrix,
) {
	s = (
		a.Clone().
		(RuneMatrix))
	s.Reverse()
	return
}


func (
	a *RuneMatrix,
) PushBack(x RuneSlice) {
	*a = append(*a, x)
}


func (
	a RuneMatrix,
) Flatten() (
	b RuneSlice,
) {
	a = a.Clone().(RuneMatrix)
	n, m := a.Shape()
	b = make(RuneSlice, 0, n * m)
	for i := Int(0); i < n; i++ {
		b = append(b, a[i]...)
	}
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
	Add(Numeric) Numeric
	Neg() Numeric
	Sub(Numeric) Numeric
	Mul(Numeric) Numeric
	Pow(Int) Numeric
	Root(Int) Float
	Abs() Numeric
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



type Vector2D struct {
	X, Y Numeric
}


func (
	v Vector2D,
) Norm() (
	norm Float,
) {
	x2 := v.X.Pow(2)
	y2 := v.Y.Pow(2)
	norm = x2.Add(y2).Root(2)
	return
}


func (
	v *Vector2D,
) IAdd(
	other Vector2D,
) {
	v.X = v.X.Add(other.X)
	v.Y = v.Y.Add(other.Y)
}


func (
	v Vector2D,
) Add(
	other Vector2D,
) (
	Vector2D,
) {
	v.IAdd(other)
	return v
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
	v *Vector2D,
) ISub(
	other Vector2D,
) {
	v.X = v.X.Sub(other.X)
	v.Y = v.Y.Sub(other.Y)
}


func (
	v Vector2D,
) Sub(
	other Vector2D,
) (
	Vector2D,
) {
	v.ISub(other)
	return v
}


func (
	v *Vector2D,
) IMul(
	other Vector2D,
) {
	v.X = v.X.Mul(other.X)
	v.Y = v.Y.Mul(other.Y)
}


func (
	v Vector2D,
) Mul(
	other Vector2D,
) (
	Vector2D,
) {
	v.IMul(other)
	return v
}


func (
	v Vector2D,
) Dot(
	other Vector2D,
) (
	Numeric,
) {
	x := v.X.Mul(other.X)
	y := v.Y.Mul(other.Y)
	return x.Add(y)
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
	V0, V1, V2 Vector2D
}


func (
	t Triangle2D,
) SignedArea() (
	area Float,
) {
	V1 := t.V1.Sub(t.V0)
	V2 := t.V2.Sub(t.V0)
	cross := V1.Cross(V2)
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



type LineSegment2D struct {
	V0, V1 Vector2D
}


func (
	s LineSegment2D,
) Intersect(
	other LineSegment2D,
) (
	ok Bool,
) {
	bl0 := s.Across(other)
	bl1 := other.Across(s)
	ok = bl0 && bl1
	return
}


func (
	s LineSegment2D,
) Across (
	other LineSegment2D,
) (
	ok Bool,
) {
	o0 := other.Orientation(
		s.V0,
	)
	o1 := other.Orientation(
		s.V1,
	)
	ok = o0 * o1 <= 0
	return
}


func (
	s LineSegment2D,
) Orientation(
	v Vector2D,
) (
	o Int,
) {
	t := Triangle2D{
		s.V0,
		s.V1,
		v,
	}
	a := t.SignedArea()
	if a < 0 {return -1}
	if a == 0 {return 0}
	if a > 0 {return 1}
	return
}



type Rectangle2D struct{
	V0, V1 Vector2D
}



type Polygon2D []Vector2D



type Slice interface {
	Len() int
	Swap(i, j int)
	Clone() Slice
}


func Reverse(
	s Slice,
) {
	n := s.Len()
	for i := 0; i < n / 2; i++ {
		s.Swap(i, n - i - 1)
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
	const dx = 1
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
	const maxIter = 1 << 7
	const eps = 1e-9
	for
	i := 0;
	i < maxIter;
	i++ {
		y := f(x)
		der := f.Derivative(x)
		dx := y / der
		x -= dx
		dx = dx.Abs().(Float)
		if dx < eps {
			break
		}
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
	fact ModSlice,
) {
	n, mod := m.Value, m.Mod
	fact = make(ModSlice, n)
	for i := Int(0); i < n; i++ {
		fact[i] = Modular{i, mod}
	}
	fact[0] = Modular{1, mod}
	fact = fact.CumProd()
	return
}


func (
	m Modular,
) InverseFactorial() (
	invFact ModSlice,
) {
	n, mod := m.Value, m.Mod
	fact := m.Factorial()
	invFact = make(ModSlice, n)
	for i := Int(0); i < n; i++ {
		invFact[i] = Modular{
			n - i,
			mod,
		}
	}
	invFact[0] = (
		fact[n - 1].
		Invert())
	invFact = invFact.CumProd()
	invFact.Reverse()
	return
}



type ModSlice []Modular


func (
	a ModSlice,
) Make(
	n Int,
	v Modular,
) (
	b ModSlice,
) {
	b = make(ModSlice, n)
	for i := Int(0); i < n; i++ {
		b[i] = v
	}
	return
}


func (
	a ModSlice,
) Clone() (
	Slice,
) {
	n := len(a)
	s := make(ModSlice, n)
	copy(s, a)
	return s
}


func (
	a ModSlice,
) Len() int {
	return len(a)
}


func (
	a ModSlice,
) Swap(
	i, j int,
) {
	a[i], a[j] = a[j], a[i]
}


func (
	a ModSlice,
) Reverse() {
	Reverse(a)
}


func (
	a ModSlice,
) Reversed() (
	s ModSlice,
) {
	s = a.Clone().(ModSlice)
	s.Reverse()
	return
}


func (
	a ModSlice,
) CumSum() (
	b ModSlice,
) {
	b = a.Clone().(ModSlice)
	n := len(a)
	for i := 0; i < n - 1; i++ {
		b[i + 1].IAdd(b[i])
	}
	return
}


func (
	a ModSlice,
) CumProd() (
	b ModSlice,
) {
	b = a.Clone().(ModSlice)
	n := len(a)
	for i := 0; i < n - 1; i++ {
		b[i + 1].IMul(b[i])
	}
	return
}



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
) Make(
	n, m Int,
	v Modular,
) (
	b ModMatrix,
) {
	b = make(
		ModMatrix,
		n,
	)
	for i := Int(0); i < n; i++ {
		b[i] = b[i].Make(m, v)
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
	v := Modular{0, mod}
	e = e.Make(n, n, v)
	for i := Int(0); i < n; i++ {
		v := Modular{1, mod}
		e[i][i] = v
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
	v := Modular{0, mod}
	c = c.Make(n, m, v)
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



type ModChoose struct {
	Fact ModSlice
	InvFact ModSlice
	Mod Int
}


func (
	c *ModChoose,
) Init(n Modular) {
	c.Fact, c.InvFact =
		n.Factorial(),
		n.InverseFactorial()
	c.Mod = n.Mod
}


func (
	c *ModChoose,
) Calc(n, r Int) (
	Modular,
) {
	if r < 0 || r > n {
		return Modular{0, c.Mod}
	}
	return c.Fact[n].Mul(
		c.InvFact[r],
	).Mul(
		c.InvFact[n - r],
	)
}


func (
	c *ModChoose,
) Calculator() (
	choose func(
		n, r Int,
	) (
		Modular,
	),
) {
	return c.Calc
}



type PII [2]Int



type Binom map[PII]Modular



type Choose struct {
	cache Binom
	mod Int
}


func (
	c *Choose,
) Init(
	mod Int,
) {
	c.cache = make(Binom)
	c.mod = mod
}


func (
	c *Choose,
) Calc(
	n, r Int,
) (
	v Modular,
) {
	mod := c.mod
	if r > n || r < 0 {
		return Modular{0, mod}
	}
	if r == 0 {
		return Modular{1, mod}
	}
	i := PII{n, r}
	cache := c.cache
	if v, ok := cache[i]; ok {
		return v
	}
	v = c.Calc(n - 1, r)
	v.IAdd(c.Calc(n - 1, r - 1))
	cache[i] = v
	return
}


func (
	c *Choose,
) Calculator() (
	func(
		Int,
		Int,
	) Modular,
) {
	return c.Calc
}



type NChoose struct {
	Values ModSlice
}


func (
	c *NChoose,
) Init(
	n Int,
	r Modular,
) {
	ifac := r.InverseFactorial()
	l := Int(len(ifac))
	mod := r.Mod
	nChoose := c.Values.Make(
		l,
		Modular{1, mod},
	)
	for
	i := Int(0); i < l - 1; i++ {
		x := Modular{n - i, mod}
		x = nChoose[i].Mul(x)
		nChoose[i + 1] = x
	}
	for
	i := Int(0); i < l; i++ {
		nChoose[i].IMul(ifac[i])
	}
	c.Values = nChoose
}


func (
	c *NChoose,
) Get(
	i Int,
) (
	v Modular,
) {
	v = c.Values[i]
	return
}



type MII map[Int]Int



type Node struct {
	ID Int
}


func (
	v Node,
) String() (
	string,
) {
	return fmt.Sprint(v.ID)
}



type NodeSlice []Node



type Edge struct {
	ID Int
	From, To Int
	Weight Int
	Capacity Int
}



type EdgeSlice []Edge


func (
	edges *EdgeSlice,
) PushBack(
	e Edge,
) {
	*edges = append(*edges, e)
}



type EdgeMatrix []EdgeSlice



type Graph struct {
	Nodes NodeSlice
	Edges EdgeMatrix
}


func (
	g *Graph,
) Init(n Int) {
	nodes := make(NodeSlice, n)
	edges := make(EdgeMatrix, n)
	for i := Int(0); i < n; i++ {
		e :=  make(
			EdgeSlice,
			0,
		)
		edges[i] = e
	}
	g.Nodes = nodes
	g.Edges = edges
}


func (
	g *Graph,
) AddEdge(e Edge) {
	u := e.From
	g.Edges[u].PushBack(e)
}


func (
	g *Graph,
) AddEdges(
	edges EdgeSlice,
) {
	for _, e := range edges {
		g.AddEdge(e)
	}
}


func (
	g *Graph,
) AddNode(
	v Node,
) {
	g.Nodes[v.ID] = v
}



type Tree Graph


func (
	g *Tree,
) Init(n Int) {
	nodes := make(NodeSlice, n)
	edges := make(EdgeMatrix, n)
	for i := Int(0); i < n; i++ {
		e :=  make(
			EdgeSlice,
			0,
		)
		edges[i] = e
	}
	g.Nodes = nodes
	g.Edges = edges
}


func (
	g *Tree,
) AddEdge(e Edge) {
	u := e.From
	g.Edges[u].PushBack(e)
}


func (
	g *Tree,
) AddEdges(
	edges EdgeSlice,
) {
	for _, e := range edges {
		g.AddEdge(e)
	}
}


func (
	g *Tree,
) AddNode(
	v Node,
) {
	g.Nodes[v.ID] = v
}



type GraphBFS struct {
	G Graph
	Level IntSlice
	Que IntSlice
}


func (
	bfs *GraphBFS,
) SetGraph(
	g Graph,
) {
	bfs.G = g
}


func (
	bfs *GraphBFS,
) Prepare(
	src Int,
) {
	g := &bfs.G
	n := Int(len(g.Nodes))
	level := new(IntSlice).Make(
		n,
		-1,
	)
	level[src] = 0
	que := make(
		IntSlice,
		0,
	)
	que.PushBack(src)
	bfs.Level = level
	bfs.Que = que
}


func (
	bfs *GraphBFS,
) Search() {
	que := &bfs.Que
	for que.Len() > 0 {
		x := que.PopFront()
		bfs.Explore(x)
	}
}


func (
	bfs *GraphBFS,
) Explore(
	x Int,
) {
	u := x
	g := &bfs.G
	que := &bfs.Que
	lv := &bfs.Level
	for
	_, e := range g.Edges[u] {
		v := e.To
		if (*lv)[v] != -1 {
			continue
		}
		(*lv)[v] = (*lv)[u] + 1
		que.PushBack(v)
	}
}



type TreeBFS struct {
	G Tree
	Root Int
	Depth IntSlice
	Dist IntSlice
	Parent IntSlice
	Que IntSlice
}


func (
	bfs *TreeBFS,
) SetGraph(
	g Tree,
) {
	bfs.G = g
}


func (
	bfs *TreeBFS,
) Prepare(
	root Int,
) {
	g := &bfs.G
	n := Int(len(g.Nodes))
	depth := bfs.Depth.Make(
		n,
		-1,
	)
	depth[root] = 0
	dist := bfs.Dist.Make(
		n,
		-1,
	)
	dist[root] = 0
	parent := bfs.Parent.Make(
		n,
		-1,
	)
	parent[root] = root
	que := make(
		IntSlice,
		0,
	)
	que.PushBack(root)
	bfs.Depth = depth
	bfs.Dist = dist
	bfs.Parent = parent
	bfs.Que = que
}


func (
	bfs *TreeBFS,
) Search() {
	que := &bfs.Que
	for que.Len() > 0 {
		x := que.PopFront()
		bfs.Explore(x)
	}
}


func (
	bfs *TreeBFS,
) Explore(
	x Int,
) {
	u := x
	g := &bfs.G
	que := &bfs.Que
	depth := bfs.Depth
	dist := bfs.Dist
	parent := bfs.Parent
	for
	_, e := range g.Edges[u] {
		v := e.To
		d := e.Weight
		if depth[v] != -1 {
			continue
		}
		depth[v] = depth[u] + 1
		dist[v] = dist[u] + d
		parent[v] = u
		que.PushBack(v)
	}
}



type DijkstraItem struct {
	Node Int
	Dist Int
}


func (
	x DijkstraItem,
) LT(
	other DijkstraItem,
) Bool {
	return x.Dist < other.Dist
}



type DijkstraHeap [
]DijkstraItem


func (
	h DijkstraHeap,
) Len() int {
	return len(h)
}


func (
	h DijkstraHeap,
) Less(
	i, j int,
) bool {
	return bool(h[i].LT(h[j]))
}


func (
	h DijkstraHeap,
) Swap(
	i, j int,
) {
	h[i], h[j] = h[j], h[i]
}


func (
	h *DijkstraHeap,
) Push(
	x interface{},
) {
	*h = append(
		*h,
		x.(DijkstraItem),
	)
}


func (
	h *DijkstraHeap,
) Pop() (
	x interface{},
) {
	n := len(*h)
	x = (*h)[n-1]
	*h = (*h)[:n-1]
	return
}



type Dijkstra struct {
	G Graph
	Heap DijkstraHeap
	Dist IntSlice
	Paths ModSlice
	x DijkstraItem
	e Edge
}


func (
	di *Dijkstra,
) SetGraph(
	g Graph,
) {
	di.G = g
}


func (
	di *Dijkstra,
) Prepare(
	inf Int,
	src Int,
) {
	g := &di.G
	n := Int(len(g.Nodes))
	dist := new(IntSlice).Make(
		n,
		inf,
	)
	dist[src] = 0
	h := DijkstraHeap{}
	heap.Init(&h)
	x := DijkstraItem{
		Node: src,
		Dist: 0,
	}
	heap.Push(&h, x)
	di.Dist = dist
	di.Heap = h
}


func (
	di *Dijkstra,
) Search() {
	h := &di.Heap
	for h.Len() > 0 {
		di.Open()
		if di.Searched() {
			continue
		}
		di.Explore()
	}
}


func (
	di *Dijkstra,
) Open() {
	h := &di.Heap
	x := (
		heap.Pop(h).
		(DijkstraItem))
	di.x = x
}


func (
	di *Dijkstra,
) Searched() (
	Bool,
) {
	x := di.x
	i, d := x.Node, x.Dist
	return d > di.Dist[i]
}


func (
	di *Dijkstra,
) Explore() {
	u := di.x.Node
	edges := di.G.Edges
	for _, e := range edges[u] {
		di.e = e
		di.exploreSupport()
	}
}


func (
	di *Dijkstra,
) exploreSupport() {
	d := di.x.Dist
	e := di.e
	v := e.To
	d += e.Weight
	dist := di.Dist
	if d >= dist[v] {
		return
	}
	dist[v] = d
	x := DijkstraItem{
		Node: v,
		Dist: d,
	}
	heap.Push(&di.Heap, x)
}



type AStarItem struct {
	Node Int
	C, H, S Int
	Dist Int
}


func (
	x AStarItem,
) LT(
	other AStarItem,
) Bool {
	if x.S != other.S {
		return x.S < other.S
	}
	return x.H < other.H
}



type AStarHeap []AStarItem


func (
	h AStarHeap,
) Len() int {
	return len(h)
}


func (
	h AStarHeap,
) Less(
	i, j int,
) bool {
	return bool(h[i].LT(h[j]))
}


func (
	h AStarHeap,
) Swap(
	i, j int,
) {
	h[i], h[j] = h[j], h[i]
}


func (
	h *AStarHeap,
) Push(
	x interface{},
) {
	*h = append(
		*h,
		x.(AStarItem),
	)
}


func (
	h *AStarHeap,
) Pop() (
	x interface{},
) {
	n := len(*h)
	x = (*h)[n-1]
	*h = (*h)[:n-1]
	return
}



type HeuristicFunc func(
	Int,
) (
	Int,
)



type AStar struct {
	G Graph
	Heap AStarHeap
	Cost IntSlice
	F HeuristicFunc
	dst Int
	x AStarItem
	e Edge
}


func (
	a *AStar,
) SetGraph(
	g Graph,
) {
	a.G = g
}


func (
	a *AStar,
) SetHeuristicFunc(
	f HeuristicFunc,
) {
	a.F = f
}


func (
	a *AStar,
) Prepare(
	inf Int,
	src Int,
	dst Int,
) {
	a.dst = dst
	g := &a.G
	n := Int(len(g.Nodes))
	cost := new(IntSlice).Make(
		n,
		inf,
	)
	cost[src] = 0
	h := AStarHeap{}
	heap.Init(&h)
	c := cost[src]
	hc := a.F(src)
	s := 0 + hc
	x := AStarItem{
		Node: src,
		C: c,
		H: hc,
		S: s,
	}
	heap.Push(&h, x)
	a.Cost = cost
	a.Heap = h
}


func (
	a *AStar,
) Search() {
	h := &a.Heap
	for h.Len() > 0 {
		a.Open()
		if a.isDst() {
			return
		}
		if a.Searched() {
			continue
		}
		a.Explore()
	}
}


func (
	a *AStar,
) Open() {
	h := &a.Heap
	x := (
		heap.Pop(h).
		(AStarItem))
	a.x = x
}


func (
	a *AStar,
) isDst() (
	Bool,
) {
	x := a.x
	i := x.Node
	return i == a.dst
}


func (
	a *AStar,
) Searched() (
	Bool,
) {
	x := a.x
	i, c := x.Node, x.C
	return c > a.Cost[i]
}


func (
	a *AStar,
) Explore() {
	u := a.x.Node
	edges := a.G.Edges
	for _, e := range edges[u] {
		a.e = e
		a.exploreSupport()
	}
}


func (
	a *AStar,
) exploreSupport() {
	c := a.x.C
	e := a.e
	v := e.To
	c += e.Weight
	cost := a.Cost
	if c >= cost[v] {
		return
	}
	cost[v] = c
	h := a.F(c)
	s := c + h
	x := AStarItem{
		Node: v,
		C: c,
		H: h,
		S: s,
	}
	heap.Push(&a.Heap, x)
}



type FloydWarshall struct {
	G Graph
	Dist IntMatrix
	src, mid, dst int
}


func (
	fw *FloydWarshall,
) SetGraph(
	g Graph,
) {
	fw.G = g
}


func (
	fw *FloydWarshall,
) Prepare(
	inf Int,
) {
	g := &fw.G
	n := Int(len(g.Nodes))
	dist := fw.Dist.Make(
		n,
		n,
		inf,
	)
	fw.Dist = dist
	for i := Int(0); i < n; i++ {
		fw.prepareSupport(i)
	}
	for i := Int(0); i < n; i++ {
		dist[i][i] = 0
	}
}


func (
	fw *FloydWarshall,
) prepareSupport(
	i Int,
) {
	g := &fw.G
	dist := fw.Dist
	for
	_, e := range g.Edges[i] {
		j := e.To
		d := e.Weight
		dist[i][j] = Min(
			dist[i][j],
			d,
		).(Int)
	}
}


func (
	fw *FloydWarshall,
) Search() {
	n := len(fw.Dist)
	for k := 0; k < n; k++ {
		fw.mid = k
		fw.searchSupport0()
	}
}


func (
	fw *FloydWarshall,
) searchSupport0() {
	n := len(fw.Dist)
	for i := 0; i < n; i++ {
		fw.src = i
		fw.searchSupport1()
	}
}


func (
	fw *FloydWarshall,
) searchSupport1() {
	n := len(fw.Dist)
	k, i := fw.mid, fw.src
	d := fw.Dist
	for j := 0; j < n; j++ {
		d[i][j] = Min(
			d[i][j],
			d[i][k] + d[k][j],
		).(Int)
	}
}



type Dinic struct{
	G Graph
	Level IntSlice
	Src, Sink Int
}


func (
	di *Dinic,
) SetGraph(
	g Graph,
) {
	di.G = g
}


func (
	di *Dinic,
) Prepare(
	Src, Sink Int,
) {
	di.Src = Src
	di.Sink = Sink
}


func (
	di *Dinic,
) Search() (
	flow Int,
) {
	sink := di.Sink
	src := di.Src
	const inf = 1 << 60
	for {
		di.UpdateLevel()
		if di.Level[sink] == -1 {
			return
		}
		flow += di.FlowToSink(
			src,
			inf,
		)
	}
}


func (
	di *Dinic,
) UpdateLevel() {
	bfs := GraphBFS{}
	bfs.SetGraph(di.G)
	bfs.Prepare(di.Src)
	bfs.Search()
	di.Level = bfs.Level
}


func (
	di *Dinic,
) FlowToSink(
	u Int,
	in Int,
) (
	out Int,
) {
	if u == di.Sink {
		out = in
		return
	}
	g := &di.G
	lv := di.Level
	edges := g.Edges[u]
	nxtEdges := make(
		EdgeSlice,
		0,
		len(edges),
	)
	for _, e := range edges {
		v := e.To
		if lv[v] <= lv[u] {
			nxtEdges.PushBack(e)
			continue
		}
		f := di.FlowToSink(
			v,
			Min(
				in - out,
				e.Capacity,
			).(Int),
		)
		e.Capacity -= f
		if e.Capacity > 0 {
			nxtEdges.PushBack(e)
		}
		if f == 0 {
			continue
		}
		e = Edge{
			From: v,
			To: u,
			Capacity: f,
		}
		g.Edges[v].PushBack(e)
		out += f
	 }
	g.Edges[u] = nxtEdges
	return
}



type LCA struct {
	G Tree
	Parent IntSlice
	Ancestors IntMatrix
	Dist IntSlice
	Depth IntSlice
}


func (
	l *LCA,
) SetTree(
	g Tree,
) {
	l.G = g
}


func (
	l *LCA,
) Prepare(
	root Int,
) {
	bfs := TreeBFS{}
	bfs.SetGraph(l.G)
	bfs.Prepare(root)
	bfs.Search()
	l.Parent = bfs.Parent
	l.Depth = bfs.Depth
	l.Dist = bfs.Dist
}


func (
	l *LCA,
) FindAncestors() {
	n := Int(len(l.G.Nodes))
	ancestors := l.Ancestors
	m := l.Depth.Max().BitLen()
	ancestors = ancestors.Make(
		m,
		n,
		-1,
	)
	ancestors[0] = l.Parent
	l.Ancestors = ancestors
	for
	i := Int(0); i < m - 1; i++ {
		l.nxtAncestor(i)
	}
}


func (
	l *LCA,
) nxtAncestor(
	i Int,
) {
	n := Int(len(l.G.Nodes))
	x := l.Ancestors[i]
	y := make(
		IntSlice,
		n,
	)
	for i := Int(0); i < n; i++ {
		y[i] = x[x[i]]
	}
	l.Ancestors[i + 1] = y
}


func (
	l *LCA,
) FindDist(
	u, v Int,
) (
	d Int,
) {
	du := l.Dist[u]
	dv := l.Dist[v]
	lca := l.FindLCA(u, v)
	dLCA := l.Dist[lca]
	d = du + dv - 2 * dLCA
	return
}


func (
	l *LCA,
) FindLCA(
	u, v Int,
) (
	lca Int,
) {
	u, v = l.sort(u, v)
	du := l.Depth[u]
	dv := l.Depth[v]
	v = l.upStream(
		v,
		dv - du,
	)
	if v == u {
		lca = u
		return
	}
	lca = l.findLCASupport(
		du,
		u,
		v,
	)
	return
}


func (
	l *LCA,
) sort(
	u, v Int,
) (
	Int, Int,
) {
	du := l.Depth[u]
	dv := l.Depth[v]
	if du > dv {
		u, v = v, u
	}
	return u, v
}


func (
	l *LCA,
) upStream(
	v Int,
	d Int,
) (
	Int,
){
	n := d.BitLen()
	for i := Int(0); i < n; i++ {
		if ^d >> i & 1 == 1 {
			continue
		}
		v = l.Ancestors[i][v]
	}
	return v
}


func (
	l *LCA,
) findLCASupport(
	dep Int,
	u, v Int,
) (
	lca Int,
) {
	n := dep.BitLen()
	ancs := l.Ancestors
	for
	i := n - 1; i > -1; i-- {
		anc := ancs[i]
		nu, nv := anc[u], anc[v]
		if nu == nv {
			continue
		}
		u, v = nu, nv
	}
	lca = l.Parent[u]
	return
}



type DisjointSet struct {
	Parent IntSlice
	Rank IntSlice
	Size IntSlice
}


func (
	ds *DisjointSet,
) Init(
	n Int,
) {
	parent := make(IntSlice, n)
	for i := Int(0); i < n; i++ {
		parent[i] = i
	}
	rank := ds.Rank.Make(n, 0)
	size := ds.Size.Make(n, 1)
	ds.Parent = parent
	ds.Rank = rank
	ds.Size = size
}


func (
	ds *DisjointSet,
) Find(
	u Int,
) (
	root Int,
) {
	parent := ds.Parent
	v := parent[u]
	if v == u {
		root = u
		return
	}
	root = ds.Find(v)
	parent[u] = root
	return
}


func (
	ds *DisjointSet,
) Unite(
	u, v Int,
) {
	u = ds.Find(u)
	v = ds.Find(v)
	if u == v {
		return
	}
	u, v = ds.sort(u, v)
	rank := ds.Rank
	parent := ds.Parent
	size := ds.Size
	parent[v] = u
	size[u] += size[v]
	rank[u] = Max(
		rank[u],
		rank[v] + 1,
	).(Int)
}


func (
	ds *DisjointSet,
) sort(
	u, v Int,
) (
	Int, Int,
) {
	rank := ds.Rank
	if rank[u] < rank[v] {
		u, v = v, u
	}
	return u, v
}


func (
	ds *DisjointSet,
) Same(
	u, v Int,
) (
	Bool,
) {
	u = ds.Find(u)
	v = ds.Find(v)
	return u == v
}



type PrimeNum struct {
	Values IntSlice
	IsPrime BoolSlice
	n, i Int
}


func (
	pn *PrimeNum,
) Init(
	n Int,
) {
	pn.n = n
	pn.SieveOfEratosthenes()
	pn.Sparse()
}


func (
	pn *PrimeNum,
) SieveOfEratosthenes() {
	n := pn.n
	isPrime := pn.IsPrime.Make(
		n,
		true,
	)
	isPrime[0] = false
	isPrime[1] = false
	pn.IsPrime = isPrime
	for
	i := Int(0);
	i * i < n;
	i++ {
		if !isPrime[i] {
			continue
		}
		pn.i = i
		pn.sieveSupport()
	}
}


func (
	pn *PrimeNum,
) sieveSupport() {
	n, i := pn.n, pn.i
	isPrime := pn.IsPrime
	for
	j := Int(i * 2);
	j < n;
	j += i {
		isPrime[j] = false
	}
}


func (
	pn *PrimeNum,
) Sparse() {
	primeNums := pn.Values.Make(
		0,
		0,
	)
	isPrime := pn.IsPrime
	for i, ok := range isPrime {
		if !ok {
			continue
		}
		primeNums = append(
			primeNums,
			Int(i),
		)
	}
	pn.Values = primeNums
}


func (
	pn *PrimeNum,
) Get(
	i Int,
) (
	v Int,
) {
	v = pn.Values[i]
	return
}



type Factorization struct{
	primeNums IntSlice
	n, p Int
	factors, fFactors MII
}


func (
	f *Factorization,
) Init(
	n Int,
) {
	pn := new(PrimeNum)
	pn.Init(n)
	f.primeNums = pn.Values
}


func (
	f *Factorization,
) Calc(
	n Int,
) (
	factors MII,
) {
	factors = make(MII)
	f.factors = factors
	primeNums := f.primeNums
	for _, p := range primeNums {
		if n < 2 {return}
		if p * p > n {
			break
		}
		f.n, f.p = n, p
		f.calcSupport()
		n = f.n
	}
	factors[n]++
	return
}


func (
	f *Factorization,
) calcSupport() {
	n, p := f.n, f.p
	factors := f.factors
	for n % p == 0 {
		factors[p]++
		n /= p
	}
	f.n = n
}


func (
	f *Factorization,
) Factorial(
	n Int,
) (
	factors MII,
) {
	factors = make(MII)
	f.fFactors = factors
	for
	i := Int(1); i < n + 1; i++ {
		f.n = i
		f.factorialSupport()
	}
	return
}


func (
	f *Factorization,
) factorialSupport() {
	n := f.n
	factors := f.fFactors
	for p, c := range f.Calc(n) {
		factors[p] += c
	}
}



type DistXFormCDT struct {
	A IntMatrix
	B IntMatrix
	i, j Int
}


func (
	cdt *DistXFormCDT,
) SetMat(
	a IntMatrix,
) {
	cdt.A = a
}


func (
	cdt *DistXFormCDT,
) Prepare(
	inf Int,
) {
	a := cdt.A
	n, m := a.Shape()
	b := cdt.B.Make(n, m, inf)
	cdt.B = b
	for i := Int(0); i < n; i++ {
		cdt.i = i
		cdt.prepareSupport()
	}
}


func (
	cdt *DistXFormCDT,
) prepareSupport() {
	a := cdt.A
	b := cdt.B
	i := cdt.i
	_, m := b.Shape()
	for j := Int(0); j < m; j++ {
		if a[i][j] == 1 {
			continue
		}
		b[i][j] = 0
	}
}


func (
	cdt *DistXFormCDT,
) Taxicab() {
	n, m := cdt.B.Shape()
	for
	i := Int(0); i < n - 1; i++ {
		cdt.i = i
		cdt.downward()
	}
	for
	i := n - 1; i > 0; i-- {
		cdt.i = i
		cdt.upward()
	}
	for
	j := Int(0); j < m - 1; j++ {
		cdt.j = j
		cdt.rightward()
	}
	for
	j := m - 1; j > 0; j-- {
		cdt.j = j
		cdt.leftward()
	}
}


func (
	cdt *DistXFormCDT,
) downward() {
	b := cdt.B
	i := cdt.i
	_, m := b.Shape()
	for j := Int(0); j < m; j++ {
		b[i + 1][j] = Min(
			b[i + 1][j],
			b[i][j] + 1,
		).(Int)
	}
}


func (
	cdt *DistXFormCDT,
) upward() {
	b := cdt.B
	i := cdt.i
	_, m := b.Shape()
	for j := Int(0); j < m; j++ {
		b[i - 1][j] = Min(
			b[i - 1][j],
			b[i][j] + 1,
		).(Int)
	}
}


func (
	cdt *DistXFormCDT,
) rightward() {
	b := cdt.B
	j := cdt.j
	n, _ := b.Shape()
	for i := Int(0); i < n; i++ {
		b[i][j + 1] = Min(
			b[i][j + 1],
			b[i][j] + 1,
		).(Int)
	}
}


func (
	cdt *DistXFormCDT,
) leftward() {
	b := cdt.B
	j := cdt.j
	n, _ := b.Shape()
	for i := Int(0); i < n; i++ {
		b[i][j - 1] = Min(
			b[i][j - 1],
			b[i][j] + 1,
		).(Int)
	}
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
	s Str
	t IntSlice
}


func (
	p *Problem,
) Init() {
	io := new(IO)
	io.Init()
	const bufSize = 1 << 19
	io.SetScanBuf(bufSize)
	p.io = io
}


func (
	p *Problem,
) Prepare() {
	io := p.io
	p.s = io.Scan()
}


func (
	p *Problem,
) Solve() {
	io := p.io
	s := p.s
	n := Int(len(s))
	p.CountUp()
	t := p.t
	t.Sort()
	for
	i := Int(0); i < n / 2; i++ {
		t[i] *= - 1
	}
	tot := t.Sum()
	io.Write(tot)
}


func (
	p *Problem,
) CountUp() {
	s := p.s
	s.Reverse()
	t := make(IntSlice, 0)
	cnt := Int(0)
	for _, c := range s {
		if c == '+' {
			cnt++
			continue
		}
		if c == '-' {
			cnt--
			continue
		}
		t.PushBack(cnt)
	}
	p.t = t
}



func main() {
	p := new(Problem)
	Run(p)
}
