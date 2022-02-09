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


type SegmentTree struct {
	m Monoid
	size, n int
	data []interface{}
}

func NewSegmentTree(m Monoid, a []interface{}) *SegmentTree {
	size := len(a)
	n := 1 << BitLength(size - 1)
	data := make([]interface{}, n << 1)
	for i := 0; i < n << 1; i++ { data[i] = m.E() }
	for i := 0; i < size; i++ { data[n + i] = a[i] }
	seg := &SegmentTree{m, size, n, data}
	for i := n - 1; i > 0; i-- { seg.merge(i) }
	return seg
}

func (seg *SegmentTree) merge(i int) {
	seg.data[i] = seg.m.Op(seg.data[i << 1], seg.data[i << 1 | 1]);
}

func (seg *SegmentTree) Set(i int, x interface{}) {
	// 0 <= i < size
	i += len(seg.data) >> 1
	seg.data[i] = x
	for i > 1 { i >>= 1; seg.merge(i) }
}

func (seg *SegmentTree) Get(l, r int) interface{} {
	// 0 <= l <= r <= size
	n := len(seg.data) >> 1
	l += n; r += n;
	vl, vr := seg.m.E(), seg.m.E()
	for l < r {
		if l & 1 == 1 { vl = seg.m.Op(vl, seg.data[l]); l++ }
		if r & 1 == 1 { r--; vr = seg.m.Op(seg.data[r], vr) }
		l >>= 1; r >>= 1;
	}
	return seg.m.Op(vl, vr)
}

func (seg *SegmentTree) MaxRight(is_ok func(interface{}) bool, l int) int {
	// 0 <= l < size
	v, i := seg.m.E(), seg.n + l
	for {
		i /= i & -i
		if is_ok(seg.m.Op(v, seg.data[i])) {
			v = seg.m.Op(v, seg.data[i])
			i++
			if i & -i == i { return seg.size }
			continue
		}
		for i < seg.n {
			i <<= 1
			if !is_ok(seg.m.Op(v, seg.data[i])) { continue }
			i++
			v = seg.m.Op(v, seg.data[i])
		}
		return i - seg.n
	}
}


func Min(a ...int) int {
	// len(a) > 0
	mn := a[0]
	for _, x := range a { if x < mn { mn = x } }
	return mn
}


type node struct {
	s, mn int
}

func op(a, b interface{}) interface{} {
	x, y := a.(node), b.(node)
	return node{x.s + y.s, Min(x.mn, x.s + y.mn)}
}

func e() interface{} { return node{0, 1 << 30} }


func main() {
	stdio := NewStdIO()
	defer stdio.Flush()

	n, q := stdio.ScanInt(), stdio.ScanInt()
	s := stdio.Scan()
	a := make([]interface{}, n)
	for i := 0; i < n; i++ {
		var x int
		if s[i] == '(' { x = 1 } else { x = -1 }
		a[i] = node{x, x}
	}
	m := Monoid{op, e, false}
	seg := NewSegmentTree(m, a)
	for ; q > 0; q-- {
		t, l, r := stdio.ScanInt(), stdio.ScanInt(), stdio.ScanInt()
		l--; r--;
		if t == 1 {
			seg.Set(l, a[r])
			seg.Set(r, a[l])
			a[l], a[r] = a[r], a[l]
		} else {
			res := seg.Get(l, r + 1).(node)
			var ans string = "No"
			if res.s == 0 && res.mn >= 0 { ans = "Yes" }
			stdio.Write(ans)
		}
	}

}
