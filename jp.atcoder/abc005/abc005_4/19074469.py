def read_int():
  return int(readline())


def read():
  import sys
  return sys.stdin.buffer.read()


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


def read_ints():
  import numpy as np
  return np.fromstring(
    string=read().decode(),
    dtype=np.int64,
    sep=' ',
  )


import numpy as np

def pad_(arr):
  return np.pad(
    arr,
    pad_width=((1, 0), (1, 0)),
    mode='constant',
    constant_values=((0, ), (0, )),
  )


def solve(
    n: int,
    d: np.ndarray,
    p: np.ndarray,
    ) -> None:

  s = pad_(
    d.cumsum(axis=0).cumsum(axis=1)
  )

  mx = np.zeros(
    shape=(n+1, n+1),
    dtype=np.int64,
  )
  for y in range(1, n+1):
    for x in range(1, n+1):
      mx[y, x] = np.amax(
        s[y:, x:] \
        - s[:-y, x:] - s[y:, :-x]
        + s[:-y, :-x]
      )

  res = np.arange(n**2+1)[:,None]
  i = np.arange(1, n+1)
  res = np.amax(
    mx[i, np.minimum(res//i, n)],
    axis=1,
  )

  print(*res[p], sep='\n')



def main():
  n = read_int()
  d = np.array([
    readline_ints()
    for _ in range(n)
  ])
  _ = read_int()
  p = read_ints()

  solve(n, d, p)


if __name__ == '__main__':
  main()
