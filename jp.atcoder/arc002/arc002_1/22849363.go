package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)



type IO struct {
	r *Read
	w *Write
}


func (
	io *IO,
) Init() {
	r := new(Read)
	r.Init()
	w := new(Write)
	w.Init()
	io.r, io.w = r, w
}


func (
	io *IO,
) Read() (
	string,
) {
	return io.r.Str()
}


func (
	io *IO,
) ReadInt() (
	int,
) {
	return io.r.Int()
}


func (
	io *IO,
) Write(
	a ...interface{},
) {
	io.w.All(a...)
}



type Read struct {
	sc *bufio.Scanner
}


func (
	r *Read,
) Init() {
	r.setScanner()
	const buf = 1 << 20
	r.setBuf(buf)
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
) setBuf(
	bufSize int,
)  {
	r.sc.Buffer(
		[]byte{},
		bufSize,
	)
}


func (
	r *Read,
) setScanner() {
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



type Write struct {
	writer *bufio.Writer
}


func (
	w *Write,
) All(
	a ...interface{},
) {
	writer := w.writer
	fmt.Fprintln(
		writer,
		a...,
	)
	writer.Flush()
}


func (
	w *Write,
) Init() {
	w.setWriter()
}


func (
	w *Write,
) setWriter() {
	w.writer = bufio.NewWriter(
		os.Stdout,
	)
}



type Message struct {
	Ok, Ng string
}



func main() {
	io := new(IO)
	io.Init()
	y := io.ReadInt()
	msg := Message{
		Ok: "YES",
		Ng: "NO",
	}
	if y % 400 == 0 {
		io.Write(
			msg.Ok,
		)
		return
	}
	if y % 100 == 0 {
		io.Write(
			msg.Ng,
		)
		return
	}
	if y % 4 == 0 {
		io.Write(
			msg.Ok,
		)
		return
	}
	io.Write(
		msg.Ng,
	)
}
