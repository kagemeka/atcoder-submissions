def readline():
  import sys
  return sys.stdin.buffer \
    .readline().rstrip()


def readline_ints():
  *ints, = map(
    int,
    readline().split(),
  )
  return ints


import numpy as np

def get_result(n, a):
  b = list(range(n))
  for i in a[::-1]:
    b[i-1], b[i] = b[i], b[i-1]
  return b


def solve(n, a, d):
  a = get_result(n, a)
  a = np.array(a)
  res = f(a, d) + 1
  print(*res, sep='\n')


def f(a, n):
  if n == 0:
    return np.arange(a.size)
  b = f(a, n//2)
  b = b[b]
  if n&1: b = a[b]
  return b


def main():
  n, _, d = readline_ints()
  a = readline_ints()
  solve(n, a, d)


if __name__ == '__main__':
  main()
