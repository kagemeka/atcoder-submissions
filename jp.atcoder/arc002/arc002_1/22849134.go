package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)


type Read struct {
	sc *bufio.Scanner
}


func (
	r *Read,
) Init() {
	r.SetScanner()
	const buf = 1 << 20
	r.SetBuf(buf)
}


func (
	r *Read,
) Int() (
	int,
) {
	s := r.Str()
	i, _ := strconv.Atoi(s)
	return i
}


func (
	r *Read,
) SetBuf(
	bufSize int,
)  {
	r.sc.Buffer(
		[]byte{},
		bufSize,
	)
}


func (
	r *Read,
) SetScanner() {
	sc := bufio.NewScanner(
		os.Stdin,
	)
	sc.Split(
		bufio.ScanWords,
	)
	r.sc = sc
}


func (
	r *Read,
) Str() (
	string,
) {
	sc := r.sc
	sc.Scan()
	return sc.Text()
}



type Message struct {
	Ok, Ng string
}


func main() {
	r := new(Read)
	r.Init()
	y := r.Int()
	msg := Message{
		Ok: "YES",
		Ng: "NO",
	}
	if y % 400 == 0 {
		fmt.Println(
			msg.Ok,
		)
		return
	}
	if y % 100 == 0 {
		fmt.Println(
			msg.Ng,
		)
		return
	}
	if y % 4 == 0 {
		fmt.Println(
			msg.Ok,
		)
		return
	}
	fmt.Println(
		msg.Ng,
	)
}
