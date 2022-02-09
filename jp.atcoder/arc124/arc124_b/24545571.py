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
  x = np.array((*cand, ))
  x.sort()
  y = x[:, None]
  ok = np.sort(
    y ^ a,
    axis=1,
  ) == np.sort(b)
  ok = ok.all(axis=1)
  res = list(x[ok])
  print(len(res))
  if res:
    print(*res, sep='\n')

main()
