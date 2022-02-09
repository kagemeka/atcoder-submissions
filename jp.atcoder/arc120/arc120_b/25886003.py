import typing
import sys
import numpy as np
import numba as nb



@nb.njit((nb.i8[:, :], ), cache=True)
def solve(a: np.ndarray) -> typing.NoReturn:
  mod = 998244353
  h, w = a.shape

  cnt = 1
  buf = np.zeros(3, np.int64)
  for p in range(h + w - 1):
    buf[:] = 0
    for i in range(min(p + 1, h)):
      j = p - i
      if j >= w: continue
      buf[a[i, j]] += 1
    if buf[1] == 0 and buf[2] == 0:
      cnt *= 2
    elif buf[1] >=1 and buf[2] >=1:
      cnt *= 0
    cnt %= mod
  print(cnt)



def main() -> typing.NoReturn:
  h, w = map(int, sys.stdin.buffer.readline().split())
  s = np.frombuffer(
    sys.stdin.buffer.read(),
    dtype='S1',
  ).reshape(h, w + 1)[:, :-1]
  a = np.empty((h, w), np.int64)
  a[s == b'.'] = 0
  a[s == b'R'] = 1
  a[s == b'B'] = 2
  solve(a)


main()
