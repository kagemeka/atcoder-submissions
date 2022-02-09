
import sys
import numpy as np
import typing
import numba as nb


@nb.njit
def gcd(
  a: int,
  b: int,
) -> int:
  if not b:
    return a if a >= 0 else -a
  return gcd(b, a % b)


@nb.njit(
  (nb.i8, nb.i8[:, :]),
  cache=True,
)
def solve(
  n: int,
  ac: np.ndarray,
) -> typing.NoReturn:
  sort_idx = np.argsort(ac[:, 1], kind='mergesort')
  ac = ac[sort_idx]
  m = len(ac)
  g = np.zeros(m + 1, np.int64)
  g[0] = n
  g[1:] = ac[:, 0]
  for i in range(m):
    g[i + 1] = gcd(g[i], g[i + 1])

  if g[-1] > 1:
    print(-1)
    return

  s = np.sum(ac[:, 1] * (g[:-1] - g[1:]))
  print(s)


def main() -> typing:
  n, m = map(int, input().split())
  ac = np.array(
    sys.stdin.read().split(),
    dtype=np.int64,
  ).reshape(m, 2)
  solve(n, ac)


main()
