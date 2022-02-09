def readline():
  import sys
  return sys.stdin.buffer \
    .readline().rstrip()


def read():
  import sys
  return sys.stdin.buffer.read()


def readline_ints():
  *ints, = map(
    int,
    readline().split(),
  )
  return ints


def read_ints():
  import numpy as np
  return np.fromstring(
    string=read().decode(),
    dtype=np.int64,
    sep=' ',
  )


def bit_count(n):
  cnt = 0
  while n:
    cnt += n&1
    n >>= 1
  return cnt


import numpy as np

def solve(
    n: int, m: int,
    xy: np.ndarray) -> None:

  relations = [0] * n
  for x, y in xy:
    relations[x] |= 1<<y
    relations[y] |= 1<<x

  cnt = 0
  for s in range(1<<n):
    t = (1<<n)-1
    for i in range(n):
      if ~ s>>i & 1: continue
      t &= relations[i] | 1<<i
    if not s&t == s: continue
    cnt = max(cnt, bit_count(s))

  print(cnt)


def main():
  import numpy as np
  n, m = readline_ints()
  xy = read_ints().reshape(m, 2) - 1
  solve(n, m, xy)


if __name__ == '__main__':
  main()
