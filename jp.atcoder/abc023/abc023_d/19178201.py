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
  import numpy as np
  return np.fromstring(
    string=read().decode(),
    dtype=np.int64,
    sep=' ',
  )


import numpy as np

def solve(n, hs):
  h, s = np.transpose(hs)
  t = np.arange(n)

  def is_ok(x):
    bl = np.sort((x - h) // s) >= t
    return np.all(bl)

  lo, hi = 0, 10<<50,
  while lo + 1 < hi:
    x = (lo + hi) // 2
    if is_ok(x): hi = x
    else: lo = x
  print(hi)


def main():
  import numpy as np
  n = read_int()
  hs = read_ints().reshape(n, 2)
  solve(n, hs)


if __name__ == '__main__':
  main()
