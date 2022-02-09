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


func main() {
	io := NewStdIO()
	n := io.ScanInt()
	contain_zero := false
	a := make([]int, n)
	for i := 0; i < n; i++ {
		a[i] = io.ScanInt()
		if a[i] == 0 { contain_zero = true }
	}
	if contain_zero {
		io.Write(0)
		return
	}
	p := 1
	const t int = 1e18
	for _, x := range a {
		if p > t / x {
			io.Write(-1)
			return
		}
		p *= x
	}
	io.Write(p)

}
