package main



import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"sort"
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
	countingSortKey := func(a []int) (key []int) {
		cnt := make([]int, n + 2)
		for _, x := range a { cnt[x + 1]++ }
		for i := 0; i < n; i++ { cnt[i + 1] += cnt[i] }
		key = make([]int, n)
		for i := 0; i < n; i++ {
			key[cnt[a[i]]] = i
			cnt[a[i]]++
		}
		return key
	}

	ac := new(ArrayCompression)
	rank, k := ac.Compress(a), 1
	first := make([]int, n)
	second := make([]int, n)
	sa = make([]int, n)
	key := make([]int, n)
	for {
		for i := 0; i < n - k; i++ { second[i] = 1 + rank[i + k] }
		for i := n - k; i < n; i++ { second[i] = 0 }
		rankSecond := countingSortKey(second)
		for i, j := range rankSecond { first[i] = rank[j] }
		rankFirst := countingSortKey(first)
		for i, j := range rankFirst { sa[i] = rankSecond[j] }
		for i := 0; i < n; i++ {
			key[i] = first[rankFirst[i]] << 30 | second[sa[i]]
		}
		rank[sa[0]] = 0
		for i := 0; i < n - 1; i++ {
			rank[sa[i + 1]] = rank[sa[i]]
			if key[i + 1] > key[i] { rank[sa[i + 1]]++ }
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
	io := NewStdIO()
	s := io.Scan()
	n := len(s)
	a := make([]int, n)
	for i, c := range s { a[i] = int(c - 'a') }
	sa := SADoublingCountsort(a)
	lcp := LCPArrayKasai(a, sa)
	io.Write(n * (n + 1) / 2 - Sum(lcp...))
}
