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


type String string

type Int int


func (
	i *Int,
) BitLength() (
	l Int,
){
	n := *i
	l = 0
	for n > 0 {
		l++
		n >>= 1
	}
	return
}

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

func (
	i Int,
) Pow(n Int) (
	Int,
){
	if n == 0 {
		return 1
	}
	a := i.Pow(n >> 1)
	a *= a
	if n & 1 == 1 {
		a *= i
	}
	return a
}


type Modular struct {
	Value Int
	Mod Int
}

func (
	m *Modular,
) Init() {
	mod := m.Mod
	m.Value %= mod
	m.Value += mod
	m.Value %= mod
}

func (
	m Modular,
) String() string {
	return fmt.Sprint(m.Value)
}


func (m *Modular) clone(
) Modular {
	return Modular(*m)
}


func (
	m *Modular,
) IAdd(
	other Modular,
) {
	m.Value += other.Value
	m.Init()
}

func (
	m *Modular,
) Add(
	other Modular,
) Modular {
	res := m.clone()
	res.IAdd(other)
	return res
}

func (
	m *Modular,
) Neg() (
	Modular,
){
	res := Modular{
		Value: -m.Value,
		Mod: m.Mod,
	}
	res.Init()
	return res
}

func (
	m *Modular,
) ISub(
	other Modular,
) {
	negOther := other.Neg()
	m.IAdd(negOther)
}

func (
	m *Modular,
) Sub(
	other Modular,
) (
	Modular,
) {
	res := m.clone()
	res.ISub(other)
	return res
}


func (
	m *Modular,
) IMul(
	other Modular,
) {
	mod := m.Mod
	m.Value *= other.Value
	m.Value %= mod
}

func (
	m *Modular,
) Mul(
	other Modular,
) (
	Modular,
) {
	res := m.clone()
	res.IMul(other)
	return res
}

func (
	m *Modular,
) IDiv(
	other Modular,
) {
	invOther := other.Invert()
	m.IMul(invOther)
}


func (
	m *Modular,
) Div(
	other Modular,
) (
	Modular,
) {
	res := m.clone()
	res.IDiv(other)
	return res
}


func (
	m *Modular,
) Pow(n Int) (
	Modular,
) {
	mod := m.Mod
	if n == 0 {
		return Modular{1, mod}
	}
	a := m.Pow(n >> 1)
	a.IMul(a)
	if n & 1 == 1 {
		a.IMul(*m)
	}
	return a
}

func (
	m *Modular,
) IPow(n Int) {
	m.Value = m.Pow(n).Value
}

func (
	m *Modular,
) Invert() (
	Modular,
) {
	return m.Pow(m.Mod - 2)
}


func (
	m *Modular,
) Factorial() (
	fact []Modular,
) {
	n, mod := m.Value, m.Mod

	fact = make(
		[]Modular,
		n + 1,
	)
	e := Int(0)
	for i := e; i < n+1; i++ {
		fact[i] = Modular{i, mod}
	}
	fact[0] = Modular{1, mod}
	for i := e; i < n; i++ {
		fact[i+1].IMul(fact[i])
	}
	return
}

func (
	m *Modular,
) InverseFactorial() (
	invFact []Modular,
) {
	n, mod := m.Value, m.Mod

	fact := m.Factorial()

	invFact = make(
		[]Modular,
		n + 1,
	)
	e := Int(0)
	invFact[n] = fact[n].Invert()
	for i := n; i > e; i-- {
		nx := Modular{i, mod}
		nx.IMul(invFact[i])
		invFact[i-1] = nx
	}
	return
}


type Combinations struct {
	Fact []Modular
	InvFact []Modular
	Mod Int
}


func (
	c *Combinations,
) Init(n Modular) {
	c.Fact, c.InvFact =
		n.Factorial(),
		n.InverseFactorial()
	c.Mod = n.Mod
}


func (
	c *Combinations,
) Choose(n, r Int) (
	comb Modular,
) {
	if r < 0 || r > n {
		return Modular{0, c.Mod}
	}
	comb = c.Fact[n]
	comb.IMul(
		c.InvFact[r],
	)
	comb.IMul(
		c.InvFact[n - r],
	)
	return
}


func (
	io *IO,
) Scan() String {
	scanner := io.Scanner
	scanner.Scan()
	s := String(scanner.Text())
	return s
}


func (
	io *IO,
) ScanInt() Int {
	s := string(io.Scan())
	v, _ := strconv.Atoi(s)
	return Int(v)
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



type Problem struct {
	io *IO
	r, c, x, y, d, l Int
	comb *Combinations
}


func (
	p *Problem,
) Init() {
	io := new(IO)
	io.Init()
	p.io = io
}


func (
	p *Problem,
) Prepare() {
	io := p.io
	r := io.ScanInt()
	c := io.ScanInt()
	y := io.ScanInt()
	x := io.ScanInt()
	d := io.ScanInt()
	l := io.ScanInt()
	comb := new(Combinations)
	mod := Int(1_000_000_007)
	n := Modular{r * c, mod}
	comb.Init(n)
	p.r = r
	p.c = c
	p.y = y
	p.x = x
	p.d = d
	p.l = l
	p.comb = comb
}


func (
	p *Problem,
) count(
	y, x Int,
) Modular {
	d, l := p.d, p.l
	comb := p.comb
	mod := comb.Mod
	if y < 0 || x < 0 {
		return Modular{0, mod}
	}
	if y * x < d + l {
		return Modular{0, mod}
	}
	c := comb.Choose(
		y * x, d + l,
	)
	c2 := comb.Choose(d + l, d)
	c.IMul(c2)
	return c
}

func (
	p *Problem,
) Solve() {
	r := p.r
	c := p.c
	y := p.y
	x := p.x
	mod := p.comb.Mod
	blocks := Modular{
		(r - y + 1) * (c - x + 1),
		mod,
	}
	n := 4
	s := Modular{0, mod}
	for
	i := Int(0);
	i < 1<<n;
	i++ {
		var bits [2]Int
		for j := 0; j < n; j++ {
			if ^i >> j & 1 == 1 {
				continue
			}
			bits[j & 1]++
		}
		f := Modular{
			Int(-1).Pow(
				i.BitCount(),
			),
			mod,
		}
		cnt := p.count(
			y - bits[0],
			x - bits[1],
		)

		s.IAdd(
			f.Mul(cnt),
		)
	}
	s.IMul(blocks)
	fmt.Println(s)

}



func main() {
	p := new(Problem)
	Run(p)
}
