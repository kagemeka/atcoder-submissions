import typing
import sys
import numpy as np
import numba as nb


@nb.njit((nb.i8[:], nb.i8), cache=True)
def solve(a: np.ndarray, k: int) -> typing.NoReturn:
  n = len(a)
  a = np.searchsorted(np.unique(a), a)
  m = a.max() + 1
  cnt = np.zeros(m, np.int64)

  r = 0
  mx = 0
  kind = 0
  for l in range(n):
    while r < n and kind <= k:
      x = a[r]
      if cnt[x] == 0:
        if kind == k: break
        kind += 1
      cnt[x] += 1
      r += 1
    mx = max(mx, r - l)
    x = a[l]
    cnt[x] -= 1
    kind -= cnt[x] == 0
  print(mx)



def main() -> typing.NoReturn:
  n, k = map(int, input().split())
  a = np.array(
    sys.stdin.readline().split(),
    dtype=np.int64,
  )
  solve(a, k)


main()
