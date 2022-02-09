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
  r = 0
  mx = 0
  p = 1
  for l in range(n):
    while r < n and p * s[r] <= k:
      p *= s[r]
      r += 1
    mx = max(mx, r - l)
    if r < n:
      p *= s[r]
      r += 1
    p //= s[l]
  print(mx)


def main() -> typing.NoReturn:
  n, k = map(int, input().split())
  s = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  )
  solve(s, k)


main()
