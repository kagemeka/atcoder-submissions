package main


import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)


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

func (io *StdIO) Scan() string {
	io.scanner.Scan()
	return io.scanner.Text()
}

func (io *StdIO) ScanInt() int {
	v, _ := strconv.Atoi(io.Scan())
	return v
}

func (io *StdIO) Write(a ...interface{}) {
	fmt.Fprintln(io.writer, a...)
	io.writer.Flush()
}


func BitLength(n int) int {
	l := 0
	for 1 << l <= n { l++ }
	return l
}


type Monoid struct {
	Op func(a, b interface{}) interface{}
	E func() interface{}
}


type SegmentTree struct {
	m Monoid
	size int
	data []interface{}
}

func NewSegmentTree(m Monoid, a []interface{}) *SegmentTree {
	size := len(a)
	n := 1 << BitLength(size - 1)
	data := make([]interface{}, n << 1)
	for i := 0; i < n << 1; i++ { data[i] = m.E() }
	for i := 0; i < size; i++ { data[n + i] = a[i] }
	for i := n - 1; i > 0; i-- {
		data[i] = m.Op(data[i << 1], data[i << 1 | 1])
	}
	seg := new(SegmentTree)
	seg.m, seg.size, seg.data = m, size, data
	return seg
}

func (seg *SegmentTree) Set(i int, x interface{}) {
	// 0 <= i < size
	i += len(seg.data) >> 1
	seg.data[i] = x
	for i > 1 {
		i >>= 1
		seg.data[i] = seg.m.Op(seg.data[i << 1], seg.data[i << 1 | 1])
	}
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


type PointSetRangeGetXor struct {
	seg *SegmentTree
}

func (q *PointSetRangeGetXor) op(a, b interface{}) interface{} {
	return a.(int) ^ b.(int)
}

func (q *PointSetRangeGetXor) e() interface{} { return 0 }

func (q *PointSetRangeGetXor) InitSeg(a []int) {
	n := len(a)
	b := make([]interface{}, n)
	for i := 0; i < n; i++ { b[i] = a[i] }
	q.seg = NewSegmentTree(Monoid{q.op, q.e}, b)
}

func (q *PointSetRangeGetXor) Get(l, r int) int {
	return q.seg.Get(l, r).(int)
}

func (q *PointSetRangeGetXor) Set(i int, x int) {
	q.seg.Set(i, x)
}


type PointOperateXorRangeGetXor struct {
	PointSetRangeGetXor
}

func (q *PointOperateXorRangeGetXor) Set(i int, x int) {
	q.seg.Set(i, q.op(q.Get(i, i + 1), x))
}


func main() {
	io := NewStdIO()
	query := PointOperateXorRangeGetXor{}
	n, q := io.ScanInt(), io.ScanInt()
	a := make([]int, n)
	for i := 0; i < n; i++ { a[i] = io.ScanInt() }
	query.InitSeg(a)
	res := make([]int, 0)
	for i := 0; i < q; i++ {
		t, x, y := io.ScanInt(), io.ScanInt(), io.ScanInt()
		if t == 1 {
			query.Set(x - 1, y)
		} else if t == 2 {
			res = append(res, query.Get(x - 1, y))
		}
	}
	// io.Write(res)
	for _, x := range res {
		io.Write(x)
	}
}
