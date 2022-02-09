package main



import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
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
	a := io.ScanInt()
	b := strings.Split(io.Scan(), ".")
	b1, _ := strconv.Atoi(b[0])
	b0, _ := strconv.Atoi(b[1])
	io.Write(a * (100 * b1 + b0) / 100)
}
