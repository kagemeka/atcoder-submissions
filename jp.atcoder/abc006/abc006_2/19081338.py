import sys
sys.setrecursionlimit(10**8)

def readline():
  import sys
  return sys.stdin.buffer \
    .readline().rstrip()


def read_int():
  return int(readline())



from functools import (
  lru_cache,
)
@lru_cache(maxsize=None)
def f(n):
  if n == 0 or n == 1: return 0
  if n == 2: return 1
  global mod
  return (f(n-1) + f(n-2) + f(n-3)) % mod


def solve(n):
  print(f(n))


def main():
  n = read_int() - 1
  global mod
  mod = 10_007
  solve(n)


if __name__ == '__main__':
  main()
