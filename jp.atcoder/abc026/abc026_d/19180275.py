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


def solve(a, b, c):
  from scipy.optimize import brenth
  import numpy as np

  def f(t):
    nonlocal a, b, c
    h = a*t + b*np.sin(c*t*np.pi) \
      - 100
    return h

  print(brenth(f, a=0, b=200))


def main():
  a, b, c = readline_ints()
  solve(a, b, c)


if __name__ == '__main__':
  main()
