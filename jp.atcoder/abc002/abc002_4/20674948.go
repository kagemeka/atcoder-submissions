package main


import (
	"fmt"
)


import (
	"bufio"
	"os"
	"strconv"
)


const MaxBuffer = 1 << 20

type IO struct {
	Scanner *bufio.Scanner
	Reader *bufio.Reader
	Writer *bufio.Writer
}


func (
	io *IO,
) SetScanner() {
	scanner := bufio.NewScanner(
		os.Stdin,
	)
	scanner.Buffer(
		[]byte{},
		MaxBuffer,
	)
	scanner.Split(
		bufio.ScanWords,
	)
	io.Scanner = scanner
}

func (
	io *IO,
) SetReader() {
	reader := bufio.NewReader(
		os.Stdin,
	)
	io.Reader = reader
}

func(
	io *IO,
) SetWriter() {
	writer := bufio.NewWriter(
		os.Stdout,
	)
	io.Writer = writer
}


func (
	io *IO,
) Init() {
	if io.Scanner == nil {
		io.SetScanner()
	}
	if io.Reader == nil {
		io.SetReader()
	}
	if io.Writer == nil {
		io.SetWriter()
	}

}


func (
	io *IO,
) Scan() string {
	scanner := io.Scanner
	scanner.Scan()
	return scanner.Text()
}


func (
	io *IO,
) ScanInt() int {
	s := io.Scan()
	v, _ := strconv.Atoi(s)
	return v
}


type Solver interface{
	Init()
	Prepare()
	Solve()
}


func Run(s Solver) {
	s.Init()
	s.Prepare()
	s.Solve()
}


type Int int

func (
	i *Int,
) BitCount() (
	cnt Int,
){
	cnt = 0
	n := *i
	for n > 0 {
		cnt += n & 1
		n >>= 1
	}
	return
}


func MaxInt(
	a ...Int,
) (
	Int,
) {
	m := a[0]
	for _, x := range a {
		if x > m {m = x}
	}
	return m
}


type ABC002D struct {
	io *IO
	n int
	relations []Int
}


func (
	p *ABC002D,
) Init() {
	io := new(IO)
	io.Init()
	p.io = io
}


func (
	p *ABC002D,
) Prepare() {
	io := p.io
	n := io.ScanInt()
	m := io.ScanInt()

	relations := make(
		[]Int,
		n,
	)
	for i := 0; i < n; i++ {
		relations[i] |= 1 << i
	}
	for
	i := 0;
	i < m;
	i++ {
		a := io.ScanInt() - 1
		b := io.ScanInt() - 1
		relations[a] |= 1 << b
		relations[b] |= 1 << a
	}
	p.n = n
	p.relations = relations
}


func (
	p *ABC002D,
) Solve() {
	n := p.n
	relations := p.relations
	cnt := Int(0)

	for
	s := Int(0);
	s < 1<<n;
	s++ {
		t := s
		for i := 0; i < n; i++ {
			if ^s >> i & 1 == 1 {
				continue
			}
			t &= relations[i]
		}
		if t != s {
			continue
		}
		cnt = MaxInt(
			cnt,
			s.BitCount(),
		)
	}
	fmt.Println(cnt)
}


func main() {
	p := new(ABC002D)
	Run(p)
}
