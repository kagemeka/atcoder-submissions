package main

import (
  "fmt"
)

func main() {
  var a [3][3]int
  for i := 0; i < 3; i++ {
    for j := 0; j < 3; j++ {
      fmt.Scan(&a[i][j])
    }
  }
  var n int
  fmt.Scan(&n)
  announced := make(map[int]bool)
  for i := 0; i < n; i++ {
    var b int
    fmt.Scan(&b)
    announced[b] = true
  }
  var res [3][3]bool
  for i := 0; i < 3; i++ {
    for j := 0; j < 3; j++ {
      if _, ok := announced[a[i][j]]; ok {
        res[i][j] = true
      }
    }
  }

  var flag bool
  for i := 0; i < 3; i++ {
    flag = true
    for j := 0; j < 3; j++ {
      if res[i][j] {continue}
      flag = false
      break
    }
    if flag {
      fmt.Println("Yes")
      return
    }
  }
  for j := 0; j < 3; j++ {
    flag = true
    for i := 0; i < 3; i++ {
      if res[i][j] {continue}
      flag = false
      break
    }
    if flag {
      fmt.Println("Yes")
      return
    }
  }
  flag = true
  for i := 0; i < 3; i++ {
    if res[i][i] {continue}
    flag = false
    break
  }
  if flag {
    fmt.Println("Yes")
    return
  }
  flag = true
  for i := 0; i < 3; i++ {
    if res[i][2-i] {continue}
    flag = false
    break
  }
  if flag {
    fmt.Println("Yes")
    return
  }
  fmt.Println("No")
}
