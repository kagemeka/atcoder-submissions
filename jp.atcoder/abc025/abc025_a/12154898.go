package main

import (
  "fmt"
)

func productString(s string, repeat int) []string {
  queue := []string{""}
  for i := 0; i < repeat; i++ {
    l := len(queue)
    for j := 0; j < l; j++ {
      t := queue[0]
      for _, c := range s {queue = append(queue, t + string(c))}
      queue = queue[1:]
    }
  }
  return queue
}

func main() {
  var s string
  var n int
  fmt.Scan(&s, &n)
  res := productString(s, 2)
  fmt.Println(res[n-1])
}
