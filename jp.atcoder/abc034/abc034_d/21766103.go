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



type Items []Item


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
	x := a[i].S()
	y := a[j].S()
	return x > y
	// if x.P != y.P {
	// 	return x.P > y.P
	// }
	// return x.W < y.W
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
		x := Item{}
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
	v := p.BinarySearch()
	fmt.Println(v)
}


func (
	p *Problem,
) Possible(
	v float64,
) bool {
	n := p.n
	items := make(Items, n)
	copy(items, p.items)
	for i := 0; i < n; i++ {
		items[i].P -= v
	}
	sort.Sort(items)
	k := p.k
	var s float64
	for i := 0; i < k; i++ {
		s += items[i].S()
	}
	return s > 0
}


func (
	p *Problem,
) BinarySearch() float64 {
	lo, hi := 0.0, 100.1
	const eps = 1e-13
	for hi - lo > eps {
		v := (hi + lo) / 2
		if p.Possible(v) {
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
