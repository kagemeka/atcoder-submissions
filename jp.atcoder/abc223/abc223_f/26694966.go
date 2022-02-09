package main


import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)


// stdio := NewStdIO()
// defer stdio.Flush()
type StdIO struct {
	scanner *bufio.Scanner
	writer *bufio.Writer
}

func NewStdIO() *StdIO {
	const maxBuffer = 1 << 20
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Buffer([]byte{}, maxBuffer)
	scanner.Split(bufio.ScanWords)
	return &StdIO {
		scanner: scanner,
		writer: bufio.NewWriter(os.Stdout),
	}
}

func (stdio *StdIO) Scan() string {
	stdio.scanner.Scan()
	return stdio.scanner.Text()
}

func (stdio *StdIO) ScanInt() int {
	v, _ := strconv.Atoi(stdio.Scan())
	return v
}

func (stdio *StdIO) Write(a ...interface{}) {
	fmt.Fprintln(stdio.writer, a...)
}

func (stdio *StdIO) Flush() { stdio.writer.Flush() }


func BitLength(n int) int {
	l := 0
	for 1 << l <= n { l++ }
	return l
}


type Monoid struct {
	Op func(a, b interface{}) interface{}
	E func() interface{}
	Commutative bool
}


type SegmentTreeLazyConfig struct {
	S, F Monoid
	Map func(f, x interface{}) (y interface{})
}

type SegmentTreeLazy struct {
	c *SegmentTreeLazyConfig
	size, n, h int
	data, lazy []interface{}
}

func NewSegmentTreeLazy(
	c *SegmentTreeLazyConfig,
	a []interface{},
) *SegmentTreeLazy {
	size := len(a)
	n := 1 << BitLength(size - 1)
	h := BitLength(n)
	data := make([]interface{}, n << 1)
	for i := 0; i < n << 1; i++ { data[i] = c.S.E() }
	for i := 0; i < size; i++ { data[n + i] = a[i] }
	lazy := make([]interface{}, n)
	for i := 0; i < n; i++ { lazy[i] = c.F.E() }
	seg := &SegmentTreeLazy{ c, size, n, h, data, lazy }
	for i := n - 1; i > 0; i-- { seg.merge(i) }
	return seg
}

func (seg *SegmentTreeLazy) merge(i int) {
	seg.data[i] = seg.c.S.Op(seg.data[i << 1], seg.data[i << 1 | 1]);
}

func (seg *SegmentTreeLazy) apply(i int, f interface{}) {
	seg.data[i] = seg.c.Map(f, seg.data[i])
	if i < seg.n { seg.lazy[i] = seg.c.F.Op(f, seg.lazy[i]) }
}

func (seg *SegmentTreeLazy) propagate(i int) {
	seg.apply(i << 1, seg.lazy[i])
	seg.apply(i << 1 | 1, seg.lazy[i])
	seg.lazy[i] = seg.c.F.E()
}


func (seg *SegmentTreeLazy) Set(l, r int, f interface{}) {
	// 0 <= l && l <= r && r <= size
	l += seg.n; r += seg.n
	for i := seg.h; i > -1; i-- {
		if (l >> i) << i != l { seg.propagate(l >> i) }
		if (r >> i) << i != r { seg.propagate((r - 1) >> i) }
	}
	l0, r0 := l, r
	for l < r {
		if l & 1 == 1 { seg.apply(l, f); l++ }
		if r & 1 == 1 { r--; seg.apply(r, f) }
		l >>= 1; r >>= 1
	}
	l, r = l0, r0
	for i := 1; i < seg.h + 1; i++ {
		if (l >> i) << i != l { seg.merge(l >> i) }
		if (r >> i) << i != r { seg.merge((r - 1) >> i) }
	}
}

func (seg *SegmentTreeLazy) Get(l, r int) interface{} {
	// 0 <= l && l <= r && r <= size
	l += seg.n; r += seg.n;
	for i := seg.h; i > -1; i-- {
		if (l >> i) << i != l { seg.propagate(l >> i) }
		if (r >> i) << i != r { seg.propagate((r - 1) >> i) }
	}
	vl, vr := seg.c.S.E(), seg.c.S.E()
	for l < r {
		if l & 1 == 1 { vl = seg.c.S.Op(vl, seg.data[l]); l++ }
		if r & 1 == 1 { r--; vr = seg.c.S.Op(seg.data[r], vr) }
		l >>= 1; r >>= 1;
	}
	return seg.c.S.Op(vl, vr)
}

func (seg *SegmentTreeLazy) Update(i int, x interface{}) {
	// 0 <= i && i < size
	i += seg.n
	for j := seg.h; j > -1; j-- { seg.propagate(i >> j) }
	seg.data[i] = x;
	for j := 1; j < seg.h + 1; j++ { seg.merge(i >> j) }
}


func Min(a ...int) int {
	// len(a) > 0
	mn := a[0]
	for _, x := range a { if x < mn { mn = x } }
	return mn
}


func main() {
	stdio := NewStdIO()
	defer stdio.Flush()

	n, q := stdio.ScanInt(), stdio.ScanInt()
	s := stdio.Scan()
	a := make([]int, n)
	b := make([]interface{}, n + 1)
	b[0] = 0
	for i := 0; i < n; i++ {
		if s[i] == '(' { a[i] = 1 } else { a[i] = -1 }
		b[i + 1] = b[i].(int) + a[i]
	}
	inf := 1 << 30
	e_s := func() interface{} { return inf }
	op_s := func(a, b interface{}) interface{} { return Min(a.(int), b.(int)) }
	e_f := func() interface{} { return 0 }
	op_f := func(f, g interface{}) interface{} { return f.(int) + g.(int) }
	mp := func(f, x interface{}) interface{} { return x.(int) + f.(int) }
	ms := Monoid{op_s, e_s, true}
	mf := Monoid{op_f, e_f, true}
	cfg := SegmentTreeLazyConfig{ms, mf, mp}
	seg := NewSegmentTreeLazy(&cfg, b)
	for ; q > 0; q-- {
		t, l, r := stdio.ScanInt(), stdio.ScanInt(), stdio.ScanInt()
		l--; r--;
		if t == 1 {
			seg.Set(l + 1, r + 1, a[r] - a[l])
			a[l], a[r] = a[r], a[l]
		} else {
			base := seg.Get(l, l + 1).(int)
			tot := seg.Get(r + 1, r + 2).(int) - base
			mn := seg.Get(l, r + 2).(int) - base
			var ans string = "No"
			if tot == 0 && mn >= 0 { ans = "Yes" }
			stdio.Write(ans)
		}
	}
}
