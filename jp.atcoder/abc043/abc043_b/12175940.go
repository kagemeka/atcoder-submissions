package main

import (
	"fmt"
)

func main() {
	var s string; fmt.Scan(&s)
	res := ""
	for _, c := range s {
		if c == 'B' {
			if len(res) > 0 {res = res[:len(res)-1]}
		} else {
			res += string(c)
		}
	}
	fmt.Println(res)

}
