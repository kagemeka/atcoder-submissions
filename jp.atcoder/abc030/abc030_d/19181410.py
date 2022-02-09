def readline():
  import sys
  return sys.stdin.buffer \
    .readline().rstrip()


def read_int():
  return int(readline())


def readline_ints():
  *ints, = map(
    int,
    readline().split(),
  )
  return ints


def solve(n, a, k, b):
  order = [None] * n
  for i in range(n + 1):
    if str(i) == k:
      print(a + 1)
      return
    if order[a] is not None:
      l, d =  i - order[a], order[a]
      break
    order[a] = i
    a = b[a]

  import numpy as np
  m = len(k)
  r = [None] * m
  r[0] = 1
  for i in range(m - 1):
    r[i+1] = r[i] * 10 % l
  k = np.array([*map(int, k[::-1])])
  r = np.array(r)
  d = ((r*k).sum() - d) % l
  for _ in range(d): a = b[a]
  print(a+1)


def main():
  n, a = readline_ints()
  a -= 1
  k = readline().decode()
  b = [x-1 for x in readline_ints()]
  solve(n, a, k, b)


if __name__ == '__main__':
  main()
