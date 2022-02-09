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



func Max(a ...int) int {
	// len(a) > 0
	mx := a[0]
	for _, x := range a { if x > mx { mx = x } }
	return mx
}


func Min(a ...int) int {
	// len(a) > 0
	mn := a[0]
	for _, x := range a { if x < mn { mn = x } }
	return mn
}


func Sum(a ...int) int {
	s := 0
	for _, x := range a { s += x }
	return s
}


func SAIS(a []int) (sa []int) {
	mn := Min(a...)
	for i, x := range a { a[i] = x - mn + 1 }
	a = append(a, 0)
	n := len(a)
	m := Max(a...) + 1
	isS := make([]bool, n)
	isLms := make([]bool, n)
	lms := make([]int, 0, n)
	for i := 0; i < n; i++ { isS[i] = true }
	for i := n - 2; i > -1; i-- {
		if a[i] == a[i + 1] {
			isS[i] = isS[i + 1]
		} else {
			isS[i] = a[i] < a[i + 1]
		}
	}
	for i := 1; i < n; i++ { isLms[i] = !isS[i - 1] && isS[i] }
	for i := 0; i < n; i++ { if isLms[i] { lms = append(lms, i) } }
	bucket := make([]int, m)
	for _, x := range a { bucket[x]++ }

	induce := func() []int {
		sa := make([]int, n)
		for i := 0; i < n; i++ { sa[i] = -1 }

		saIdx := make([]int, m)
		copy(saIdx, bucket)
		for i := 0; i < m - 1; i++ { saIdx[i + 1] += saIdx[i] }
		for j := len(lms) - 1; j > -1; j-- {
			i := lms[j]
			x := a[i]
			saIdx[x]--
			sa[saIdx[x]] = i
		}

		copy(saIdx, bucket)
		s := 0
		for i := 0; i < m; i++ { s, saIdx[i] = s + saIdx[i], s }
		for j := 0; j < n; j++ {
			i := sa[j] - 1
			if i < 0 || isS[i] { continue }
			x := a[i]
			sa[saIdx[x]] = i
			saIdx[x]++
		}

		copy(saIdx, bucket)
		for i := 0; i < m - 1; i++ { saIdx[i + 1] += saIdx[i] }
		for j := n - 1; j > -1; j-- {
			i := sa[j] - 1
			if i < 0 || !isS[i] { continue }
			x := a[i]
			saIdx[x]--
			sa[saIdx[x]] = i
		}

		return sa
	}

	sa = induce()

	lmsIdx := make([]int, 0, len(sa))
	for _, i := range sa { if isLms[i] { lmsIdx = append(lmsIdx, i) } }
	l := len(lmsIdx)
	rank := make([]int, n)
	for i := 0; i < n; i++ { rank[i] = -1 }
	r := 0; rank[n - 1] = r
	for i := 0; i < l - 1; i++ {
		j, k := lmsIdx[i], lmsIdx[i + 1]
		for d := 0; d < n; d++ {
			jIsLms, kIsLms := isLms[j + d], isLms[k + d]
			if a[j + d] != a[k + d] || jIsLms != kIsLms { r++; break }
			if d > 0 && (jIsLms || kIsLms) { break }
		}
		rank[k] = r
	}
	buf := make([]int, 0, l)
	for _, r := range rank { if r >= 0 { buf = append(buf, r) } }
	var lmsOrder []int
	if r == l - 1 {
		lmsOrder = make([]int, l)
		for i, r := range buf { lmsOrder[r] = i }
	} else {
		lmsOrder = SAIS(buf)
	}
	buf = make([]int, len(lms))
	for i, j := range lmsOrder { buf[i] = lms[j] }
	lms = buf
	return induce()[1:]
}


func LCPArrayKasai(a, sa []int) (lcp []int) {
	n := len(a)
	// len(sa) == n
	rank := make([]int, n)
	for i := 0; i < n; i++ { rank[i] = -1 }
	for i, j := range sa { rank[j] = i }
	lcp = make([]int, n - 1)
	h := 0
	for i := 0; i < n; i++ {
		if h > 0 { h-- }
		r := rank[i]
		if r == n - 1 { continue }
		j := sa[r + 1]
		for i + h < n && j + h < n {
			if a[i + h] != a[j + h] { break }
			h++
		}
		lcp[r] = h
	}
	return
}


func main() {
	io := NewStdIO()
	n, s := io.ScanInt(), io.Scan()
	a := make([]int, n)
	for i, c := range s { a[i] = int(c - 'a') }
	sa := SAIS(a)
	lcp := LCPArrayKasai(a, sa)

	res := make([]int, n)
	for i := 0; i < n; i++ { res[i] = n - i }
	for z := 0; z < 2; z++ {
		s := 0
		st := [][2]int{}
		for i := 0; i < n - 1; i++ {
			l := 1
			h := lcp[i]

			for len(st) > 0 && st[len(st) - 1][0] >= h {
				x := st[len(st) - 1]
				st = st[:len(st) - 1]
				l += x[1]
				s -= x[0] * x[1]
			}
			s += h * l
			st = append(st, [2]int{h, l})
			res[sa[i + 1]] += s
		}
		for i, j := 0, n - 1; i < j; i, j = i + 1, j - 1 {
			sa[i], sa[j] = sa[j], sa[i]
		}
		for i, j := 0, n - 2; i < j; i, j = i + 1, j - 1 {
			lcp[i], lcp[j] = lcp[j], lcp[i]
		}
	}
	for _, x := range res { io.Write(x) }
}
