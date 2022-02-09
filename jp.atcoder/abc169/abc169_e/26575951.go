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


func main() {
	io := NewStdIO()
	n := io.ScanInt()
	a, b := make([]int, n), make([]int, n)
	for i := 0; i < n; i++ {
		a[i], b[i] = io.ScanInt(), io.ScanInt()
	}
	sort.Ints(a)
	sort.Ints(b)

	if n & 1 == 1 {
		io.Write(b[n / 2] - a[n / 2] + 1)
	} else {
		mx := b[n / 2] + b[n / 2 - 1]
		mn := a[n / 2] + a[n / 2 - 1]
		io.Write(mx - mn + 1)
	}
}
