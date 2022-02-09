package main


import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)


// io := NewStdIO()
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


type Monoid struct {
	Op func(a, b interface{}) interface{}
	E func() interface{}
	commutative bool
}


type Group struct {
	Monoid
	Inverse func(interface{}) interface{}
}



// seg := NewFenwickTree(m Monoid, a []interface{})
type FenwickTree struct {
	m Monoid
	data []interface{}
}

func NewFenwickTree(m Monoid, a []interface{}) *FenwickTree {
	n := len(a)
	data := make([]interface{}, n + 1)
	data[0] = m.E()
	for i := 0; i < n; i++ { data[i + 1] = a[i] }
	for i := 1; i < n + 1; i++ {
		j := i + (i & -i)
		if j < n + 1 { data[j] = m.Op(data[j], data[i]) }
	}
	fw := new(FenwickTree)
	fw.m, fw.data = m, data
	return fw
}

func (fw *FenwickTree) Set(i int, x interface{}) {
	// 0 <= i < size
	i += 1
	for i < len(fw.data) {
		fw.data[i] = fw.m.Op(fw.data[i], x)
		i += i & -i
	}
}

func (fw *FenwickTree) Get(i int) interface{} {
	// 0 <= i < len(fw.data) == size + 1
	v := fw.m.E()
	for i > 0 {
		v = fw.m.Op(v, fw.data[i])
		i -= i & -i
	}
	return v
}



// query := new(PointOperateXorRangeGetXor)
// query.Init(a []int)
type PointOperateXorRangeGetXor struct {
	fw *FenwickTree
}

func (q *PointOperateXorRangeGetXor) op(a, b interface{}) interface{} {
	return a.(int) ^ b.(int)
}

func (q *PointOperateXorRangeGetXor) e() interface{} { return 0 }

func (q *PointOperateXorRangeGetXor) inverse(a interface{}) interface{} {
	return a
}

func (q *PointOperateXorRangeGetXor) Init(a []int) {
	n := len(a)
	b := make([]interface{}, n)
	for i := 0; i < n; i++ { b[i] = a[i] }
	q.fw = NewFenwickTree(Monoid{Op: q.op, E: q.e, commutative: true}, b)
}

func (q *PointOperateXorRangeGetXor) Get(i int) int {
	return q.fw.Get(i).(int)
}

func (q *PointOperateXorRangeGetXor) Set(i int, x int) {
	q.fw.Set(i, x)
}

func (q *PointOperateXorRangeGetXor) GetRange(l, r int) int {
	return q.op(q.inverse(q.Get(l)), q.Get(r)).(int)
}


func main() {
	io := NewStdIO()
	query := new(PointOperateXorRangeGetXor)
	n, q := io.ScanInt(), io.ScanInt()
	a := make([]int, n)
	for i := 0; i < n; i++ { a[i] = io.ScanInt() }
	query.Init(a)
	res := make([]int, 0)
	for i := 0; i < q; i++ {
		t, x, y := io.ScanInt(), io.ScanInt(), io.ScanInt()
		if t == 1 {
			query.Set(x - 1, y)
		} else if t == 2 {
			res = append(res, query.GetRange(x - 1, y))
		}
	}
	// io.Write(res)
	for _, x := range res {
		io.Write(x)
	}
}
