def readline():
  import sys
  return sys.stdin.buffer \
    .readline().rstrip()


def read_int():
  return int(readline())


def solve(s):
  print(f(s))


from functools import (
  lru_cache,
)

@lru_cache(maxsize=None)
def f(n):
  if n == 0: return 1
  if n == 1 or n == 2: return 0
  global mod
  return (f(n-1) + f(n-3)) % mod


def main():
  s = read_int()
  global mod
  mod = 10**9 + 7
  import sys
  sys.setrecursionlimit(10**6)
  solve(s)


if __name__ == '__main__':
  main()
