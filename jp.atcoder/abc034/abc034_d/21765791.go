package main


import (
	"fmt"
	"sort"
)



type Item struct {
	W float64
	P float64
}


func (
	x Item,
) S() float64 {
	return x.W * x.P / 100
}



type Items []*Item


func (
	a Items,
) Len() int {
	return len(a)
}


func (
	a Items,
) Swap(
	i, j int,
) {
	a[i], a[j] = a[j], a[i]
}


func (
	a Items,
) Less(
	i, j int,
) bool {
	x := a[i].P
	y := a[j].P
	return x > y
}



type Problem struct {
	n, k int
	items Items
}


func (
	p *Problem,
) Prepare() {
	var n, k int
	fmt.Scan(&n, &k)
	items := make(Items, n)
	for i := 0; i < n; i++ {
		x := new(Item)
		fmt.Scan(&x.W, &x.P)
		items[i] = x
	}
	p.n = n
	p.k = k
	p.items = items
}


func (
	p *Problem,
) Solve() {
	sort.Sort(p.items)
	v := p.BinarySearch()
	fmt.Println(v)
}


func (
	p *Problem,
) Possible(
	v float64,
) bool {
	items := p.items
	cnt := 0
	var s, w float64
	for _, x := range items {
		ns := s + x.S()
		nw := w + x.W
		if p := ns / nw; p < v {
			continue
		}
		s = ns
		w = nw
		cnt++
		if cnt == p.k {
			return true
		}
	}
	return false
}


func (
	p *Problem,
) BinarySearch() float64 {
	lo, hi := 0.0, 100.1
	const eps = 1e-8
	for hi - lo > eps {
		v := (hi + lo) / 2
		if p.Possible(v / 100) {
			lo = v
		} else {
			hi = v
		}
	}
	return lo
}



func main() {
	p := new(Problem)
	p.Prepare()
	p.Solve()
}
