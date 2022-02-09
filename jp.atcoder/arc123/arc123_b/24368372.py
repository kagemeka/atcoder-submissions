from bisect import (
  bisect_right,
)


def main():
  n = int(input())
  a = [
    int(x)
    for x in input().split()
  ]
  b = [
    int(x)
    for x in input().split()
  ]
  c = [
    int(x)
    for x in input().split()
  ]
  a.sort()
  b.sort()
  c.sort()
  lb = -1
  rb = -1
  cnt = 0
  for x in a:
    i = bisect_right(b, x)
    if i <= lb: i = lb + 1
    if i == n: break
    lb = i
    x = b[i]
    i = bisect_right(c, x)
    if i <= rb: i = rb + 1
    if i == n: break
    rb = i
    cnt += 1
  print(cnt)




main()
