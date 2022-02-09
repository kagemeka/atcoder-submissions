import typing
import numpy as np
import sys

def main() -> typing.NoReturn:
  n = int(input())
  a, b = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(2, n)
  cand = set(a[0] ^ b)
  k = 32
  i = np.arange(k)
  a = a[:, None] >> i & 1
  b = b[:, None] >> i & 1
  a = a.sum(axis=0)
  b = b.sum(axis=0)
  c = a + b
  d = a - b
  x = np.array((*cand, ))
  x.sort()
  y = x[:, None] >> i & 1
  ok = (d * (y ^ 1) == 0).all(
    axis=1,
  )
  ok &= (c * y == y * n).all(
    axis=1,
  )
  res = list(x[ok])
  print(len(res))
  if res:
    print(*res, sep='\n')


main()
