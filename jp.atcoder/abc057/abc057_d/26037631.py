import typing
import sys
import numpy as np
import numba as nb



@nb.njit
def choose_pascal(n: int) -> np.ndarray:
  choose = np.zeros((n + 1, n + 1), np.int64)
  choose[:, 0] = 1
  for i in range(1, n + 1):
    for j in range(1, n + 1):
      choose[i, j] = choose[i - 1, j] + choose[i - 1, j - 1]
  return choose


@nb.njit((nb.i8[:], nb.i8, nb.i8), cache=True)
def solve(v: np.ndarray, a: int, b: int) -> typing.NoReturn:
  n = len(v)
  v.sort()
  m = np.mean(v[-a:])
  r = np.searchsorted(v, v[-a], side='right')
  l = np.searchsorted(v, v[-a], side='left')
  cand = r - l

  choose = choose_pascal(50)
  if r < n:
    cnt = choose[cand, r - n + a]
  else:
    cnt = 0
    for i in range(a, b + 1):
      cnt += choose[cand, i]

  print(m)
  print(cnt)


def main() -> typing.NoReturn:
  n, a, b = map(int, input().split())
  v = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  solve(v, a, b)


main()
