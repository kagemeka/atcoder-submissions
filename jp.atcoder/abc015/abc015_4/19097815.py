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


def solve(w, n, k, ab):
  import numpy as np
  val = np.zeros(
    shape=(k+1, w+1),
    dtype=np.int32,
  )
  for a, b in ab:
    np.maximum(
      val[1:, a:],
      val[:-1, :-a] + b,
      out=val[1:, a:],
    )
  print(val[k][w])


def main():
  w = read_int()
  n, k, *ab = read_ints()
  ab = zip(*[iter(ab)]*2)
  solve(w, n, k, ab)


if __name__ == '__main__':
  main()
