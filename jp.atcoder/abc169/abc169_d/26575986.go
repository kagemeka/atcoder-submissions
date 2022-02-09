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


func find_cnt(s int) int {
	cnt := 1
	for cnt * (cnt + 1) / 2 <= s {cnt ++}
	return cnt - 1
}


func main() {
	io := NewStdIO()
	n := io.ScanInt()


	cnt := 0
	i := 1
	for i * i < n {
		i++
		s := 0
		for n % i == 0 {
			s++
			n /= i
		}
		cnt += find_cnt(s)
	}
	if n > 1 { cnt++ }
	io.Write(cnt)
}
