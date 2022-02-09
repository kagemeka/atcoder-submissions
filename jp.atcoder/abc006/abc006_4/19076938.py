def read():
  import sys
  return sys.stdin.buffer.read()


def readline():
  import sys
  return sys.stdin.buffer \
    .readline().rstrip()


def read_int():
  return int(readline())


def read_ints():
  *ints, = map(
    int,
    read().split(),
  )
  return ints


def longest_increasing_sequence(a):
  from bisect import (
    bisect_left,
  )
  inf = float('inf')
  lis = [inf] * len(a)
  for x in a:
    lis[bisect_left(lis, x)] = x
  return lis


from typing import (
  List,
)

def solve(n: int, a: List[int]):
  inf = float('inf')
  lis = longest_increasing_sequence(
    a,
  )
  from bisect import (
    bisect_left,
  )
  print(n - bisect_left(lis, inf))


def main():
  n = read_int()
  c = read_ints()
  solve(n, c)


if __name__ == '__main__':
  main()
