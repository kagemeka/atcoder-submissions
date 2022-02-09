import typing
import sys
import numpy as np
import numba as nb


@nb.njit((nb.i8[:], nb.i8), cache=True)
def solve(s: np.ndarray, k: int) -> typing.NoReturn:
  n = len(s)
  for i in range(n):
    if s[i] != 0: continue
    print(n)
    return
  if k == 0:
    print(0)
    return
  l = 0
  mx = 0
  p = 1
  for r in range(n):
    p *= s[r]
    while p > k:
      p //= s[l]
      l += 1
    mx = max(mx, r - l + 1)
  print(mx)


def main() -> typing.NoReturn:
  n, k = map(int, input().split())
  s = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  )
  solve(s, k)


main()
