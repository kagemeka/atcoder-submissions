package main



import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"sort"
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


// ac := new(ArrayCompression)
// ac.Compress(a []int)
// ac.Retrieve(i int)
type ArrayCompression struct { v []int }

func (ac *ArrayCompression) Compress(a []int) []int {
	buf := make(map[int]bool)
	for _, x := range a { buf[x] = true }
	v := make([]int, 0, len(buf))
	for k := range buf { v = append(v, k) }
	sort.Ints(v)
	n := len(a)
	rank := make([]int, n)
	for i := 0; i < n; i++ { rank[i] = sort.SearchInts(v, a[i]) }
	ac.v = v
	return rank
}

func (ac *ArrayCompression) Retrieve(i int) int { return ac.v[i] }


func SADoublingCountsort(a []int) (sa []int) {
	n := len(a)
	ac := new(ArrayCompression)
	rank, k := ac.Compress(a), 1
	key := make([]int, n)
	for {
		for i := 0; i < n; i++ {
			key[i] = rank[i] << 30
			if i + k < n { key[i] |= 1 + rank[i + k] }
		}
		sa = make([]int, n)
		for i := 0; i < n; i++ { sa[i] = i }
		sort.SliceStable(sa, func(i, j int) bool { return key[sa[i]] <= key[sa[j]] } )
		rank[sa[0]] = 0
		for i := 0; i < n - 1; i++ {
			rank[sa[i + 1]] = rank[sa[i]]
			if key[sa[i + 1]] > key[sa[i]] { rank[sa[i + 1]]++ }
		}
		k <<= 1
		if k >= n { break }
	}
	return
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
	stdio := NewStdIO()
	defer stdio.Flush()
	n, s := stdio.ScanInt(), stdio.Scan()
	a := make([]int, n)
	for i, c := range s { a[i] = int(c - 'a') }
	sa := SADoubling(a)
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
		for i := 0; i < n >> 1; i++ {
			j := n - 1 - i
			sa[i], sa[j] = sa[j], sa[i]
		}
		for i := 0; i < (n - 1) >> 1; i++ {
			j := n - 2 - i
			lcp[i], lcp[j] = lcp[j], lcp[i]
		}
	}
	for _, x := range res { stdio.Write(x) }
}
